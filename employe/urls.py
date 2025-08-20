from django.urls import path
from . import views
urlpatterns = [
    path("", views.list_employe, name="list_employe"),
    path("ajouter/", views.ajouter_employer, name="ajouter_employer"),
    path("modifier/<int:id>/", views.modifier_employer, name="modifier_employer"),
    path("supprimer/<int:id>/", views.supprimer_employer, name="supprimer_employer"),
    
    
]
 