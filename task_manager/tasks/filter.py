from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from .models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User
from django.utils.translation import gettext as _
from django import forms


class TaskFilter(FilterSet):

    def my_task_filter(self, queryset, name, value):
        if value:
            author = getattr(self.request, 'user', None)
            queryset = queryset.filter(author=author)
        return queryset

    labels = ModelChoiceFilter(queryset=Label.objects.all(),
                               label=_('Label'),
                               widget=forms.Select(
                                   attrs={'name': 'label',
                                          'class': 'custom-select d-block',
                                          'title_id': 'id_label'}))

    status = ModelChoiceFilter(queryset=Status.objects.all(),
                               label=_('Status'),
                               widget=forms.Select(
                                   attrs={'name': 'status',
                                          'class': 'custom-select d-block',
                                          'title_id': 'id_status'}))

    executor = ModelChoiceFilter(queryset=User.objects.all(),
                                 label=_('Executor'),
                                 widget=forms.Select(
                                     attrs={'name': 'executor',
                                            'class': 'custom-select d-block',
                                            'title_id': 'id_executor'}))

    author = ModelChoiceFilter(queryset=User.objects.all(),
                               label=_('Author'),
                               widget=forms.Select(
                                   attrs={'name': 'author',
                                          'class': 'custom-select d-block',
                                          'title_id': 'id_author'}))

    self_task = BooleanFilter(label=_('My tasks only'),
                              widget=forms.widgets.CheckboxInput(
                                  attrs={'name': 'self_task',
                                         'title_id': 'id_self_task'}),
                              method='my_task_filter',
                              )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'author', 'self_task']
