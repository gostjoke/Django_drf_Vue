from . import views
from rest_framework.routers import DefaultRouter

urlpatterns =[]

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)

urlpatterns += router.urls