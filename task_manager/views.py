from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.translations.trans import TransMessagesUsers, TransMessagesTemplates


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = TransMessagesUsers.login_success
    extra_context = {
        'header': TransMessagesTemplates.sign_in_header,
        'button': TransMessagesTemplates.sign_in_button,
    }


class UserLogoutView(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, TransMessagesUsers.logout_success)
        return super().dispatch(request, *args, **kwargs)
