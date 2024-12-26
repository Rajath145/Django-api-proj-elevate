from django.urls import path
from movieapp import views

urlpatterns=[
    path("",views.movieapi),
    path('<int:id>',views.movieapi),
    path("index/",views.index,name="movies")
]