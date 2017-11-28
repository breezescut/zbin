from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'hello_text': 'Hello World!',}
    return render(request, 'risk_control/index.html', context)