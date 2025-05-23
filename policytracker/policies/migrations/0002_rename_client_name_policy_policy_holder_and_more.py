# Generated by Django 5.1.7 on 2025-03-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policy',
            old_name='client_name',
            new_name='policy_holder',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='assigned_status',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='date_processed',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='id',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='policy_id',
        ),
        migrations.AddField(
            model_name='policy',
            name='branch',
            field=models.CharField(default='Head Office', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policy',
            name='payment_mode',
            field=models.CharField(default='Debit Order', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policy',
            name='policy_num',
            field=models.IntegerField(default='00000000000', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policy',
            name='policy_type',
            field=models.CharField(default='Adepa', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policy',
            name='status',
            field=models.CharField(default='approved', max_length=50),
            preserve_default=False,
        ),
    ]
