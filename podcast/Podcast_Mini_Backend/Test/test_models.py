from django.test import TestCase
from Podcast.models import Podcast_info


class Podcast_infoTestCase(TestCase):
    def setUp(self):
        Podcast_info.objects.create(
            Title="Top Programming Languages at FAANG",
            Description="testing",
            podcast="/home/ghassanmohder/Music/go.mp3",
            Thumbnail="/home/ghassanmohder/Pictures/Glacier-Mountain.jpg",
            podcasted_by="ghassan_mohder",
            is_viewed=True,
            is_liked=False
        )

    def test_podcast_info_podcast_exstence(self):
        podcast_1 = Podcast_info.objects.get(
            podcast = "/home/ghassanmohder/Music/go.mp3"
            )
        self.assertEqual(podcast_1.podcast, "/home/ghassanmohder/Music/go.mp3")
