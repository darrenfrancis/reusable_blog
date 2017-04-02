from django.test import TestCase
from .models import Post

class PostTests(TestCase):
    """
    Here we'll define the tests
    that'll run against our post model
    """

    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),
                         'My Latest Blog Pos')


# Create your tests here.
