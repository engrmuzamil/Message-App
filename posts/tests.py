from django.test import TestCase
from .models import Post
class postModeltest(TestCase):
    def setUp(self):
        Post.objects.create(message="Message")

    def test_msg(self):
        post = Post.objects.get(id = 1)
        objectname = f'{post.message}'
        self.assertEqual(objectname,"Message")

from .views import homeView
from django.urls import reverse
class homeviewTest(TestCase):
    def setUp(self):
        Post.objects.create(message="message")

    def test_url_exists(self):
        responseRecv  = self.client.get('/')
        self.assertEqual(responseRecv.status_code, 200)
    
    def test_url_name(self):
        responseRecv = self.client.get(reverse('home'))
        self.assertEqual(responseRecv.status_code, 200)
    
    def test_View_Uses_Correct_Template(self):
        reponseRecv= self.client.get(reverse('home'))
        self.assertEqual(reponseRecv.status_code, 200)
        self.assertTemplateUsed(reponseRecv, 'index.html')

    
