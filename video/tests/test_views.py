from django.test import TestCase, Client
from django.urls import reverse
from video.views import video_motivation,sport_detail
from video.models import stand_up

class Test_views(TestCase):

    def test_video_stand_up(self):
        self.client = Client()
        response = self.client.get(reverse('video:stand_up_comedy'))
        self.assertEqual(response.status_code, 200)

    def test_add_stand_up_video(self):
        self.client = Client()
        response = self.client.get(reverse('video:add_stand_up_video'))
        self.assertEqual(response.status_code, 200)

    def test_video_motivation(self):
        self.client = Client()
        response = self.client.get(reverse('video:motivation'))
        self.assertEqual(response.status_code, 200)

    def test_video_Sport(self):
        self.client = Client()
        response = self.client.get(reverse('video:Sport'))
        self.assertEqual(response.status_code, 200)

    def test_add_sport_video(self):
        self.client = Client()
        response = self.client.get(reverse('video:add_sport_video'))
        self.assertEqual(response.status_code, 200)