from django.db import models
from django.contrib.auth.models import User # Pour le Login/Signup
 
#this class permits to add new categories on our admin interface w:o affecting our code: this is whr i configure my db
class Categorie(models.Model):
    libelle = models.CharField(max_length=40)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.libelle}"


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, blank=True, null=True)
    fichier_pdf = models.FileField(upload_to='livres_pdfs/', blank=True, null=True)
    book_cover = models.ImageField(upload_to='livres_cover/', blank=True, null=True)
    
    def __str__(self):
       return f"{self.titre} {self.categorie} (écrit par {self.author})"
  

#class Customer(models.Model):
    #On lie notre modèle au User de Django
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #details = models.TextField(blank=True)
    
    #def __str__(self):
      #  return self.user.username

   
   