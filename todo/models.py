from django.db import models

#add user field to model

class Todo(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    time_created = models.DateTimeField()

    def __str__(self):
        return self.title
