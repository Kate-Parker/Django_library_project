#views = python functions
from django.shortcuts import render,redirect
from .models import Livre
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# In your html template use dictionary cuz it doesn't read python variales.

def liste_livres(request):
    all_the_books = Livre.objects.all()
    return render(request,'blog/catalogue.html',{'livres': all_the_books})

#pour filtre mes different categorie de livre

def catalog_par_category(request,nom_categorie):
    
    livre_filtre = Livre.objects.filter(categorie__libelle=nom_categorie)

    return render(request, 'blog/catalogue.html', {
        'livres': livre_filtre,
        'categorie_actuelle': nom_categorie
    })

def login_Page(request):
    print("******Login page ")
    form = AuthenticationForm()
    if form.is_valid(): 
        user = form.get_user()
        login_Page(request, user)
        return redirect ('home')

    else:
        form = AuthenticationForm()
    context ={'form':form}
    return render(request,'blog/accounts/login.html',context)


#to create a registerpage
def register_Page(request):
    print("******Register page ")
    form = UserCreationForm
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    
    context ={'form':form}
    return render(request,'blog/accounts/register.html',context)






