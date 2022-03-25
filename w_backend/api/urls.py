from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name="api-overwiev"),
  path('woman-list', views.womanList, name="woman-list"),                 #OK
  path('woman-detail/<str:pk>', views.womanDetail, name="woman-detail"),  #OK
  path('woman-create', views.womanCreate, name="woman-create"),           #OK
  path('woman-update/<str:pk>', views.womanUpdate, name="woman-update"),  #OK - with all woman object not just one key
  path('woman-delete/<str:pk>', views.womanDelete, name="woman-delete"),  #OK - remember to click on delete on the page
]