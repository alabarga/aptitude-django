# coding=utf-8

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem('Users', children=[
            ChildItem(model='auth.user'),
            ChildItem('User groups', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Extras', children=[
            ChildItem('View site', url='http://aptitude.biotektools.org'),
            ChildItem('Change password', url='admin:password_change'),
            ChildItem('APTITUDE', url='https://www.aptitude-net.com/', target_blank=True),

        ], align_right=True, icon='fa fa-cog'),
    )

    def ready(self):
        super(SuitConfig, self).ready()

        # DO NOT COPY FOLLOWING LINE
        # It is only to prevent updating last_login in DB for demo app
        self.prevent_user_last_login()

    def prevent_user_last_login(self):
        """
        Disconnect last login signal
        """
        from django.contrib.auth import user_logged_in
        from django.contrib.auth.models import update_last_login
        user_logged_in.disconnect(update_last_login)