from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls', namespace='index')),
    path('pages/', include('pages.urls', namespace='pages')),
]
