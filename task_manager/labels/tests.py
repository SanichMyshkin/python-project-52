from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User
from task_manager.labels.models import Label
from django.core.exceptions import ObjectDoesNotExist
from task_manager.translations.trans import TransMessagesLabels


class TestLabelsWithoutAuth(TestCase):

    def setUp(self):
        self.login = reverse('user_login')
        self.urls = [reverse('labels'),
                     reverse('create_lbl'),
                     reverse('delete_lbl', args=[1]),
                     reverse('update_lbl', args=[1])]

    def test_no_auth(self):
        for u in self.urls:
            response = self.client.get(u)
            self.assertRedirects(response, self.login)


class LabelsTestCase(TestCase):
    fixtures = ['labels.json', 'users.json',
                'tasks.json', 'statuses.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
        self.labels = reverse('labels')
        self.form_data = {'name': 'one more label'}

    def test_label_list(self):
        """ GET """
        response = self.client.get(self.labels)
        self.assertEqual(response.status_code, 200)
        labels = list(response.context['labels'])
        self.assertEqual(len(labels), 5)
        label1 = labels[0]
        self.assertEqual(label1.name, 'Срочно')

    def test_create_label(self):
        self.create_label = reverse('create_lbl')
        """ GET """
        get_response = self.client.get(self.create_label)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.create_label, self.form_data,
                                         follow=True)
        self.assertRedirects(post_response, self.labels)
        new_label = Label.objects.get(name=self.form_data['name'])
        self.assertEqual(new_label.id, 6)
        self.assertContains(post_response,
                            text=TransMessagesLabels.success_create)

    def test_update_label(self):
        self.update_label = reverse('update_lbl', args=[1])
        """ GET """
        get_response = self.client.get(self.update_label)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.update_label,
                                         self.form_data, follow=True)
        self.assertRedirects(post_response, self.labels)
        updated_label = Label.objects.get(pk=1)
        self.assertEqual(updated_label.name, 'one more label')
        self.assertContains(post_response,
                            text=TransMessagesLabels.success_update)

    def test_delete_not_used_label(self):
        self.delete_label = reverse('delete_lbl', args=[2])
        """ GET """
        get_response = self.client.get(self.delete_label, follow=True)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.delete_label, follow=True)
        self.assertRedirects(post_response, self.labels)
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(pk=2)
        self.assertContains(post_response,
                            text=TransMessagesLabels.success_delete)

    def test_delete_used_label(self):
        self.delete_label = reverse('delete_lbl', args=[5])
        """ GET """
        get_response = self.client.get(self.delete_label, follow=True)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(self.delete_label, follow=True)
        self.assertRedirects(post_response, self.labels)
        self.assertEqual(len(Label.objects.all()), 5)
