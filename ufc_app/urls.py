from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="fighters_list", permanent=False), name="home"),
    path("weight-classes/", views.weight_classes_list, name="weight_classes_list"),
    path("weight-classes/<int:pk>/edit/", views.weight_class_update, name="weight_class_update"),
    path("weight-classes/<int:pk>/delete/", views.weight_class_delete, name="weight_class_delete"),
    path("fighters/", views.fighters_list, name="fighters_list"),
    path("fighters/<int:pk>/edit/", views.fighter_update, name="fighter_update"),
    path("fighters/<int:pk>/delete/", views.fighter_delete, name="fighter_delete"),
    path("events/", views.events_list, name="events_list"),
    path("events/<int:pk>/edit/", views.event_update, name="event_update"),
    path("events/<int:pk>/delete/", views.event_delete, name="event_delete"),
    path("fights/", views.fights_list, name="fights_list"),
    path("fights/<int:pk>/edit/", views.fight_update, name="fight_update"),
    path("fights/<int:pk>/delete/", views.fight_delete, name="fight_delete"),
    path("results/", views.results_list, name="results_list"),
    path("results/<int:pk>/edit/", views.result_update, name="result_update"),
    path("results/<int:pk>/delete/", views.result_delete, name="result_delete"),
]
