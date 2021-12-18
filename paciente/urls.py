from django.urls import path
from paciente.views import (IndexPacienteView, PacienteView)


urlpatterns = [
	path('', IndexPacienteView.as_view(), name='index-paciente'),
	path('paciente/', PacienteView.as_view(), name='paciente'), 
] 