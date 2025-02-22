from django.urls import path
from .views import plot_api
from .views import run_management_command
from . views import pie_api


urlpatterns = [
     path("plot/", plot_api, name="plot_api"),
     path("api/run-command/", run_management_command, name="run_command"),
     path("pie/", pie_api, name="pie_api"),
]
