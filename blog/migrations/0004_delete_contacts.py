# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150630_1712'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
