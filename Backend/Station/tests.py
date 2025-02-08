from rest_framework.test import APITestCase
from django.urls import reverse
from unittest.mock import patch
from requests.exceptions import ConnectionError

class TestSetUp(APITestCase):
    def setUp(self):
        self.stations_url = reverse("station-list")
        self.station_urls = [reverse("station-detail", args=[i+1]) for i in range(46)]
        self.non_existend_uri = reverse("station-detail", args=[50])

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestViews(TestSetUp):
    @patch("requests.get")
    def test_cannot_connect_to_server(self):
        mock_get.side_effect = ConnectionError("Failed to connect")
        with self.assertRaises(ConnectionError):
            res = self.client.get(self.stations_url)
            print(res.status_code)


    def test_get_all_stations(self):
        res = self.client.get(self.stations_url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 46)

        station1 = res.data[0]
        self.assertEqual(station1["id"], 1)
        self.assertEqual(station1["stationName"], "Roosevelt")
        self.assertEqual(station1["trainLine"], "LRT1")
        self.assertEqual(station1["leftETA"], 10)
        self.assertEqual(station1["rightETA"], 10)
        self.assertEqual(station1["leftCurrentDensity"], "Heavy")
        self.assertEqual(station1["rightCurrentDensity"], "Light")
        self.assertEqual(station1["leftHistory"], "")
        self.assertEqual(station1["rightHistory"], "")
        self.assertEqual(station1["cctv"], "")
        self.assertEqual(station1["isOperating"], True)
        self.assertEqual(station1["stationIMG"], "")

        station2 = res.data[23]
        self.assertEqual(station2["id"], 24)
        self.assertEqual(station2["stationName"], "V. Mapa")
        self.assertEqual(station2["trainLine"], "LRT2")
        self.assertEqual(station2["leftETA"], 10)
        self.assertEqual(station2["rightETA"], 10)
        self.assertEqual(station2["leftCurrentDensity"], "Heavy")
        self.assertEqual(station2["rightCurrentDensity"], "Light")
        self.assertEqual(station2["leftHistory"], "")
        self.assertEqual(station2["rightHistory"], "")
        self.assertEqual(station2["cctv"], "")
        self.assertEqual(station2["isOperating"], True)
        self.assertEqual(station2["stationIMG"], "")

        station3 = res.data[40]
        self.assertEqual(station3["id"], 41)
        self.assertEqual(station3["stationName"], "Boni")
        self.assertEqual(station3["trainLine"], "MRT3")
        self.assertEqual(station3["leftETA"], 10)
        self.assertEqual(station3["rightETA"], 10)
        self.assertEqual(station3["leftCurrentDensity"], "Heavy")
        self.assertEqual(station3["rightCurrentDensity"], "Light")
        self.assertEqual(station3["leftHistory"], "")
        self.assertEqual(station3["rightHistory"], "")
        self.assertEqual(station3["cctv"], "")
        self.assertEqual(station3["isOperating"], True)
        self.assertEqual(station3["stationIMG"], "")

    def test_get_specific_station(self):
        res = self.client.get(self.station_urls[0])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["id"], 1)
        self.assertEqual(res.data["stationName"], "Roosevelt")
        self.assertEqual(res.data["trainLine"], "LRT1")
        self.assertEqual(res.data["leftETA"], 10)
        self.assertEqual(res.data["rightETA"], 10)
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
        self.assertEqual(res.data["rightETA"], 10)
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
        self.assertEqual(res.data["rightETA"], 10)
        self.assertEqual(res.data["leftCurrentDensity"], "Heavy")
        self.assertEqual(res.data["rightCurrentDensity"], "Light")
        self.assertEqual(res.data["leftHistory"], "")
        self.assertEqual(res.data["rightHistory"], "")
        self.assertEqual(res.data["cctv"], "")
        self.assertEqual(res.data["isOperating"], True)
        self.assertEqual(res.data["stationIMG"], "")

    def test_selected_station_does_not_exist(self):
        res = self.client.get(self.non_existend_uri)
        self.assertEqual(res.status_code, 404)
