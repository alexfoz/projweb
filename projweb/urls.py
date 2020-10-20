"""projweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from ausencia.api.viewsets import AusenciaViewSet
from cargo.api.viewsets import CargoViewSet
from departamento.api.viewsets import DepartamentoViewSet
from escala.api.viewsets import EscalaViewSet
from feedBack.api.viewsets import FeedbackViewSet
from ferias.api.viewsets import FeriasViewSet
from historicoTicket.api.viewsets import HistoricoticketViewSet
from horarios.api.viewsets import HorariosViewSet
from painelInformacoes.api.viewsets import PainelInformacoesViewSet
from periodo.api.viewsets import PeriodoViewSet
from tickets.api.viewsets import TicketsViewSet
from ticketstatus.api.viewsets import TicketStatusViewSet
from usuario.api.viewsets import UsuarioViewSet
from usuariot.api.viewsets import UsuariotViewSet


router = routers.DefaultRouter()
router.register(r'ausencia', AusenciaViewSet)
router.register(r'cargo', CargoViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'escala', EscalaViewSet)
router.register(r'feedBack', FeedbackViewSet)
router.register(r'ferias', FeriasViewSet)
router.register(r'historicoTicket', HistoricoticketViewSet)
router.register(r'horarios', HorariosViewSet)
router.register(r'painelInformacoes', PainelInformacoesViewSet)
router.register(r'periodo', PeriodoViewSet)
router.register(r'tickets', TicketsViewSet)
router.register(r'ticketsStatus', TicketStatusViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'usuariot', UsuariotViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
