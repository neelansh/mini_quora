# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 17:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_auto_20160311_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=1024)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='upvoted_by',
            field=models.ManyToManyField(blank=True, related_name='question_upvoted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answers',
            name='ques_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='questions.Question'),
        ),
    ]
