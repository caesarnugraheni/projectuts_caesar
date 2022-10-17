from django.contrib import admin
from jadwal.models import jadwal

# Register your models here.


# username : admin
# pw : admin123

class jadwaladmin(admin.ModelAdmin):
    list_display = ['hari', 'matapelajaran1', 'matapelajaran2', 'matapelajaran3', 'matapelajaran4', 'matapelajaran5']
    search_fields = ['hari']
    list_per_page = 5

admin.site.register(jadwal, jadwaladmin)