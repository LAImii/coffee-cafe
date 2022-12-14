# Generated by Django 4.1 on 2022-08-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('gender', models.CharField(default='O', max_length=15)),
                ('status', models.CharField(choices=[('unapproved', 'Unapproved'), ('approved', 'Approved'), ('banned', 'Banned')], default='unapproved', max_length=15)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
