from django.shortcuts import render, redirect

from employe.models import Employe

from django.contrib import messages

from django.core.paginator import Paginator

from . import forms


# Create your views here.
def employes(request):
    if request.method == 'POST':
        formEmpData = forms.EmployeForm(request.POST)
        if formEmpData.is_valid():
            print('Valid')
            # employe_name = formEmpData.cleaned_data['nom']
            # print("Employee Name:", employe_name)
            employee = Employe(
                nom=formEmpData.cleaned_data['nom'],
                prenom=formEmpData.cleaned_data['prenom'],
                poste=formEmpData.cleaned_data['poste'],
                dateEmbauche=formEmpData.cleaned_data['dateEmbauche'],
                email=formEmpData.cleaned_data['email']
            )
            employee.save()
            messages.success(request, 'Un nouveau employé est ajouté.')
            return redirect('employes')
        

    formEmp = forms.EmployeForm()
    # employes = Employe.objects.all()   
    employes = Employe.objects.order_by('idEmploye').all()

    page = Paginator(employes, 1)
    page_liste = request.GET.get('page')
    page = page.get_page(page_liste)  
    return render(request, 'index.html', {'page': page, 'formEmp': formEmp}) 

    # return render(request, 'index.html', {'employes': employes, 'formEmp': formEmp}) 



def delete_employee(request, employee_id):
    employee = Employe.objects.get(idEmploye=employee_id)
    employee.delete()
    messages.success(request, "L'employé " + employee.nom +" a été supprimé")
    return redirect('employes')

def edit_employee(request, employee_id):
    employee = Employe.objects.get(idEmploye=employee_id)
    print(employee.nom)

    if request.method == 'POST':
        form = forms.EmployeForm(request.POST)
        if form.is_valid():
            # Update the employee details
            employee.nom = form.cleaned_data['nom']
            employee.prenom = form.cleaned_data['prenom']
            employee.dateEmbauche = form.cleaned_data['dateEmbauche']
            employee.poste = form.cleaned_data['poste']
            employee.email = form.cleaned_data['email']
            employee.save()
            print("Le nom modifie ", form.cleaned_data['nom'])
            messages.success(request, "Les infos de l'employé " + employee.nom +" sont modifiés")
    
    return redirect('employes')