from django.urls import path
from recursoshumanos.views import (IndexRecursoshumanosView)


urlpatterns = [
	path('', IndexRecursoshumanosView.as_view(), name='index-recursos'), 
] 