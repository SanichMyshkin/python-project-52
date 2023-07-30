from django.utils.translation import gettext as _


class TransMessagesUsers:
    # Warning
    no_login = _("You need to authenticated")
    no_rules_edit = _('You cannot edit another user')
    no_rules_delete = _("You don't have the rights "
                        "to change another user.")
    is_already_use = _("It is not possible to delete a user "
                       "because it is being used")

    # Success
    update_success = _('User update successfully')
    create_success = _('User create successfully')
    delete_success = _("The user deleted! You need to log in again")
    login_success = _('You are successfully logged in')
    logout_success = _("You're logged out")

    # Alert


class TransMessagesTemplates:
    # Headers
    edit_user = _('Edit user')
    create_user = _('Create user')  # регистрация
    registry = _('Registry')
    delete_user = _('Delete user')
    sign_in_header = _('sign in header')

    status = _('Statuses')  # Статусы
    create_status = _('Create status')
    delete_status = _('Delete status')
    update_status = _('Update status')

    # Button
    update_button = _('update button')
    create_button = _('create button')
    delete_button = _('delete button')
    sign_in_button = _('sign in button')  # Войти


class TransMessagesStatus:
    # Warning
    no_rule_delete = _("This status is used, you can't delete it")

    # Success
    create_success = _('The status successfully created')
    update_success = _('The status successfully updated')
    delete_success = _('The status successfully deleted')


class NameForField:
    def __init__(self):
        self.name = _('Name')
        self.descr = _('Description')
        self.label = _('Label')
        self.status = _('Status')
        self.executor = _('Executor')
        self.date = _('Date')
        self.task = _('Task')
        self.author = _('Author')
        self.labels = _('Labels')


class TransMessagesTask:
    create_task = _('Create task')
    update_task = _('Update task')
    to_del_task = _('To delete task')
    no_delete_task = _("The task can only be deleted by its author")

    success_delete = _('The task successfully deleted')
    success_create = _('The task successfully created')
    success_update = _('The task successfully updated')


class TransMessagesLabels:
    create_label = _('Create label')
    update_label = _('Update label')
    to_del_label = _('To delete label')
    no_delete_label = _("This label is used, you can't delete it")

    success_create = _('The label successfully created')
    success_delete = _('The label successfully deleted')
    success_update = _('The label successfully updated')
