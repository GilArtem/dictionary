from . import views
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home', views.home_page, name='home'),
    path('home/', views.home_page, name='home'),
    path('word_list', views.show_words_page, name='word_list'),
    path('word_list/', views.show_words_page, name='word_list'),
    path('add_word', views.add_word_page, name='add_word'),
    path('add_word/', views.add_word_page, name='add_word'),
    path('search', views.search_word_page, name='search'),
    path('edit_word', views.edit_word_page, name='edit_word'),
    path('edit_word/', views.edit_word_page, name='edit_word'),
    path('delete_word', views.delete_word_page, name='delete_word'),
    path('delete_word/', views.delete_word_page, name='delete_word'),
]

# Для того, чтобы при отображении страницы прогружались стили 
# Импортируем переменные статики 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
