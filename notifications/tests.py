from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Notification

class NotificationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='testpassword')

    def test_notification_display(self):
        Notification.objects.create(user=self.user, message='Test Notification')
        self.client.login(username='user', password='testpassword')
        response = self.client.get(reverse('notifications'))
        self.assertContains(response, 'Test Notification')
