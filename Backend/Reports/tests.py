from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.db import connection
from unittest.mock import patch

from .models import Reports

# Create your tests here.

User = get_user_model()

class TestReportsView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="admin",
            password="password"
        )
        self.client.force_authenticate(user=self.user)

        Reports.objects.create(id=10, station="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:37:25Z")
        Reports.objects.create(id=9, station="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:37:08Z")
        Reports.objects.create(id=8, station="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:36:16Z")
        Reports.objects.create(id=7, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:35:48Z")
        Reports.objects.create(id=6, station="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:35:18Z")
        Reports.objects.create(id=5, station="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:34:43Z")
        Reports.objects.create(id=4, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:34:15Z")
        Reports.objects.create(id=3, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:33:52Z")
        Reports.objects.create(id=2, station="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:33:25Z")
        Reports.objects.create(id=1, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimeReported="2025-02-23T10:33:07Z")

        self.url = reverse('reports')

    # Successful reports retrieval
    def test_reports_retrieval(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data['count'], 10)
        self.assertIn('/api/reports/?limit=5&offset=5', data['next'])
        self.assertEqual(data['previous'], None)
        self.assertEqual(len(data['results']), 5)

        r1 = data['results'][0]
        self.assertEqual(r1['id'], 10)
        self.assertEqual(r1['station'], "LRT-2")
        self.assertEqual(r1['subject'], "Lorem Ipsum")
        # self.assertEqual(r1['datetimeReported'], "2025-02-23T10:37:25Z")

        r4 = data['results'][3]
        self.assertEqual(r4['id'], 7)
        self.assertEqual(r4['station'], "LRT-1")
        self.assertEqual(r4['subject'], "Lorem Ipsum")
        # self.assertEqual(r4['datetimeReported'], "2025-02-23T10:35:48Z")

    # requesting additional reports
    def test_additional_reports_retrieval(self):
        response = self.client.get(self.url, {"limit": 5, "offset": 5})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data['count'], 10)
        self.assertEqual(data['next'], None)
        self.assertIn('/api/reports/?limit=5', data['previous'])
        self.assertEqual(len(data['results']), 5)

        r6 = data['results'][0]
        self.assertEqual(r6['id'], 5)
        self.assertEqual(r6['station'], "MRT-3")
        self.assertEqual(r6['subject'], "Lorem Ipsum")
        # self.assertEqual(r6['datetimeReported'], "2025-02-23T10:34:43Z")

        r9 = data['results'][3]
        self.assertEqual(r9['id'], 2)
        self.assertEqual(r9['station'], "LRT-2")
        self.assertEqual(r9['subject'], "Lorem Ipsum")
        # self.assertEqual(r9['datetimeReported'], "2025-02-23T10:33:25Z")

    # No database connections
    @patch("Reports.views.check_database_status")
    def test_no_db_connection(self, mock_check_db_status):
        mock_check_db_status.return_value = False
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(res.data, {"error": "Database connection error"})

    # unauthenticated access
    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TestReportSubmissionView(APITestCase):
    def setUp(self):
        self.valid_data = {
            "subject": "Test Subject",
            "station": "Katipunan",
            "body": "ipsum lorem."
        }
        self.submission_url = reverse("report-submission")

    def test_create_report(self):
        response = self.client.post(
            self.submission_url, 
            self.valid_data, 
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reports.objects.count(), 11)
    
        entry = Reports.objects.last()
        if entry != None:
            self.assertEqual(entry.subject, self.valid_data["subject"])
            self.assertEqual(entry.station, self.valid_data["station"])
            self.assertEqual(entry.body, self.valid_data["body"])

    @patch("Reports.views.check_database_status")
    def test_no_db_connection(self, mock_check_db_status):
        mock_check_db_status.return_value = False
        res = self.client.post(
            self.submission_url, 
            self.valid_data, 
            format="json"
        )

        self.assertEqual(res.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(res.data, {"error": "Database is currently unavailable."})