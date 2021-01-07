from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django_iamge.api import views

router = routers.DefaultRouter()
# router.register(r'posts', views.PostsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', views.post_collection),
    path('detail/<str:title>', views.detail_collection),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
