from django.urls import path
from .views import ViewDaPagPrincipal, Assunto


urlpatterns = [
        path('', ViewDaPagPrincipal.as_view(), name='home'),
        path('papo/', Assunto.as_view(), name='Papo')
    ]