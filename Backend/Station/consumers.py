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
        self.active_tasks = {}

        # Add connection to the station's group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        # Start sending ETA updates
        if self.group_name not in self.active_tasks:
            self.active_tasks[self.group_name] = asyncio.create_task(self.send_eta_updates(self.platform_side))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

        if self.group_name in self.active_tasks:
            self.active_tasks[self.group_name].cancel()
            del self.active_tasks[self.group_name]


    async def send_eta_updates(self, platform_side):
        first_pass = True # Buffer

        while True:
            eta_data = await self.get_eta(self.station_id)  # Get ETA

            if eta_data:
                match platform_side:
                    case "left":
                        if eta_data["leftETA"]:
                            countdown = eta_data["leftETA"] - timezone.now()
                            min_left = int(countdown.total_seconds() // 60)

                            if min_left <= 0:
                                if first_pass:
                                    await self.update_leftETA(self.station_id)
                                else:
                                    await self.channel_layer.group_send(
                                        self.group_name, {"type": "send_eta", "message": f"{min_left}"}
                                    )

                                    await self.update_leftETA(self.station_id)

                                    await asyncio.sleep(random.randint(25, 60)) # Simulate train stopping for a while
                            else:
                                await self.channel_layer.group_send(
                                    self.group_name, {"type": "send_eta", "message": f"{min_left}"}
                                )
                        else:
                            await self.channel_layer.group_send(
                                self.group_name, {"type": "send_eta", "message": "Service is currently unavailable."}
                            )
                    
                    case "right":
                        if eta_data["rightETA"]:
                            countdown = eta_data["rightETA"] - timezone.now()
                            min_left = int(countdown.total_seconds() // 60)

                            if min_left <= 0:
                                if first_pass:
                                    await self.update_rightETA(self.station_id)
                                else:
                                    await self.channel_layer.group_send(
                                        self.group_name, {"type": "send_eta", "message": f"{min_left}"}
                                    )

                                    await self.update_rightETA(self.station_id)

                                    await asyncio.sleep(random.randint(25, 60)) # Simulate train stopping for a while
                            else:
                                await self.channel_layer.group_send(
                                    self.group_name, {"type": "send_eta", "message": f"{min_left}"}
                                )
                        else:
                            await self.channel_layer.group_send(
                                self.group_name, {"type": "send_eta", "message": "Service is currently unavailable."}
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
            station.leftETA = (timezone.now() + timedelta(minutes=random.randint(5, 20))) # Simulate train ETA
            station.save()


    @sync_to_async
    def update_rightETA(self, station_id):
        station = Station.objects.get(id=station_id)

        if station:
            station.rightETA = (timezone.now() + timedelta(minutes=random.randint(5, 20))) # Simulate train ETA
            station.save()


    @sync_to_async
    def get_eta(self, station_id):
        station = Station.objects.get(id=station_id)
        if station:
            return {
                "leftETA": station.leftETA, 
                "rightETA": station.rightETA,
            }
        return None