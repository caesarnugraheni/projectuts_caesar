from django.shortcuts import render
from materi.models import materi

def index(request):
    
    materis = materi.objects.all()
    # dosens = dosen.objects.filter(prodi='Pendidikan Matematika')

    variabel = {
        'materis' : materis,
    }
    return render(request, 'materi/index.html', variabel)

