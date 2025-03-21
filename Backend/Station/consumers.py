import json
import asyncio
from datetime import timedelta
from django.utils import timezone
import random
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Station


class TrainETAConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.station_id = self.scope["url_route"]["kwargs"]["station_id"]  # Get station ID from URL
        self.platform_side = self.scope["url_route"]["kwargs"]["platform_side"] # Get platform side from URL
        self.group_name = f"station_{self.station_id}_{self.platform_side}"  # WebSocket group for station

        # Add connection to the station's group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        # Start sending ETA updates
        asyncio.create_task(self.send_eta_updates(self.platform_side))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


    async def send_eta_updates(self, platform_side):
        first_pass = True # Buffer

        while True:
            eta_data = await self.get_eta(self.station_id)  # Get ETA

            if eta_data:
                match platform_side:
                    case "left":
                        countdown = eta_data["leftETA"] - timezone.now()

                        if countdown <= timedelta(seconds=0):
                            if first_pass:
                                await self.update_leftETA(self.station_id)
                                countdown = eta_data["leftETA"] - timezone.now()
                                await self.channel_layer.group_send(
                                    self.group_name, {"type": "send_eta", "message": f"{countdown}"}
                                )
                            else:
                                await self.channel_layer.group_send(
                                    self.group_name, {"type": "send_eta", "message": "Train has arrived!"}
                                )

                                await self.update_leftETA(self.station_id)

                                await asyncio.sleep(random.randint(15, 60)) # Simulate train stopping for a while
                        else:
                            await self.channel_layer.group_send(
                                self.group_name, {"type": "send_eta", "message": f"{countdown}"}
                            )
                    
                    case "right":
                        countdown = eta_data["rightETA"] - timezone.now()

                        if countdown <= timedelta(seconds=0):
                            if first_pass:
                                await self.update_rightETA(self.station_id)
                                countdown = eta_data["leftETA"] - timezone.now()
                                await self.channel_layer.group_send(
                                    self.group_name, {"type": "send_eta", "message": f"{countdown}"}
                                )
                            else:
                                await self.channel_layer.group_send(
                                    self.group_name, {"type": "send_eta", "message": "Train has arrived!"}
                                )

                                await self.update_rightETA(self.station_id)

                                await asyncio.sleep(random.randint(15, 60)) # Simulate train stopping for a while
                        else:
                            await self.channel_layer.group_send(
                                self.group_name, {"type": "send_eta", "message": f"{countdown}"}
                            )

                    case _:
                        pass
            
            await asyncio.sleep(5)
            first_pass = False
            


    async def send_eta(self, event):
        await self.send(text_data=json.dumps(event["message"]))


    @sync_to_async
    def update_leftETA(self, station_id):
        station = Station.objects.get(id=station_id)

        if station:
            station.leftETA = (timezone.now() + timedelta(minutes=random.randint(3, 20))) # Simulate train ETA
            station.save()


    @sync_to_async
    def update_rightETA(self, station_id):
        station = Station.objects.get(id=station_id)

        if station:
            station.rightETA = (timezone.now() + timedelta(minutes=random.randint(3, 20))) # Simulate train ETA
            station.save()


    @sync_to_async
    def get_eta(self, station_id):
        station = Station.objects.get(id=station_id)
        if station:
            return {
                "station_id": station_id,
                "station_name": station.stationName,
                "leftETA": station.leftETA, 
                "rightETA": station.rightETA,
            }
        return None
