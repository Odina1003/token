from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    user_id = models.IntegerField(primary_key=True)
 
    def __str__(self):
        return self.title
