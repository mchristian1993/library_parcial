from django.shortcuts import render

from .models import Autor

def index(request):
    autores = Autor.objects.order_by('nombre')
    context = {'autores': autores}
    return render(request, 'library/index.html', context)
