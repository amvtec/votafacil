from django.urls import path
from .views import editar_pauta  # Adicione essa linha na lista de imports
from core.views import api_vereadores_presencas
from .views import api_painel_publico
from .views import visualizar_pautas
from .views import gerar_relatorio_presencas
from .views import remover_pauta  # Adicione essa linha
from . import views
from .views import reabrir_votacao  # Adicione esta linha
from .views import sessoes_encerradas, reabrir_sessao
from .views import (
    login_view, logout_view, painel_presidente, painel_vereador, 
    registrar_presenca, votar_pauta, registrar_voto, abrir_sessao, 
    encerrar_sessao, iniciar_votacao, encerrar_votacao, voto_desempate, 
    ver_resultados, gerar_relatorio, painel_publico, ver_presencas, pautas_presidente
)

urlpatterns = [
    # Autenticação
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    # Painel do Vereador
    path("vereador/", painel_vereador, name="painel_vereador"),
    path("vereador/presenca/", registrar_presenca, name="registrar_presenca"),
    path("vereador/votar/<int:pauta_id>/", votar_pauta, name="votar_pauta"),
    path("vereador/registrar_voto/<int:pauta_id>/", registrar_voto, name="registrar_voto"),
    path('pautas/', visualizar_pautas, name='visualizar_pautas'),
    
    # Painel do Presidente
    path("presidente/", painel_presidente, name="painel_presidente"),
    path("presidente/abrir_sessao/<int:sessao_id>/", abrir_sessao, name="abrir_sessao"),
    path("presidente/encerrar_sessao/<int:sessao_id>/", encerrar_sessao, name="encerrar_sessao"),
    path('presidente/iniciar_votacao/<int:pauta_id>/<str:tipo_votacao>/', views.iniciar_votacao, name='iniciar_votacao'),
    path("presidente/encerrar_votacao/", encerrar_votacao, name="encerrar_votacao"),
    path("presidente/voto_desempate/<int:pauta_id>/", voto_desempate, name="voto_desempate"),
    path("presidente/ver_resultados/", ver_resultados, name="ver_resultados"),
    path("presidente/ver-presencas/<int:sessao_id>/", ver_presencas, name="ver_presencas"),
    path("presidente/editar_pauta/<int:pauta_id>/", editar_pauta, name="editar_pauta"),
    path("presidente/remover_pauta/<int:pauta_id>/", remover_pauta, name="remover_pauta"),
    path("presidente/reabrir_votacao/<int:pauta_id>/", reabrir_votacao, name="reabrir_votacao"),
    path('presidente/pautas/', pautas_presidente, name='pautas_presidente'),
    path("sessoes-encerradas/", sessoes_encerradas, name="sessoes_encerradas"),
    path("reabrir-sessao/<int:sessao_id>/", reabrir_sessao, name="reabrir_sessao"),
    path('relatorio-presencas/<int:sessao_id>/', gerar_relatorio_presencas, name='gerar_relatorio_presencas'),



    
    # Relatórios
    path("presidente/gerar_relatorio/<int:sessao_id>/", gerar_relatorio, name="gerar_relatorio"),
    
    # Painel Público
    path("painel_publico/", painel_publico, name="painel_publico"),
    path("api/vereadores_presencas/", api_vereadores_presencas, name="api_vereadores_presencas"),
    path('api/painel-publico/', api_painel_publico, name='api_painel_publico'),
]
