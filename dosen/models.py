from django.db import models

# Create your models here.

class dosen(models.Model):
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=150)
    alamat = models.CharField(max_length=250)

    def __str__(self):
        return self.nama

