from django.views.generic import TemplateView
# Create your views here.

class ViewDaPagPrincipal(TemplateView):
    
    template_name = 'home.html'

class Assunto(TemplateView):
    template_name = 'AboutP.html'
