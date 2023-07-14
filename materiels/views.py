from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Materiel, Categorie, SousCategorie
from .forms import MaterielForm
from django.contrib import messages


class MaterielListView(View):
    def get(self, request):
        categories = Categorie.objects.all()
        sub_categories = SousCategorie.objects.all()
        form = MaterielForm()
        context = {
            'categories': categories,
            'sub_categories': sub_categories,
            'form': form
        }
        return render(request, 'materiels.html', context)

    def post(self, request):
        form = MaterielForm(request.POST)
        if form.is_valid():
            materiel_name = form.cleaned_data['materiel_name']
            materiel_description = form.cleaned_data['materiel_description']
            num_serie = form.cleaned_data['num_serie']
            materiel_description = form.cleaned_data['materiel_description']
            category_id = form.cleaned_data['categorie']
            sub_category_id = form.cleaned_data['sub_category']

            # Vérifier si une nouvelle catégorie a été spécifiée
            if category_id == 'new':
                nom_category = form.cleaned_data['new_category_name']
                description_category = form.cleaned_data['new_category_description']
                categorie = Categorie.objects.create(nomCategory=nom_category, description=description_category)
            else:
                categorie = Categorie.objects.get(idCategory=category_id)

            # Vérifier si une nouvelle sous-catégorie a été spécifiée
            if sub_category_id == 'new':
                nom_sous_category = form.cleaned_data['new_sub_category_name']
                description_sous_category = form.cleaned_data['new_sub_category_description']
                sous_categorie = SousCategorie.objects.create(nomSousCategory=nom_sous_category, description=description_sous_category, categorie=categorie)
            else:
                sous_categorie = SousCategorie.objects.get(idSousCategorie=sub_category_id)

            # Enregistrer le nouveau matériel
            Materiel.objects.create(nomMateriel=materiel_name, NumSerie=num_serie, description=materiel_description, sous_categorie=sous_categorie)
            messages.success(request, "Le matériel a été enregistré avec succès.")
            return redirect('materiel_list')

        # Si le formulaire n'est pas valide, réafficher le formulaire avec les erreurs
        categories = Categorie.objects.all()
        sub_categories = SousCategorie.objects.all()
        context = {
            'categories': categories,
            'sub_categories': sub_categories,
            'form': form
        }
        # Ajouter un message d'erreur à afficher
        messages.error(request, "Une erreur s'est produite lors de la soumission du formulaire.")
        return render(request, 'materiels.html', context)
