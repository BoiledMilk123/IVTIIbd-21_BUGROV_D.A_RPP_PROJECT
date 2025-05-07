from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from visits.models import Visit, Client as ClientModel

class VisitsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client_obj = ClientModel.objects.create(name='Test Client', contact_info='test@example.com')
        self.visit = Visit.objects.create(
            client=self.client_obj,
            date='2025-05-06',
            time='10:00:00',
            employee=self.user,
            status='planned'
        )

    def test_visits_list_page(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('visits:visit_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Client')

    def test_login_page(self):
        response = self.client.get(reverse('visits:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'visits/login.html')

    def test_unauthenticated_access(self):
        response = self.client.get(reverse('visits:visit_list'))
        self.assertRedirects(response, '/visits/login/?next=/visits/')
