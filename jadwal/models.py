from django.db import models

# Create your models here.

class jadwal(models.Model):
    hari = models.CharField(max_length=20)
    matapelajaran1 = models.CharField(max_length=200)
    matapelajaran2 = models.CharField(max_length=200)
    matapelajaran3 = models.CharField(max_length=200)
    matapelajaran4 = models.CharField(max_length=200)
    matapelajaran5 = models.CharField(max_length=200)

    def __str__(self):
        return self.hari

