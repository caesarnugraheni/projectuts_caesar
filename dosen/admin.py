from django.contrib import admin
from dosen.models import dosen

# Register your models here.


# username : admin
# pw : admin123

class DosenAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nip', 'ttl', 'email', 'fakultas', 'prodi', 'alamat']
    search_fields = ['nama', 'fakultas', 'prodi']
    list_per_page = 5

admin.site.register(dosen, DosenAdmin)