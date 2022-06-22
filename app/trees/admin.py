from django.contrib import admin
from trees.models import Trees, PlantTree


class PlantTreeStackedAdmin(admin.StackedInline):
	model = PlantTree
	extra = 1

class TreesAdmin(admin.ModelAdmin):
	list_display = ['name', 'alias']
	inlines = [PlantTreeStackedAdmin]

class PlanTreeAdmin(admin.ModelAdmin):
	
	list_display = ['trees', 'get_first_name', 'user', 'age', 'lt', 'lg']

	@admin.display(ordering='user_plan_tree', description='First name')
	def get_first_name(self, obj):
		return obj.user.profile_user.first_name

admin.site.register(Trees, TreesAdmin)
admin.site.register(PlantTree, PlanTreeAdmin)
