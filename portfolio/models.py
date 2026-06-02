from django.db import models

class Project(models.Model):
    Title=models.CharField(max_length=100)
    description=models.TextField()
    progress=models.IntegerField(default=0)
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title