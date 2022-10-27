from django.db import models

class Daily(models.Model):
    date = models.DateField(auto_now=True)
    study = models.TextField()
    research = models.TextField()
    hobby = models.TextField()
    others = models.TextField()
    future_work = models.TextField()
    evaluation = models.IntegerField(default=100)
    isOpen = models.BooleanField(default=True)

    def __str__(self):
        date_str = self.date.strftime('%Y/%m/%d')
        return date_str
