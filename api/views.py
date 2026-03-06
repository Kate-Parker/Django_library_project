from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog .models import Livre
from .serializers import LivreSerializer


#this page permits us to serialize & view our data into a json format on the net

@api_view(['GET'])
def api_livres(request):
    livre = Livre.objects.all()
    serializer = LivreSerializer(livre,many=True)
    return Response(serializer.data)








