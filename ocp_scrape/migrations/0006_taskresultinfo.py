# Generated by Django 4.2.1 on 2023-05-31 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_celery_results', '0011_taskresult_periodic_task_name'),
        ('ocp_scrape', '0005_delete_extendedtaskresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResultInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_field', models.CharField(max_length=100)),
                ('task_result', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_celery_results.taskresult')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]