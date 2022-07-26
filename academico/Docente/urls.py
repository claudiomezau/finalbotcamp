from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import DocenteList, DocenteCreate, DocenteUpdate , DocenteDelete
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from Docente import views

urlpatterns = [
    #localhost:8000/docente/api
    path('api/', views.API_objects.as_view()),
    #localhost:8000/docente/api/n°
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('listar/', DocenteList.as_view(), name="docentes_list"),
    path('crear/', DocenteCreate.as_view(), name="docentes_form"),
    path('editar/<int:pk>', DocenteUpdate.as_view(), name="docentes_update"),
    path('borrar/<int:pk>', DocenteDelete.as_view(), name="docentes_borrar"),
    
]
