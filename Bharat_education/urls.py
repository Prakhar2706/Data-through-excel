from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from data import views
from data.views import download_pdf

router = DefaultRouter()
router.register(r'universities', views.UniversityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/list-universities/', views.list_universities, name='list-universities'),
    path('api/receive_lead/', views.receive_lead, name='receive_lead'),
    path('api/upload_leads/', views.upload_leads, name='upload_leads'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/download_pdf/', download_pdf, name='download_pdf'),
]
