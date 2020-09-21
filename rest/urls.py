from django.urls import path

from rest.views import index, posts, FirstView, FirstInheritView, PostListView, GeneratePdfView
urlpatterns = [
    path('', index),
    path('posts/',posts),
  #  path('post_list/<int:post_id>', views.post_list_id),
  path('greet/',FirstView.as_view()),
  path('greetin/', FirstInheritView.as_view() ),

  path('modelist/', PostListView.as_view() ),

  path('pdf/', GeneratePdfView.as_view())
]