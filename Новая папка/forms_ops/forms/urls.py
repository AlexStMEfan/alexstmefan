from django.urls import path

from forms.views import index

urlpatterns = [
    path('', index)
]