from django.db.models.base import Model
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from base.base_admin_permissions import BaseAdminUsersAd
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import CustomUser
from django.views.generic import ListView
from django.contrib.auth.views import (
	LoginView,
	PasswordChangeView,
	PasswordResetView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
	)


class UserLogin(SuccessMessageMixin, LoginView):
	template_name = 'accounts/login.html'
 
	def get(self, request, *args, **kwargs): 
		if self.request.user.is_authenticated:
			return redirect('index-administrador') 
		else:
			return self.render_to_response(self.get_context_data())

class UserCreate(SuccessMessageMixin, CreateView):
	model = CustomUser
	form_class = CustomUserCreateForm
	template_name = 'accounts/user-new.html'
	success_url = reverse_lazy('login')
	success_message = 'Bem Vindo(a)! Faça login para começar'


class UserChange(BaseAdminUsersAd, UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	template_name = 'accounts/user-change.html'
	success_url = reverse_lazy('index')
	success_message = 'Sua mudança de perfil foi bem-sucedida' 

class UserDelete(BaseAdminUsersAd, DeleteView):
	model = CustomUser
	success_url = reverse_lazy('index')
	template_name = 'accounts/user-delete.html'

	def get_success_url(self): 
		messages.success(self.request, self.success_message) 
		return reverse('users')


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
	template_name = 'accounts/password-change.html'
	success_url = reverse_lazy('index')
	success_message = 'Sua mudança de senha foi bem sucedida'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
	template_name = 'accounts/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
	success_message = 'Sua senha foi redefinida corretamente. Faça login para começar'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
	template_name = 'accounts/password-reset-complete.html'
	success_message = 'Sua senha foi redefinida corretamente. Faça login para começar'

	def get(self, request, *args, **kwargs):

		return redirect('login')

class UserListView(BaseAdminUsersAd, ListView):
	model = CustomUser
	template_name = 'accounts/usuarios.html' 