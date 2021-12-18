from django.views.generic.base import TemplateView 
from base.base_admin_permissions import BaseAdminUsersall

class IndexRelatorioView(BaseAdminUsersall, TemplateView):
	template_name = 'index-relatorio.html'

class RelatorioView(BaseAdminUsersall, TemplateView):
	template_name = 'relatorio.html'
