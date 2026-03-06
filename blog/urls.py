from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_Page, name='signup'), #Page de signup, when you don't have an account
    path('login/',views.login_Page, name='login'), #Page d'login
    path('',views.liste_livres, name='liste_livres'), #Page d'accueil qui affiche tous les livres
    path('catalogue/<str:nom_categorie>/',views.catalog_par_category, name='filtrer_categorie')   #url dynamique, this is where the url goes & take info from my view catalog function
]

