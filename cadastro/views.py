from django.views.generic.base import TemplateView 
from base.base_admin_permissions import BaseAdminUsersall

class IndexCadastroView(BaseAdminUsersall, TemplateView):
	template_name = 'index-cadastro.html'

class CadastroView(BaseAdminUsersall, TemplateView):
	template_name = 'cadastro.html'
