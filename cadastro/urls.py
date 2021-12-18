from django.urls import path
from cadastro.views import (IndexCadastroView, CadastroView)


urlpatterns = [
	path('', IndexCadastroView.as_view(), name='index-cadastro'),
	path('cadastro/', CadastroView.as_view(), name='cadastro'), 
] 