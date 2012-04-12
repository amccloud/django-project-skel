#-*- coding: UTF-8 -*-
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.v2 import MediaFileContent

 # Set of extensions
Page.register_extensions('datepublisher',)

Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
            ('main', _('Main content area')),
        ),
    })

Page.create_content_type(RichTextContent)
Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
    ('lightbox', _('lightbox')),
))
