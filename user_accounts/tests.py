from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserSignupLoginTest(TestCase):
    def test_register_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_user(self):
        User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
