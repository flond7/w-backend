from django.urls import path
from . import views
urlpatterns = [
  path('', views.apiOverview, name="api-overwiev"),
  path('woman-list', views.womanList, name="woman-list"),
  path('woman-detail/<str:pk>', views.womanDetail, name="woman-detail"),
  path('woman-create', views.womanCreate, name="woman-create"),
  path('woman-update/<str:pk>', views.womanUpdate, name="woman-update"),
  path('woman-delete/<str:pk>', views.womanDelete, name="woman-delete"),
  """ path('woman-open-paths', views.womanOpenPaths, name="woman-open-paths"),
  path('path-create/<str:pk>', views.pathCreate, name="path-create"),
  path('appointment-create/<str:wk>/<str:pk>', views.appointmentCreate, name="appointment-create"), """
]