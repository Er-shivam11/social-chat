# Generated by Django 4.2.5 on 2024-02-12 07:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="usertype",
            table="tbl_usertype",
        ),
    ]