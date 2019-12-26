from django.db import models


# Create your models here.
class Todo(models.Model):

    # todo = models.CharField(max_length=100, null=False, help_text="This field is required")
    todo = models.CharField(max_length=100, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo