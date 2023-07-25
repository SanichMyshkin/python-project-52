from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.core.exceptions import ObjectDoesNotExist
from task_manager.translations.trans import TransMessagesStatus


class TestStatusesWithoutAuth(TestCase):

    def setUp(self):
        self.login = reverse('user_login')
        self.urls = [reverse('statuses'),
                     reverse('status_create'),
                     reverse('status_delete', args=[1]),
                     reverse('status_update', args=[1])]

    def test_no_auth(self):
        for u in self.urls:
            response = self.client.get(u)
            self.assertRedirects(response, self.login)


class StatusesTestCase(TestCase):
    fixtures = ['statuses.json', 'users.json']

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.client.force_login(self.user)
        self.statuses = reverse('statuses')
        self.form_data = {'name': 'new status'}

    def test_status_list(self):
        self.s1 = Status.objects.get(pk=1)
        self.s2 = Status.objects.get(pk=5)
        self.s3 = Status.objects.get(pk=6)
        """ GET """
        response = self.client.get(self.statuses)
        self.assertEqual(response.status_code, 200)
        response_tasks = list(response.context['statuses'])
        self.assertQuerysetEqual(response_tasks,
                                 [self.s1, self.s2,
                                  self.s3])

    def test_create_status(self):
        self.create_status = reverse('status_create')
        """ GET """
        get_response = self.client.get(self.create_status)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.create_status,
                                         self.form_data, follow=True)
        self.assertRedirects(post_response, self.statuses)
        self.assertTrue(Status.objects.get(id=7))
        self.assertContains(
            post_response, text=TransMessagesStatus.create_success)

    def test_update_status(self):
        self.update_status = reverse('status_update', args=[1])
        """ GET """
        get_response = self.client.get(self.update_status)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.update_status,
                                         self.form_data, follow=True)
        self.assertRedirects(post_response, self.statuses)
        self.status = Status.objects.get(pk=1)
        self.assertEqual(self.status.name, self.form_data['name'])
        self.assertContains(
            post_response, text=TransMessagesStatus.update_success)

    def test_delete_used_status(self):
        self.delete_status = reverse('status_delete', args=[1])
        """ GET """
        get_response = self.client.get(self.delete_status)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.delete_status)
        self.assertRedirects(post_response, self.statuses)
        self.assertEqual(len(Status.objects.all()), 2)

    def test_delete_not_used_status(self):
        self.delete_status = reverse('status_delete', args=[5])
        """ GET """
        get_response = self.client.get(self.delete_status)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.delete_status, follow=True)
        self.assertRedirects(post_response, self.statuses)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=5)
        self.assertContains(
            post_response, text=TransMessagesStatus.delete_success)
