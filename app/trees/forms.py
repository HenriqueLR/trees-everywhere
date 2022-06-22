from django import forms
from trees.models import Trees, PlantTree


class TreesForm(forms.ModelForm):

	class Meta:
		model = Trees
		fields = ['name', 'alias']


class PlantTreeForm(forms.ModelForm):

	class Meta:
		model = PlantTree
		fields = ['age', 'lt', 'lg']
