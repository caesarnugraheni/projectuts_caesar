from django.contrib import admin
from materi.models import materi

# Register your models here.


# username : admin
# pw : admin123

class materiadmin(admin.ModelAdmin):
    list_display = ['nama_materi', 'link_video']
    search_fields = ['nama_materi']
    list_per_page = 5

admin.site.register(materi, materiadmin)