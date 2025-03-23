from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch
from .models import Station, HourlyDensity, DailyDensity


class TestViews(APITestCase):
    def setUp(self):
        Station.objects.create(id=1, stationName="Roosevelt", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        self.selected = Station.objects.create(id=2, stationName="Balintawak", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=3, stationName="Monumento", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=4, stationName="5th Avenue", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=5, stationName="R. Papa", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=6, stationName="Abad Santos", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=7, stationName="Blumentritt", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=8, stationName="Tayuman", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=9, stationName="Bambang", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=10, stationName="Doroteo Jose", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=11, stationName="Carriedo", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=12, stationName="Central Terminal", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=13, stationName="United Nations", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=14, stationName="Pedro Gil", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=15, stationName="Quirino", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=16, stationName="Vito Cruz", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=17, stationName="Gil Puyat", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=18, stationName="Libertad", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=19, stationName="EDSA", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=20, stationName="Baclaran", trainLine="LRT1", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=21, stationName="Recto", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=22, stationName="Legarda", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=23, stationName="Pureza", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=24, stationName="V. Mapa", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=25, stationName="J. Ruiz", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="", rightCCTV="", isOperating=True, stationIMG="")
        Station.objects.create(id=26, stationName="Gilmore", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=27, stationName="Betty Go-Belmonte", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=28, stationName="Araneta-Cubao", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=29, stationName="Anonas", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=30, stationName="Katipunan", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=31, stationName="Santolan", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=32, stationName="Marikina", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=33, stationName="Antipolo", trainLine="LRT2", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=34, stationName="North Avenue", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=35, stationName="Quezon Avenue", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=36, stationName="Kamuning", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=37, stationName="Cubao", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=38, stationName="Santolan", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=39, stationName="Ortigas", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=40, stationName="Shaw Blvd.", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=41, stationName="Boni", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=42, stationName="Guadalupe", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=43, stationName="Buendia", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=44, stationName="Ayala", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=45, stationName="Magallanes", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")
        Station.objects.create(id=46, stationName="Taft", trainLine="MRT3", leftETA="2025-02-23T05:00:00Z", rightETA="2025-02-23T05:00:00Z", leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4", rightCCTV="https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4", isOperating=True, stationIMG="")


        HourlyDensity.objects.create(id=1, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T05:00:00Z")
        HourlyDensity.objects.create(id=2, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T06:00:00Z")
        HourlyDensity.objects.create(id=3, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T07:00:00Z")
        HourlyDensity.objects.create(id=4, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T08:00:00Z")
        HourlyDensity.objects.create(id=5, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T09:00:00Z")
        HourlyDensity.objects.create(id=6, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T10:00:00Z")
        HourlyDensity.objects.create(id=7, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T11:00:00Z")
        HourlyDensity.objects.create(id=8, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T12:00:00Z")
        HourlyDensity.objects.create(id=9, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T13:00:00Z")
        HourlyDensity.objects.create(id=10, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T14:00:00Z")
        HourlyDensity.objects.create(id=11, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T15:00:00Z")
        HourlyDensity.objects.create(id=12, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T16:00:00Z")
        HourlyDensity.objects.create(id=13, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T17:00:00Z")
        HourlyDensity.objects.create(id=14, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T18:00:00Z")
        HourlyDensity.objects.create(id=15, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T19:00:00Z")
        HourlyDensity.objects.create(id=16, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T20:00:00Z")
        HourlyDensity.objects.create(id=17, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T21:00:00Z")
        HourlyDensity.objects.create(id=18, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-23T22:00:00Z")


        DailyDensity.objects.create(id=1, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-24T00:00:00Z")
        DailyDensity.objects.create(id=2, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-25T00:00:00Z")
        DailyDensity.objects.create(id=3, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-26T00:00:00Z")
        DailyDensity.objects.create(id=4, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-27T00:00:00Z")
        DailyDensity.objects.create(id=5, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-02-28T00:00:00Z")
        DailyDensity.objects.create(id=6, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-03-01T00:00:00Z")
        DailyDensity.objects.create(id=7, station=self.selected, leftDensity=12.34, rightDensity=43.21, timestamp="2025-03-02T00:00:00Z")


    @patch("Station.views.check_database_status")
    def test_cannot_connect_to_server(self, mock_check_db_status):
        mock_check_db_status.return_value = False
        self.stations_url = reverse("station-list")
        res = self.client.get(self.stations_url)
        self.assertEqual(res.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(res.data, {"error": "Database is currently unavailable. Please try again later."})


    def test_get_all_stations(self):
        self.stations_url = reverse("station-list")
        res = self.client.get(self.stations_url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 46)

        station1 = res.data[0]
        self.assertEqual(station1["id"], 1)
        self.assertEqual(station1["stationName"], "Roosevelt")
        self.assertEqual(station1["trainLine"], "LRT1")
        self.assertEqual(station1["isOperating"], True)

        station2 = res.data[23]
        self.assertEqual(station2["id"], 24)
        self.assertEqual(station2["stationName"], "V. Mapa")
        self.assertEqual(station2["trainLine"], "LRT2")
        self.assertEqual(station2["isOperating"], True)

        station3 = res.data[40]
        self.assertEqual(station3["id"], 41)
        self.assertEqual(station3["stationName"], "Boni")
        self.assertEqual(station3["trainLine"], "MRT3")
        self.assertEqual(station3["isOperating"], True)


    def test_get_specific_station(self):
        self.station_urls = [reverse("station-details", args=[i+1]) for i in range(46)]

        res = self.client.get(self.station_urls[0])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["id"], 1)
        self.assertEqual(res.data["stationName"], "Roosevelt")
        self.assertEqual(res.data["trainLine"], "LRT1")
        self.assertEqual(res.data["leftETA"], "2025-02-23T05:00:00Z")
        self.assertEqual(res.data["rightETA"], "2025-02-23T05:00:00Z")
        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")
        self.assertEqual(res.data["rightCurrentDensity"], "Light")
        self.assertEqual(res.data["leftCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4")
        self.assertEqual(res.data["rightCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4")
        self.assertEqual(res.data["isOperating"], True)
        self.assertEqual(res.data["stationIMG"], "")

        res = self.client.get(self.station_urls[23])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["id"], 24)
        self.assertEqual(res.data["stationName"], "V. Mapa")
        self.assertEqual(res.data["trainLine"], "LRT2")
        self.assertEqual(res.data["leftETA"], "2025-02-23T05:00:00Z")
        self.assertEqual(res.data["rightETA"], "2025-02-23T05:00:00Z")
        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")
        self.assertEqual(res.data["rightCurrentDensity"], "Light")
        self.assertEqual(res.data["leftCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4")
        self.assertEqual(res.data["rightCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4")
        self.assertEqual(res.data["isOperating"], True)
        self.assertEqual(res.data["stationIMG"], "")

        res = self.client.get(self.station_urls[40])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["id"], 41)
        self.assertEqual(res.data["stationName"], "Boni")
        self.assertEqual(res.data["trainLine"], "MRT3")
        self.assertEqual(res.data["leftETA"], "2025-02-23T05:00:00Z")
        self.assertEqual(res.data["rightETA"], "2025-02-23T05:00:00Z")
        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")
        self.assertEqual(res.data["rightCurrentDensity"], "Light")
        self.assertEqual(res.data["leftCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4")
        self.assertEqual(res.data["rightCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4")
        self.assertEqual(res.data["isOperating"], True)
        self.assertEqual(res.data["stationIMG"], "")


    def test_selected_station_does_not_exist(self):
        self.non_existend_uri = reverse("station-details", args=[50])
        res = self.client.get(self.non_existend_uri)
        self.assertEqual(res.status_code, 404)

    
    def test_get_current_density(self):
        self.left_current_density = reverse("current-density", args=[12, "left"])
        res = self.client.get(self.left_current_density)
        self.assertEqual(res.status_code, 200)

        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")

        
        self.right_current_density = reverse("current-density", args=[34, "right"])
        res = self.client.get(self.right_current_density)
        self.assertEqual(res.status_code, 200)

        self.assertEqual(res.data["rightCurrentDensity"], "Light")


    def test_get_hourly_density(self):
        self.left_hourly_density = reverse("hourly-density", args=[2, "left"])
        res = self.client.get(self.left_hourly_density)
        self.assertEqual(res.status_code, 200)

        hour4 = res.data[3]
        self.assertEqual(hour4["id"], 4)
        self.assertEqual(hour4["station_id"], 2)
        self.assertEqual(hour4["leftDensity"], 12.34)

        hour13 = res.data[12]
        self.assertEqual(hour13["id"], 13)
        self.assertEqual(hour13["station_id"], 2)
        self.assertEqual(hour13["leftDensity"], 12.34)


        self.right_hourly_density = reverse("hourly-density", args=[2, "right"])
        res = self.client.get(self.right_hourly_density)
        self.assertEqual(res.status_code, 200)

        hour4 = res.data[3]
        self.assertEqual(hour4["id"], 4)
        self.assertEqual(hour4["station_id"], 2)
        self.assertEqual(hour4["rightDensity"], 43.21)

        hour13 = res.data[12]
        self.assertEqual(hour13["id"], 13)
        self.assertEqual(hour13["station_id"], 2)
        self.assertEqual(hour13["rightDensity"], 43.21)
    

    def test_get_daily_density(self):
        self.left_daily_density = reverse("daily-density", args=[2, "left"])
        res = self.client.get(self.left_daily_density)
        self.assertEqual(res.status_code, 200)

        day1 = res.data[0]
        self.assertEqual(day1["id"], 1)
        self.assertEqual(day1["station_id"], 2)
        self.assertEqual(day1["leftDensity"], 12.34)

        day7 = res.data[6]
        self.assertEqual(day7["id"], 7)
        self.assertEqual(day7["station_id"], 2)
        self.assertEqual(day7["leftDensity"], 12.34)


        self.right_daily_density = reverse("daily-density", args=[2, "right"])
        res = self.client.get(self.right_daily_density)
        self.assertEqual(res.status_code, 200)

        day1 = res.data[0]
        self.assertEqual(day1["id"], 1)
        self.assertEqual(day1["station_id"], 2)
        self.assertEqual(day1["rightDensity"], 43.21)

        day7 = res.data[6]
        self.assertEqual(day7["id"], 7)
        self.assertEqual(day7["station_id"], 2)
        self.assertEqual(day7["rightDensity"], 43.21)

    
    def test_connected_to_cctv(self):
        self.left_cctv = reverse("cctv-feed", args=[2, "left"])
        res = self.client.get(self.left_cctv)
        self.assertEqual(res.status_code, 200)

        self.assertEqual(res.data["leftCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_left_cctv_sample.mp4")

        
        self.right_cctv = reverse("cctv-feed", args=[2, "right"])
        res = self.client.get(self.right_cctv)
        self.assertEqual(res.status_code, 200)

        self.assertEqual(res.data["rightCCTV"], "https://res.cloudinary.com/stations-cctv/video/upload/station_right_cctv_sample.mp4")

    
    def test_no_cctvs_available(self):
        self.left_cctv = reverse("cctv-feed", args=[25, "left"])
        res = self.client.get(self.left_cctv)
        self.assertEqual(res.status_code, 404)

        self.right_cctv = reverse("cctv-feed", args=[25, "right"])
        res = self.client.get(self.right_cctv)
        self.assertEqual(res.status_code, 404)


    def test_cannot_fetch_current_densities(self):
        self.left_current_density = reverse("current-density", args=[25, "left"])
        res = self.client.get(self.left_current_density)
        self.assertEqual(res.status_code, 404)

        self.right_current_density = reverse("current-density", args=[25, "right"])
        res = self.client.get(self.right_current_density)
        self.assertEqual(res.status_code, 404)


    def test_cannot_fetch_hourly_densities(self):
        self.left_hourly_density = reverse("hourly-density", args=[25, "left"])
        res = self.client.get(self.left_hourly_density)
        self.assertEqual(res.status_code, 404)

        self.right_hourly_density = reverse("hourly-density", args=[25, "right"])
        res = self.client.get(self.right_hourly_density)
        self.assertEqual(res.status_code, 404)


    def test_cannot_fetch_daily_densities(self):
        self.left_daily_density = reverse("daily-density", args=[25, "left"])
        res = self.client.get(self.left_daily_density)
        self.assertEqual(res.status_code, 404)

        self.right_daily_density = reverse("daily-density", args=[25, "right"])
        res = self.client.get(self.right_daily_density)
        self.assertEqual(res.status_code, 404)
