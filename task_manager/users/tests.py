from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _


class UserTestCase(TestCase):
    fixtures = ['users.json']

    user_create = _('The user successfully created')
    user_update = _('The user successfully updated')
    no_rigths_for_user = _("You don't have the rights "
                           "to change another user.")
    user_delete = _("The user deleted! You need to log in again")
    no_delete_user = _("It is not possible to delete a user "
                       "because it is being used")

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.users_list = reverse('users')
        self.login = reverse('user_login')
        self.form_data = {'username': 'NewName',
                          'last_name': 'L',
                          'first_name': 'F',
                          'password1': 'NewPassword123',
                          'password2': 'NewPassword123'}

    def test_users_list(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        response_tasks = list(response.context['users'])
        self.assertQuerysetEqual(response_tasks,
                                 [self.user1, self.user2,
                                  self.user3])

    def test_create_user(self):
        create_user = reverse('user_create')
        """ GET """
        get_response = self.client.get(create_user)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(create_user,
                                         self.form_data, follow=True)
        self.assertRedirects(post_response, self.login)
        self.assertTrue(User.objects.get(id=4))
        # self.assertContains(post_response, UserTestCase.user_create)

    def test_update_user(self):
        self.client.force_login(self.user2)
        update_user = reverse('user_update', args=[2])
        """ GET """
        get_response = self.client.get(update_user)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(update_user,
                                         self.form_data, follow=True)
        self.assertRedirects(post_response, self.users_list)
        updated_user = User.objects.get(pk=2)
        self.assertEqual(updated_user.username, 'NewName')
        # self.assertContains(post_response, UserTestCase.user_update)

    def test_update_user_no_permission(self):
        self.client.force_login(self.user2)
        updated_user = reverse('user_update', args=[1])
        """ GET """
        get_response = self.client.get(updated_user,
                                       follow=True)
        self.assertRedirects(get_response, self.users_list)
        """ POST """
        post_response = self.client.post(updated_user,
                                         self.form_data, follow=True)
        user1 = User.objects.get(id=1)
        self.assertRedirects(post_response, self.users_list)
        self.assertFalse(user1.username == self.form_data['username'])

    def delete_user_no_permission(self):
        self.client.force_login(self.user3)
        del_user1 = reverse('delete', args=[1])
        """ GET """
        get_response = self.client.get(del_user1)
        self.assertRedirects(get_response, self.users_list)
        self.assertEqual(len(User.objects.all()), 3)
        """ POST """
        post_response = self.client.post(del_user1, follow=True)
        self.assertContains(post_response, UserTestCase.no_rigths_for_user)

    def delete_user_without_tasks(self):
        self.client.force_login(self.user3)
        del_user3 = reverse('delete', args=[3])
        """ GET """
        get_response = self.client.get(del_user3, follow=True)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(del_user3, follow=True)
        self.assertRedirects(post_response, self.users_list)
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(pk=3)
        # self.assertContains(post_response, UserTestCase.user_delete)

    def delete_user_with_tasks(self):
        self.client.force_login(self.user2)
        del_user2 = reverse('delete', args=[2])
        """ GET """
        get_response = self.client.get(del_user2, follow=True)
        self.assertRedirects(get_response, self.users_list)
        self.assertEqual(len(User.objects.all()), 3)
        """ POST """
        post_response = self.client.post(del_user2, follow=True)
        self.assertContains(post_response, UserTestCase.no_delete_user)
