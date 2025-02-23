from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.db import connection

from .models import Reports

# Create your tests here.

User = get_user_model()

class TestReportsView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="",
            password=""
        )
        cls.token = Token.objects.create(user=cls.user)

        Reports.objects.create(id=10, station="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:37:25Z")
        Reports.objects.create(id=9, station="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:37:08Z")
        Reports.objects.create(id=8, station="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:36:16Z")
        Reports.objects.create(id=7, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:35:48Z")
        Reports.objects.create(id=6, station="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:35:18Z")
        Reports.objects.create(id=5, station="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:34:43Z")
        Reports.objects.create(id=4, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:34:15Z")
        Reports.objects.create(id=3, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:33:52Z")
        Reports.objects.create(id=2, station="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:33:25Z")
        Reports.objects.create(id=1, station="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:33:07Z")

        cls.url = reverse('reports')

    # Successful reports retrieval
    def test_reports_retrieval(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data['count'], 10)
        self.assertContains(data['next'], '/api/reports/?limit=5&offset=10')
        self.assertEqual(data['previous'], None)
        self.assertEqual(len(data['results']), 5)

        r1 = data['results'][0]
        self.assertEqual(r1['id'], 10)
        self.assertEqual(r1['station'], "LRT-2")
        self.assertEqual(r1['subject'], "Lorem Ipsum")
        self.assertEqual(r1['datetimePosted'], "2025-02-23T10:37:25Z")

        r4 = data['results'][3]
        self.assertEqual(r4['id'], 7)
        self.assertEqual(r4['station'], "LRT-1")
        self.assertEqual(r4['subject'], "Lorem Ipsum")
        self.assertEqual(r4['datetimePosted'], "2025-02-23T10:35:48Z")


    # requesting additional reports
    def test_additional_reports_retrieval(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        response = self.client.get(self.url, {"limit": 5, "offset": 5})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data['count'], 10)
        self.assertEqual(data['next'], None)
        self.assertContains(data['previous'], '/api/reports/?limit=5')
        self.assertEqual(len(data['results']), 5)

        r6 = data['results']
        self.assertEqual(r6['id'], 5)
        self.assertEqual(r6['station'], "MRT-3")
        self.assertEqual(r6['subject'], "Lorem Ipsum")
        self.assertEqual(r6['datetimePosted'], "2025-02-23T10:34:43Z")

        r9 = data['results'][3]
        self.assertEqual(r9['id'], 2)
        self.assertEqual(r9['station'], "LRT-2")
        self.assertEqual(r9['subject'], "Lorem Ipsum")
        self.assertEqual(r9['datetimePosted'], "2025-02-23T10:33:25Z")

    # No database connections
    def test_no_db_connection(self):
        connection.close()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    # unauthenticated access
    def test_unauthenticated_access(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
