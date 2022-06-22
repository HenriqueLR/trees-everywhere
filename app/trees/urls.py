from django.urls import path
from trees.views import list_plants, plant_tree, add_tree, list_trees, detail_plants

urlpatterns=[
	path('list_plants/', list_plants, name='list_plants'),
	path('plant_tree/<int:param>/', plant_tree, name='plant_tree'),
	path('add_tree/', add_tree, name='add_tree'),
	path('list_trees/', list_trees, name='list_trees'),
	path('detail_plants/<int:id>/<str:fp>/', detail_plants, name='detail_plants')
]