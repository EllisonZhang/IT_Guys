from django.test import TestCase
from WeGame.models import Review
from WeGame.models import Game
from WeGame.models import Video
from WeGame.models import Publisher
from accounts.models import CustomUser
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.template import loader

class AboutPageTests(TestCase):

    def test_about_contains_message(self):
        """
        Check if there is an about page and that it contains the particular message
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Welcome, our team is comprised of dedicated Glasgow University students and we would be delighted if you reach out to us with some feedback regarding our website. Thank you very much!')

    def test_about_using_template(self):
        """
        Check the template is used to render the about page
        """
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'wegame/about.html')


class NewsPageTests(TestCase):

    def test_news_page(self):
        """
        Check if the news page is functioning as intended
        """
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code,200)


class StaticImageTests(TestCase):
    def test_static_files(self):
        """
        Check if static media is used properly, not none if it fines a specific image
        """
        foundImage = finders.find('game1.jpg')
        self.assertIsNotNone(foundImage)


class SlugTest(TestCase):
    
    def test_slug(self):
        """
        check that slugify works correctly
        """
        game = Game(category='tests',name='world of warcraft',year_released='2019-10-25', game_content="moreTest")
        game.save()
        self.assertEqual(game.slug, 'world-of-warcraft')

class VideoModelTest(TestCase):

    def test_str_is_equal_to_name(self):
        """
        Method '_str_' should be equal to the field game_name
        """
        pub = Publisher(name='test', country='USA')
        gam = Game(category='testy',name='testname',publisher_name= pub, year_released='2000', game_content="moreTest")
        gname = Video(game_name =gam)
        self.assertEqual(str(gname), 'testname')

    def test_length_of_video_path(self):
        """
        Method to see if pthat length of video path limited to a 100
        """
        pub = Publisher(name='test', country='USA')
        gam = Game(category='testy',name='testname',publisher_name= pub, year_released='2000', game_content="moreTest")
        vid = Video(game_name = gam,video_path = 'abcdahHSAFOHDÓFIHDHGDLFHGdlkDLFKHGDLHFGDLHGfdlkhfgdlhfgdfgdifgdfgfgsd;fkdjglksdglkhfdglHKFGldhghgasa')
        self.assertEqual((len(vid.video_path) <= 100), True)


class IndexPageTests(TestCase):

    def test_news_page(self):
        """
        Check if the index page is functioning as intended
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)

class DatabaseTest(TestCase):

    def test_create_new_publisher(self):
        """
        Check if accurate number of Publishers within the Database
        """
        publ = Publisher(name='Sony', country='Korea')
        publ.save()
        publisher_data = Publisher.objects.all()
        self.assertEquals(len(publisher_data),1)
        sole = publisher_data[0]
        self.assertAlmostEquals(sole, publ)