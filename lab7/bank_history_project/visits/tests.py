from django.test import TestCase, Client as DjangoTestClient
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from visits.models import Visit, Client, Employee, Branch
from django.utils import timezone
import datetime


class VisitsTests(TestCase):
    def setUp(self):
        self.test_client = DjangoTestClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.employee = Employee.objects.create(full_name='Test Employee', position='Manager')
        self.client_obj = Client.objects.create(full_name='Test Client', email='test@example.com')
        self.branch = Branch.objects.create(name='Test Branch', address='123 Test St')
        view_perm = Permission.objects.get(codename='view_visit')
        self.user.user_permissions.add(view_perm)
        self.visit = Visit.objects.create(
            client=self.client_obj,
            visit_date=timezone.make_aware(datetime.datetime(2025, 5, 6, 12, 0, 0)),
            visit_type='consultation',
            employee=self.employee,
            branch=self.branch
        )

    def test_visits_list_page(self):
        self.test_client.login(username='testuser', password='testpass123')
        response = self.test_client.get(reverse('visits:visit_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Client')

    def test_login_page(self):
        response = self.test_client.get(reverse('visits:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'visits/login.html')

    def test_unauthenticated_access(self):
        response = self.test_client.get(reverse('visits:visit_list'))
        self.assertRedirects(response, '/visits/login/?next=/visits/')
