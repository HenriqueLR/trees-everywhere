from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class DefaultFieldsModel(models.Model):
	updated_at = models.DateTimeField(verbose_name=u'Updated At', auto_now=True, db_column='updated_at')
	created_at = models.DateTimeField(verbose_name=u'Created At', auto_now_add=True, db_column='created_at')
	description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Description')

	class Meta:
		abstract = True



class Trees(DefaultFieldsModel):
	alias = models.CharField(max_length=200, verbose_name="Alias", db_column="alias", unique=True) 
	name = models.CharField(max_length=120, verbose_name="Name", db_column="name", 	unique=True) 

	def __str__(self):
		return f'{self.alias}'

	def get_absolute_url(self):
		return reverse('trees:update', kwargs={'pk':self.pk})

	@property
	def _name(self):
		return self.name

	class Meta:
		verbose_name = 'Trees'
		verbose_name_plural = 'Trees'
		ordering=['-created_at']
		db_table='trees'



class PlantTree(DefaultFieldsModel):
	age = models.IntegerField(verbose_name='Age', null=False, db_column="age")
	user = models.ForeignKey(User, verbose_name='User', related_name="user_plan_tree", on_delete=models.CASCADE, null=False)    
	trees = models.ForeignKey(Trees, verbose_name="Trees", null=False, on_delete=models.CASCADE, related_name='trees_plant')
	lt = models.DecimalField(verbose_name='Lat', max_digits=22, decimal_places=16, null=False, db_column="lt")
	lg = models.DecimalField(verbose_name='Long', max_digits=22, decimal_places=16, null=False, db_column="lg")
    
	def __str__(self):
		return f'{self.trees.alias}'

	def get_absolute_url(self):
		return reverse('trees:update', kwargs={'pk':self.pk})

	class Meta:
		verbose_name = 'PlantTree'
		verbose_name_plural = 'PlantTree'
		ordering=['-created_at']
		db_table='planttree'