from django.shortcuts import render
from dosen.models import dosen

def index(request):
    
    dosens = dosen.objects.all()
    # dosens = dosen.objects.filter(prodi='Pendidikan Matematika')

    variabel = {
        'dosens' : dosens,
    }
    return render(request, 'dosen/index.html', variabel)

