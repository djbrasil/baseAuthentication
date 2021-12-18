from django.urls import path
from servicos.views import (IndexServicosView, ServicosView)


urlpatterns = [
	path('', IndexServicosView.as_view(), name='index-servicos'),
	path('servicos/', ServicosView.as_view(), name='servicos'), 
] 