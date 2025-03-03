from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import OperationalError, connection

# for video processing
import cv2
import torch
import supervision as sv
from ultralytics import YOLO
from django.http import StreamingHttpResponse

from .models import Station
from .serializers import StationSerializer

# Create your views here.
@api_view(['GET'])
def get_all_station(request):
    if check_database_status():
        stations = Station.objects.values('id', 'stationName', 'trainLine', 'isOperating')
        return Response(stations)
    else:
        return Response(
            {"error": "Database is currently unavailable. Please try again later."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

@api_view(['GET'])
def get_station(request, id):
    station = get_object_or_404(Station, id = id)
    serializer = StationSerializer(station)
    return Response(serializer.data)


def check_database_status():
    try:
        connection.cursor()
        return True
    except OperationalError:
        return False
    

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are connected!"})
    

    # in Header
    # Authentication: Bearer <access key>


# Load YOLOv8n model
# Run on CUDA if available else, run on CPU (slower inference)
model = YOLO("yolov8n.pt").to("cuda" if torch.cuda.is_available() else "cpu")

# Process video frames
def generate_frames(src):
    while True:
        cap = cv2.VideoCapture(src)

        if not cap.isOpened():
            return Response({"message": "Error: Could not open video source"})

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            # Run YOLOv8 detection
            results = model(frame, verbose=False)[0] # verbose is set to false to suppress logs in terminal
            detections = sv.Detections.from_ultralytics(results)

            # Filter only people (COCO class ID for "person" is 0)
            detections = detections[detections.class_id == 0]

            # Render bounding boxes
            # box_annotator = sv.BoxAnnotator()
            # frame = box_annotator.annotate(scene=frame, detections=detections)

            # Show people count
            people_count = len(detections)
            cv2.putText(frame, f"People Count: {people_count}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Encode frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Yield the frame in HTTP streaming format
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        cap.release()


@api_view(['GET'])
def get_cctv_feed(request, id, platform_side):
    station = get_object_or_404(Station, id=id)

    # Ensure the station has a valid CCTV URL
    if not station.leftCCTV and not station.rightCCTV:
        return StreamingHttpResponse("No CCTVs available for this station.", status=404)

    match  platform_side:
        case 'left':
            if not station.leftCCTV:
                return StreamingHttpResponse("Selected CCTV is unavailable", status=404)
            return StreamingHttpResponse(generate_frames(station.leftCCTV),
                                        content_type='multipart/x-mixed-replace; boundary=frame')
        case 'right':
            if not station.rightCCTV:
                return StreamingHttpResponse("Selected CCTV is unavailable", status=404)
            return StreamingHttpResponse(generate_frames(station.rightCCTV),
                                        content_type='multipart/x-mixed-replace; boundary=frame')
        case _:
            return StreamingHttpResponse("Invalid URL", status=404)

