from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('new', views.new, name='page2'),
# ]

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('husky/', views.first_breed, name='first_breed'),
    path('german-shepherd/', views.second_breed, name='second_breed'),
    path('labrador/', views.third_breed, name='third_breed'),
    path('spitz/', views.fourth_breed, name='fourth_breed'),
]