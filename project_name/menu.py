#-*- coding: utf-8 -*-

"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py:
    ADMIN_TOOLS_MENU = '{{project_name}}.menu.CustomMenu'
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu import items, Menu

class CustomMenu(Menu):
    """
    Custom Menu for {{project_name}} admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.AppList(
                _('Applications'),
                exclude=(
                    'django.contrib.*',
                ),
                children=[
#                    items.MenuItem(u'Страницы', reverse('admin:flatpages_flatpage_changelist')),
#                    items.MenuItem(u'Новости', reverse('admin:articles_news_changelist')),
#                    items.MenuItem(u'Файлы', reverse('fb_browse')),
                ],
            ),
            items.AppList(
                _('Administration'),
                exclude=(
                    'django.contrib.*',
                    'articles.*',
                    'chunks.*',
                ),
                children=[
                    items.MenuItem(u'users', reverse('admin:auth_user_changelist')),
                    items.MenuItem(u'groups', reverse('admin:auth_group_changelist')),
                ]
            ),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)
