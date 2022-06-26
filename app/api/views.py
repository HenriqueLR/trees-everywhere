from rest_framework.views import APIView
from rest_framework.response import Response
from trees.models import Trees
from api.serializers import TreeSerializer
from django.db.models import Count


class TreeApiView(APIView):

    def get(self, request, *args, **kwargs):
        trees_plant = Trees.objects.filter(trees_plant__user__account__in=\
                                            request.user.account.filter(status_account=True))\
							        .annotate(count_plant=Count('trees_plant', distinct=True))\
								    .order_by('-pk').distinct()
        serializer = TreeSerializer(trees_plant, many=True)
        return Response(serializer.data)


list_tree_api = TreeApiView.as_view()
