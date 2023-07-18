from django.shortcuts import render, redirect
from .models import Panne
from materiels.models import Materiel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# def pannes_page(request):
#     # Il faudra les materiels, les sauvegarder dans la database des pannes et ensuite on affiche
#     pannes = Panne.objects.all()
#     return render(request, 'panne.html', {'pannes': pannes})

@login_required
def pannes_page(request):
    # Récupérer tous les matériels en panne
    materiels_en_panne = Materiel.objects.filter(en_panne=True)

    # Pour chaque matériel en panne, vérifier s'il y a déjà une panne existante pour ce matériel.
    # Si ce n'est pas le cas, créer une nouvelle panne.
    for materiel in materiels_en_panne:
        if not Panne.objects.filter(materiel=materiel, resolue=False).exists():
            Panne.objects.create(materiel=materiel, description="Description de la panne...")

    # Récupérer toutes les pannes non résolues pour les afficher
    pannes = Panne.objects.filter(resolue=False)

    return render(request, 'panne.html', {'pannes': pannes})

@require_POST
def toggle_panne(request, panne_id):
    panne = Panne.objects.get(id=panne_id)
    panne.resolue = True
    panne.materiel.en_panne = False  # Pour mettre à jour l'état du matériel correspondant
    panne.materiel.save()  # Sauvegarder les modifications du matériel
    panne.save()  # Sauvegarder les modifications de la panne
    return redirect('pannes')
