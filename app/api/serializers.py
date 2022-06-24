from rest_framework import serializers
from trees.models import Trees, PlantTree


class PlantTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantTree
        fields = '__all__'


class TreeSerializer(serializers.ModelSerializer):
    trees_plant = PlantTreeSerializer(many=True)

    class Meta:
        model = Trees
        fields = '__all__'
