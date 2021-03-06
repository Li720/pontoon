# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 21:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0087_auto_20170306_2113"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExternalResource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("url", models.URLField(blank=True, verbose_name=b"URL")),
            ],
        ),
        migrations.AlterModelOptions(
            name="project",
            options={"permissions": (("can_manage_project", "Can manage project"),)},
        ),
        migrations.RemoveField(model_name="locale", name="style_guide",),
        migrations.RemoveField(model_name="project", name="l10n_contact",),
        migrations.RemoveField(model_name="project", name="preview_url",),
        migrations.RemoveField(model_name="project", name="project_contact",),
        migrations.RemoveField(model_name="project", name="project_url",),
        migrations.AddField(
            model_name="project",
            name="admin_notes",
            field=models.TextField(
                blank=True,
                help_text=b"\n        Notes only visible in Administration\n    ",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                help_text=b"\n        L10n driver in charge of the project\n    ",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact_for",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="externalresource",
            name="locale",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.Locale",
            ),
        ),
        migrations.AddField(
            model_name="externalresource",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.Project",
            ),
        ),
    ]
