from django.http import JsonResponse
from django.views.generic.list import BaseListView

from goods.models import Goods


class GoodsMixin:
    model = Goods
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Goods.objects.values('id', 'where_from', 'where_to', 'date', 'time')
        print(f"context: {queryset}")
        return queryset

    def render_to_response(self, context, **response_kwargs):
        print(f"context: {context}")
        return JsonResponse(context)


class GoodsDetailView(GoodsMixin, BaseListView):

    def get_context_data(self, **kwargs):
        context = {
            "result": list(self.get_queryset())
        }
        return context
