# user_accounts/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_profile(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile_create'), {
            'first_name': 'Test',
            'last_name': 'User',
            'bio': 'This is a test user.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_update_profile(self):
        Profile.objects.create(user=self.user, first_name='Test', last_name='User', bio='This is a test user.')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile_update'), {
            'first_name': 'Updated',
            'last_name': 'User',
            'bio': 'This is an updated test user.',
        })
        self.assertEqual(response.status_code, 302)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.first_name, 'Updated')

    def test_delete_profile(self):
        Profile.objects.create(user=self.user, first_name='Test', last_name='User', bio='This is a test user.')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile_delete'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
