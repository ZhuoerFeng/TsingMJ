from rest_framework.routers import DefaultRouter
from .views import PaipuList, PaipuDetailByName, PaipuDetailById, TestList, TestDetail
from django.urls import path, include

# router = DefaultRouter()
# router.register(r'paipus', PaipuView, basename='paipu')

urlpatterns = [
    path('test', TestList.as_view(), name='test-list'),
    path('test/<int:pk>', TestDetail.as_view(), name='test-detail'),
    path('paipu', PaipuList.as_view(), name='paipu-list'),
    path('paipu/name=<str:match_name>', PaipuDetailByName.as_view(), name='paipu-detail'),
    path('paipu/id=<int:pk>', PaipuDetailById.as_view(), name='paipu-detail'),

]