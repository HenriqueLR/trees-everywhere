
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from trees.forms import TreesForm, PlantTreeForm
from trees.models import Trees, PlantTree
from django.forms.models import formset_factory
from django.db.models import Count
from django.views.generic import CreateView
from django.contrib import messages
from accounts.decorators import login_required
from trees.permissions import PermissionsTreeCreateMixin



@login_required
def list_trees(request):
	context = {
		'trees': Trees.objects.all()
	}
	return render(request, "trees/list_trees.html", context)


@login_required
def list_plants(request):
	fp = request.GET.get('fp')
	if fp == "all":
		trees = Trees.objects.filter(trees_plant__user__account__in=request.user.account.filter(status_account=True))\
							 .annotate(count_plant=Count('trees_plant', distinct=True))\
								.order_by('-pk').distinct()
	else:
		fp = "my"
		trees = Trees.objects.filter(trees_plant__user=request.user)\
								.annotate(count_plant=Count('pk')).order_by('-pk')
	
	context = {
		'trees':trees,
		'fp': fp,
	}
	return render(request, 'trees/list_plants.html', context)


@login_required
def detail_plants(request, id, fp):
	tree = get_object_or_404(Trees, pk=id)
	if fp == "all":
		plants = PlantTree.objects.filter(user__account__in=request.user.account.filter(status_account=True),\
											trees=tree).order_by('-pk').distinct()
	else:
		plants = PlantTree.objects.filter(trees=tree, user=request.user).order_by('-pk')
	context = {'plants': plants, 'fp': fp, 'tree': tree}
	return render(request, 'trees/detail_plant.html', context)


@login_required
def plant_tree(request, param):
	tree =  get_object_or_404(Trees, pk=param)
	planttreeformset = formset_factory(PlantTreeForm, extra=1)
	formset = planttreeformset(request.POST or None)

	if all([formset.is_valid()]):
		for form in formset:
			child = form.save(commit=False)
			child.trees = tree
			child.user = request.user
			child.save()
		messages.success(request, 'Tree planted')
		return redirect('trees:list_plants')
	context = {
		"formset": formset,
		"tree":tree,
	}			
	return render(request, "trees/plant_tree.html", context)		



class CreateTreeView(PermissionsTreeCreateMixin, CreateView):

	model = Trees
	form_class = TreesForm
	template_name = 'trees/new_tree.html'
	success_url = reverse_lazy('trees:list_trees')
	message_success = 'Tree created success'

add_tree = CreateTreeView.as_view()