from django.urls import path
from relatorio.views import (IndexRelatorioView, RelatorioView)


urlpatterns = [
	path('', IndexRelatorioView.as_view(), name='index-relatorio'),
	path('relatorio/', RelatorioView.as_view(), name='relatorio'), 
] 