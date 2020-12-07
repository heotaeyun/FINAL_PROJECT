from django.urls import path

from. import views

app_name = "movies"

urlpatterns = [
    path('', views.start, name='start'),
    path('popular/', views.popular_movies, name='popular'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommendation/<str:genre1>/<str:genre2>/', views.recommendation, name='recommendation'),
    path('show/<str:genre>/', views.show_movies, name='show_movies'),
    path('about/', views.about, name='about'),
]