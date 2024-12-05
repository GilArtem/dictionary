from .views import file_views
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', file_views.home_page, name='home'),
    path('home', file_views.home_page, name='home'),
    path('home/', file_views.home_page, name='home'),
    path('word_list', file_views.show_words_page, name='word_list'),
    path('word_list/', file_views.show_words_page, name='word_list'),
    path('add_word', file_views.add_word_page, name='add_word'),
    path('add_word/', file_views.add_word_page, name='add_word'),
    path('search', file_views.search_word_page, name='search'),
    path('edit_word', file_views.edit_word_page, name='edit_word'),
    path('edit_word/', file_views.edit_word_page, name='edit_word'),
    path('delete_word', file_views.delete_word_page, name='delete_word'),
    path('delete_word/', file_views.delete_word_page, name='delete_word'),
]

# Для того, чтобы при отображении страницы прогружались стили 
# Импортируем переменные статики 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
