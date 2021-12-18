from django.views.generic.base import TemplateView  
from base.base_admin_permissions import BaseAdminUsersAd

class IndexRecursoshumanosView(BaseAdminUsersAd, TemplateView):
	template_name = 'recursoshumanos/index-recursos.html'