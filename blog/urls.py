from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', PostListView.as_view(), name='post_list'),
    path('blogs/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blogs/create/', PostCreateView.as_view(), name='post_create'),
    path('blogs/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('blogs/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
