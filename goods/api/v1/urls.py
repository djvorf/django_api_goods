from django.urls import path

from .views import GoodsDetailView

urlpatterns = [
    path('goods/', GoodsDetailView.as_view()),
]