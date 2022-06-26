# Generated by Django 3.2.13 on 2022-06-26 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Created At')),
                ('description', models.TextField(blank=True, db_column='description', null=True, verbose_name='Description')),
                ('alias', models.CharField(db_column='alias', max_length=200, unique=True, verbose_name='Alias')),
                ('name', models.CharField(db_column='name', max_length=120, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Trees',
                'verbose_name_plural': 'Trees',
                'db_table': 'trees',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PlantTree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Created At')),
                ('description', models.TextField(blank=True, db_column='description', null=True, verbose_name='Description')),
                ('age', models.IntegerField(db_column='age', verbose_name='Age')),
                ('lt', models.DecimalField(db_column='lt', decimal_places=16, max_digits=22, verbose_name='Lat')),
                ('lg', models.DecimalField(db_column='lg', decimal_places=16, max_digits=22, verbose_name='Long')),
                ('trees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trees_plant', to='trees.trees', verbose_name='Trees')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_plan_tree', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'PlantTree',
                'verbose_name_plural': 'PlantTree',
                'db_table': 'planttree',
                'ordering': ['-created_at'],
            },
        ),
    ]
