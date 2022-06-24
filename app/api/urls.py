from django.urls import path
from api.views import list_tree_api


urlpatterns=[
	path('v1/trees/list_my_plants/', list_tree_api, name='list_my_plants'),
]
