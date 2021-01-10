from django.test import TestCase
from django.urls import reverse, resolve
from video.views import add_stand_up_video,add_motivation_video,add_sport_video


class Test_urls(TestCase):

    def test_add_stand_up_video(self):
        url = reverse('video:add_stand_up_video')
        self.assertEqual(resolve(url).func, add_stand_up_video)

    def test_video_motivation(self):
        url = reverse('video:add_motivation_video')
        self.assertEqual(resolve(url).func, add_motivation_video)

    def test_add_sport_video(self):
        url = reverse('video:add_sport_video')
        self.assertEqual(resolve(url).func, add_sport_video)