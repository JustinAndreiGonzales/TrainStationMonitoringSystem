from rest_framework.test import APITestCase
from rest_framework import status
from  django.urls import reverse
from unittest.mock import patch

# Create your tests here.

class TestAnnouncementViews(APITestCase):

    def setUp(self):
        # TODO: add db data
        ...

    # TODO: No database connections
    # @patch("Reports.views.")
    
    # Successful announcement retrieval
    def test_announcement_retrieval(self):
        self.announcement_url = reverse('announcements')
        res = self.client.get(self.announcement_url) 

        self.assertEqual(res.status_code, 200)
        ...

    # requesting additional announcement
    def test_request_additional_reports(self):
        self.announcement_url = reverse('announcements')
        res = self.client.get(self.announcement_url, {'limit': 3, 'offset': 3}) 

        self.assertEqual(res.status_code, 200)
        ...

