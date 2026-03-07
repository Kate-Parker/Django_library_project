#views = python functions
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Livre
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# In your html template use dictionary cuz it doesn't read python variales.


@login_required(login_url="login/")
def liste_livres(request):
    all_the_books = Livre.objects.all()
    print("user:", request.user)
    return render(request,'blog/catalogue.html',{'livres': all_the_books})

#pour filtre mes different categorie de livre
def catalog_par_category(request,nom_categorie):
    livre_filtre = Livre.objects.filter(categorie__libelle=nom_categorie)

    return render(request, 'blog/catalogue.html', {
        'livres': livre_filtre,
        'categorie_actuelle': nom_categorie
    })

# manages the login
def login_Page(request):
    print("******Login page ")
    form = AuthenticationForm
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():  
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('liste_livres')
    return render(request,'blog/accounts/login.html', {'form': form})


def logout_session(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login') 
    else:
        return redirect('login')


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






