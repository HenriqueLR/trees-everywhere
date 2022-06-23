from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import Account, User, Profile
from django.contrib.auth.models import Group
from accounts.forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAdmin(BaseUserAdmin):

	form = UserAdminChangeForm
	add_form = UserAdminCreationForm
	list_display = ['email', 'is_staff']
	list_filter = ['is_staff']
	fieldsets = (
		(None, {'fields': ('email', 'password', 'account')}),
		('Permissions', {'fields': ('is_active',)}),
	)
	add_fieldsets = (
			(None, {
			'classes': ('wide',),
			'fields': ('email', 'password', 'password_2', 'account', 'is_active'),}
		),
	)
	search_fields = ['email']
	ordering = ['email']
	filter_horizontal = ()


class AccountAdmin(admin.ModelAdmin):
	
	list_display = ["cpf", "status_account"]
	actions = ['disabled_accounts', 'active_accounts']

	@admin.action(description='disabled accounts')
	def disabled_accounts(self, request, queryset):
		queryset.update(status_account=False)

	@admin.action(description='active accounts')
	def active_accounts(self, request, queryset):
		queryset.update(status_account=True)


class ProfileAdmin(admin.ModelAdmin):
	
	list_display = ["first_name", "get_username"]    

	@admin.display(ordering='profile_user', description='User')
	def get_username(self, obj):
		return obj.user.email


admin.site.unregister(Group)
admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
