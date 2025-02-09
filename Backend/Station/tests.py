from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch
from .models import Station

class TestViews(APITestCase):
    def setUp(self):
        Station.objects.create(id=1, stationName="Roosevelt", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=2, stationName="Balintawak", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=3, stationName="Monumento", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=4, stationName="5th Avenue", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=5, stationName="R. Papa", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=6, stationName="Abad Santos", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=7, stationName="Blumentritt", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=8, stationName="Tayuman", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=9, stationName="Bambang", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=10, stationName="Doroteo Jose", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=11, stationName="Carriedo", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=12, stationName="Central Terminal", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=13, stationName="United Nations", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=14, stationName="Pedro Gil", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=15, stationName="Quirino", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=16, stationName="Vito Cruz", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=17, stationName="Gil Puyat", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=18, stationName="Libertad", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=19, stationName="EDSA", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=20, stationName="Baclaran", trainLine="LRT1", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=21, stationName="Recto", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=22, stationName="Legarda", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=23, stationName="Pureza", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=24, stationName="V. Mapa", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=25, stationName="J. Ruiz", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=26, stationName="Gilmore", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=27, stationName="Betty Go-Belmonte", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=28, stationName="Araneta-Cubao", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=29, stationName="Anonas", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=30, stationName="Katipunan", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=31, stationName="Santolan", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=32, stationName="Marikina", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=33, stationName="Antipolo", trainLine="LRT2", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=34, stationName="North Avenue", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=35, stationName="Quezon Avenue", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=36, stationName="Kamuning", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=37, stationName="Cubao", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=38, stationName="Santolan", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=39, stationName="Ortigas", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=40, stationName="Shaw Blvd.", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=41, stationName="Boni", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=42, stationName="Guadalupe", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=43, stationName="Buendia", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=44, stationName="Ayala", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=45, stationName="Magallanes", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")
        Station.objects.create(id=46, stationName="Taft", trainLine="MRT3", leftETA=10, rightETA=3, leftCurrentDensity="Heavy", rightCurrentDensity="Light", leftHistory="", rightHistory="", cctv="", isOperating=True, stationIMG="")

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
        self.assertEqual(res.data["leftETA"], 10)
        self.assertEqual(res.data["rightETA"], 3)
        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")
        self.assertEqual(res.data["rightCurrentDensity"], "Light")
        self.assertEqual(res.data["leftHistory"], "")
        self.assertEqual(res.data["rightHistory"], "")
        self.assertEqual(res.data["cctv"], "")
        self.assertEqual(res.data["isOperating"], True)
        self.assertEqual(res.data["stationIMG"], "")


        res = self.client.get(self.station_urls[23])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["id"], 24)
        self.assertEqual(res.data["stationName"], "V. Mapa")
        self.assertEqual(res.data["trainLine"], "LRT2")
        self.assertEqual(res.data["leftETA"], 10)
        self.assertEqual(res.data["rightETA"], 3)
        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")
        self.assertEqual(res.data["rightCurrentDensity"], "Light")
        self.assertEqual(res.data["leftHistory"], "")
        self.assertEqual(res.data["rightHistory"], "")
        self.assertEqual(res.data["cctv"], "")
        self.assertEqual(res.data["isOperating"], True)
        self.assertEqual(res.data["stationIMG"], "")


        res = self.client.get(self.station_urls[40])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["id"], 41)
        self.assertEqual(res.data["stationName"], "Boni")
        self.assertEqual(res.data["trainLine"], "MRT3")
        self.assertEqual(res.data["leftETA"], 10)
        self.assertEqual(res.data["rightETA"], 3)
        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")
        self.assertEqual(res.data["rightCurrentDensity"], "Light")
        self.assertEqual(res.data["leftHistory"], "")
        self.assertEqual(res.data["rightHistory"], "")
        self.assertEqual(res.data["cctv"], "")
        self.assertEqual(res.data["isOperating"], True)
        self.assertEqual(res.data["stationIMG"], "")

    def test_selected_station_does_not_exist(self):
        self.non_existend_uri = reverse("station-details", args=[50])
        res = self.client.get(self.non_existend_uri)
        self.assertEqual(res.status_code, 404)
