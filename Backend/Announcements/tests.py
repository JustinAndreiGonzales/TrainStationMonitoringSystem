from rest_framework.test import APITestCase
from  django.urls import reverse
from django.db import connection
from unittest.mock import patch
from rest_framework import status

from .models import Announcements

# Create your tests here.

class TestAnnouncementViews(APITestCase):

    def setUp(self):
        Announcements.objects.create(id=10, author="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:37:25Z")
        Announcements.objects.create(id=9, author="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:37:08Z")
        Announcements.objects.create(id=8, author="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:36:16Z")
        Announcements.objects.create(id=7, author="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:35:48Z")
        Announcements.objects.create(id=6, author="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:35:18Z")
        Announcements.objects.create(id=5, author="MRT-3", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:34:43Z")
        Announcements.objects.create(id=4, author="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:34:15Z")
        Announcements.objects.create(id=3, author="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:33:52Z")
        Announcements.objects.create(id=2, author="LRT-2", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:33:25Z")
        Announcements.objects.create(id=1, author="LRT-1", subject="Lorem Ipsum", body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ornare lacus arcu, ut congue justo consectetur convallis. Duis accumsan urna sed varius vulputate. Maecenas eget nulla vitae lectus ultricies venenatis. Duis sem mi, tincidunt sit amet aliquam sed, porttitor id diam. Vestibulum et justo quis arcu venenatis egestas. Ut hendrerit convallis ipsum sed vulputate. Nullam a semper nulla, et interdum justo. Proin vehicula erat vitae arcu rutrum euismod. Etiam pretium augue tristique consequat malesuada. Nam blandit, dolor eget vestibulum ultricies, nunc nibh feugiat ex, rhoncus scelerisque nisi neque vitae quam.", datetimePosted="2025-02-23T10:33:07Z")


    # No database connections
    @patch("Announcements.views.check_database_status")
    def test_announcements_no_db_connection(self, mock_check_db_status):
        mock_check_db_status.return_value = False
        self.announcement_url = reverse('announcements')
        res = self.client.get(self.announcement_url)
        self.assertEqual(res.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(res.data, {"error": "Database connection error"})
    
    # Successful announcement retrieval
    def test_announcement_retrieval(self):
        self.announcement_url = reverse('announcements')
        res = self.client.get(self.announcement_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data
        self.assertEqual(data['count'], 10)
        self.assertIn('/api/announcements/?limit=5&offset=5', data['next'])
        self.assertEqual(data['previous'], None)
        self.assertEqual(len(data['results']), 5)

        a1 = data['results'][0]
        self.assertEqual(a1['id'], 10)
        self.assertEqual(a1['author'], "LRT-2")
        self.assertEqual(a1['subject'], "Lorem Ipsum")

        a4 = data['results'][3]
        self.assertEqual(a4['id'], 7)
        self.assertEqual(a4['author'], "LRT-1")
        self.assertEqual(a4['subject'], "Lorem Ipsum")
        

    # requesting additional announcement
    def test_request_additional_reports(self):
        self.announcement_url = reverse('announcements')
        res = self.client.get(self.announcement_url, {'limit': 5, 'offset': 5}) 

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data
        self.assertEqual(data['count'], 10)
        self.assertEqual(data['next'], None)
        self.assertIn('/api/announcements/?limit=5', data['previous'])
        self.assertEqual(len(data['results']), 5)

        a6 = data['results'][0]
        self.assertEqual(a6['id'], 5)
        self.assertEqual(a6['author'], "MRT-3")
        self.assertEqual(a6['subject'], "Lorem Ipsum")

        a9 = data['results'][3]
        self.assertEqual(a9['id'], 2)
        self.assertEqual(a9['author'], "LRT-2")
        self.assertEqual(a9['subject'], "Lorem Ipsum")