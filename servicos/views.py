from django.views.generic.base import TemplateView 
from base.base_admin_permissions import BaseAdminUsersall

class IndexServicosView(BaseAdminUsersall, TemplateView):
	template_name = 'index-servicos.html'

class ServicosView(BaseAdminUsersall, TemplateView):
	template_name = 'servicos.html'
