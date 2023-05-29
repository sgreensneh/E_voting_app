# Generated by Django 4.2.1 on 2023-05-29 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_voting_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voter',
            options={},
        ),
        migrations.AlterModelManagers(
            name='voter',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='voter',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='email',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='password',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='username',
        ),
        migrations.AlterField(
            model_name='party',
            name='acronym',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='party',
            name='flag_bearer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='party',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='poll',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_voting_app.voter'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='voter',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
