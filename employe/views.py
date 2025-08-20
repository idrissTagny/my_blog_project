from django.shortcuts import render, redirect, get_object_or_404
from .models import Employe
from .forms import employeForms
# Create your views here.

def list_employe(request):
    employe = Employe.objects.all()
    return render(request, 'employe/list.html', {'employes':employe} )


def ajouter_employer(request):
    form = employeForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_employe')
    return render(request, 'employe/formulaire.html', {'form': form}) 


def modifier_employer(request, id):
    employe = get_object_or_404(Employe, id=id)   # employe = instance unique
    form = employeForms(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('list_employe')
    return render(request, 'employe/formulaire.html', {'form': form})

def supprimer_employer(request, id):
    employe = get_object_or_404(Employe, id=id)   # employe = instance unique
    if request.method == "POST":
        employe.delete()
        return redirect('list_employe')
    return render(request, 'employe/confirSuppression.html', {'employe': employe})   
