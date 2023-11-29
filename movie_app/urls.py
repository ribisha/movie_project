

from django.urls import path
from .import views
# for name space
app_name='movie_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('details/<int:movie_id>/',views.details,name='details'),
    path('add_movie/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
