from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user_accounts.models import Profile  # Import Profile model
from .models import Job, Category

class JobManagementTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='employer', password='testpassword')
        Profile.objects.create(user=self.user, is_employer=True)  # Create Profile with is_employer=True
        self.category = Category.objects.create(name='Frontend Developer')

    def test_create_job(self):
        self.client.login(username='employer', password='testpassword')
        response = self.client.post(reverse('job_create'), {
            'title': 'Build a website',
            'description': 'I need a frontend developer to build a website.',
            'budget': 1000,
            'due_date': '2023-12-31',
            'category': self.category.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Job.objects.filter(title='Build a website').exists())

    def test_update_job(self):
        job = Job.objects.create(employer=self.user, title='Build a website', description='I need a frontend developer to build a website.', budget=1000, due_date='2023-12-31', category=self.category)
        self.client.login(username='employer', password='testpassword')
        response = self.client.post(reverse('job_update', args=[job.id]), {
            'title': 'Update website',
            'description': 'I need a frontend developer to update a website.',
            'budget': 1500,
            'due_date': '2023-12-31',
            'category': self.category.id,
        })
        self.assertEqual(response.status_code, 302)
        job.refresh_from_db()
        self.assertEqual(job.title, 'Update website')

    def test_delete_job(self):
        job = Job.objects.create(employer=self.user, title='Build a website', description='I need a frontend developer to build a website.', budget=1000, due_date='2023-12-31', category=self.category)
        self.client.login(username='employer', password='testpassword')
        response = self.client.post(reverse('job_delete', args=[job.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Job.objects.filter(id=job.id).exists())
