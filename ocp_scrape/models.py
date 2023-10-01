from django.db import models
from django_celery_results.models import TaskResult
from django.contrib.auth.models import User

# Create your models here.
class GeneratedFiles(models.Model):
    file_field = models.FileField(upload_to='uploads/',default='')  # Adjust the upload path as needed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.file_field.name

class TaskResultInfo(models.Model):
    task_result = models.OneToOneField(TaskResult, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add your additional fields here
    extra_field = models.CharField(max_length=100)


