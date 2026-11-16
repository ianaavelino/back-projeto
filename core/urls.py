
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import EventoViewSet, ParticipanteViewSet

# Configuração do roteador da API
router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'participantes', ParticipanteViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('eventos/', views.eventos, name='eventos'),
    path('participantes/', views.participantes, name='participantes'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/excluir/<int:evento_id>/', views.excluir_evento, name='excluir_evento'),
    path('participantes/editar/<int:participante_id>/', views.editar_participante, name='editar_participante'),
    path('participantes/excluir/<int:participante_id>/', views.excluir_participante, name='excluir_participante'),
    path('logout/', views.logout_view, name='logout'),

    # Rotas da API
    path('api/', include(router.urls)),
]
