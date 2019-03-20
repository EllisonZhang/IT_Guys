from django.test import TestCase
from WeGame.models import Review
from WeGame.models import Game
from WeGame.models import Publisher
from accounts.models import CustomUser
from django.core.urlresolvers import reverse

class ReviewMethodTests(TestCase):
    def test_ensure_likes_are_positive(self):
        """
        ensure_likes_are_positive should results True for reviews
        where likes are zero or positive
        """
        pub = Publisher(name='test', country='USA')
        gam = Game(category='testy',name='testname',publisher_name= pub, year_released='2000', game_content="moreTest")
        userCustom = CustomUser(age='24')
        rev = Review(number_likes=-1,number_dislikes=0,comment_text="test",creation_date=2019-10-25, game_reviewed= gam, user= userCustom)
        self.assertEqual((rev.number_likes >=0), True)


    def test_ensure_dislikes_are_positive(self):
        """
        ensure_dislikes_are_positive should results True for reviews
        where dislikes are zero or positive
        """
        pub = Publisher(name='test', country='USA')
        gam = Game(category='testy',name='testname',publisher_name= pub, year_released='2000', game_content="moreTest")
        userCustom = CustomUser(age='24')
        rev = Review(number_likes=0,number_dislikes=-1,comment_text="test",creation_date=2019-10-25, game_reviewed= gam, user= userCustom)
        self.assertEqual((rev.number_dislikes >=0), True)


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