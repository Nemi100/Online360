from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Message

class MessagingTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='testpassword')
        self.receiver = User.objects.create_user(username='receiver', password='testpassword')

    def test_send_message(self):
        self.client.login(username='sender', password='testpassword')
        response = self.client.post(reverse('message_send'), {
            'receiver': self.receiver.id,
            'subject': 'Test Message',
            'content': 'This is a test message.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Message.objects.filter(subject='Test Message').exists())

    def test_receive_message(self):
        Message.objects.create(sender=self.sender, receiver=self.receiver, subject='Test Message', content='This is a test message.')
        self.client.login(username='receiver', password='testpassword')
        response = self.client.get(reverse('message_inbox'))
        self.assertContains(response, 'Test Message')
