# Generated by Django 4.1.13 on 2024-09-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stregsystem', '0018_member_signup_due_paid_alter_mobilepayment_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('html', models.CharField(blank=True, default='', max_length=50, verbose_name='HTML filename')),
                ('css', models.CharField(blank=True, default='', max_length=50, verbose_name='CSS filename')),
                ('js', models.CharField(blank=True, default='', max_length=50, verbose_name='JS filename')),
                ('begin_month', models.PositiveSmallIntegerField(verbose_name='Begin month')),
                ('begin_day', models.PositiveSmallIntegerField(default=1, verbose_name='Begin day')),
                ('end_month', models.PositiveSmallIntegerField(verbose_name='End month')),
                ('end_day', models.PositiveSmallIntegerField(default=31, verbose_name='End day')),
                ('override', models.CharField(choices=[('N', 'None'), ('S', 'Force show'), ('H', 'Force hide')], default='N', max_length=1, verbose_name='Override')),
            ],
            options={
                'ordering': ['begin_month', 'begin_day'],
            },
        ),
    ]
