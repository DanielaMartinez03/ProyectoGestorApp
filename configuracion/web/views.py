from django.shortcuts import render
#Render --> es Renderizar y significa Pintar

# Create your views here.
def Home(request):
    return render(request, 'index.html')