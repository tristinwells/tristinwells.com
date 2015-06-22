# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150602_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='posted',
            new_name='created_dttm',
        ),
    ]
