from django.views.generic.base import TemplateView 
from base.base_admin_permissions import BaseAdminUsersall

class IndexPacienteView(BaseAdminUsersall, TemplateView):
	template_name = 'index-paciente.html'

class PacienteView(BaseAdminUsersall, TemplateView):
	template_name = 'paciente.html'
