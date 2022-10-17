from django.db import models

# Create your models here.

class materi(models.Model):
    nama_materi = models.CharField(max_length=200)
    link_video = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.nama_materi

