from django.test import TestCase
from Podcast.models import Podcast_info, channel, comment


class Podcast_info_TestCase(TestCase):
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



class channel_Testcase(TestCase):
    def setUp(self):
        channel.objects.create(
            channel_name = "Malek_zahra007",
            podcast_maker = "Malek zahra",
            subscribers = 5,
            podcast_num = 9,
        )

    def test_channel(self):
        channel_1 = channel.objects.get(
            channel_name = "Malek_zahra007"
        )
        self.assertEqual(channel_1.channel_name, "Malk_zahra007")
        self.assertEqual(channel_1.podcast_num, 8)



class comment_Testcase(TestCase):
    def setUp(self):
        comment.objects.create(
            text = "hello there"
            
        )

    def test_channel(self):
        comment_1 = comment.objects.get(
           text = "hello there"
        )
        self.assertEqual(comment_1.text, "hello there")