from rest_framework import routers

from sendEmail import views

router = routers.DefaultRouter()
router.register(r'email', views.emailView, basename='email')

urlpatterns = router.urls