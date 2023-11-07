from django.urls import path
from Scrapper.views import *

urlpatterns = [
    path('import-csv/', import_csv, name='import_csv'),
]