from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index', views.index, name='index'),
    path('Bio', views.Bio, name='Bio'),
    path('TecTips', views.TecTips, name='TecTips'),
    path('', views.home, name='home'),
    path('archive', views.archive, name='archive'),
    path('home/<int:question_id>', views.entry, name='entry'),
    path('<int:question_id>/add_comment/', views.add_comment, name='add_comment'),
    path('init', views.init, name='init')
]
