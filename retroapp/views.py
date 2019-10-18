from django.shortcuts import render
from .models import Juego, Genero, Empresa, JuegoInstance

# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio
    """

    #Genera contadores de algunos de los objetos principales
    num_games=Juego.objects.all().count()
    num_instances=JuegoInstance.objects.all().count()
    #Juegos disponibles (status = 'a')
    num_instances_available=JuegoInstance.objects.filter(status__exact='a').count()
    num_empresa=Empresa.objects.count() #El 'all()' está implícito por defecto.

    #Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_games':num_games,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_empresa':num_empresa},
    )
