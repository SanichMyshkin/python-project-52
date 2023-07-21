from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import ProtectedError

from .models import TaskUser
from task_manager.users.forms import UserForm


# Create your views here.

class UsersView(ListView):
    model = TaskUser
    context_object_name = 'users_list'
    template_name = 'users/index.html'


class UsersFormCreateView(CreateView):
    model = TaskUser
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_login')
    form_class = UserForm
    extra_context = {
        'header': _('Registry'),
        'button': _("button_cr")
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('User create successfully'))
        return response


class UsersUpdateView(UpdateView):
    model = TaskUser
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users')
    extra_context = {
        'header': _('Edit User'),
        'button': _('Update')
    }

    login_url = reverse_lazy('user_login')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, _('User update successfully'))
        return redirect(self.success_url)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = _('You cannot edit another user')
            url = reverse_lazy('users')
        else:
            message = _("You need to authenticated")
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)


class UsersDestroyView(DeleteView):
    model = TaskUser
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    login_url = reverse_lazy('user_login')

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = _("You don't have the rights "
                        "to change another user.")
            url = self.success_url
        else:
            message = _("You need to authenticated")
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, _("The user deleted! You need to log in again"))
            return redirect(self.success_url)
        except ProtectedError:
            messages.warning(self.request,
                             _("It is not possible to delete a user "
                               "because it is being used"))
            return redirect(success_url)
