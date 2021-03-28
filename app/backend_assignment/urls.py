from django.urls import include, path
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'videos', views.VideoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('', include('backend_assignment.api_server.urls')),
]