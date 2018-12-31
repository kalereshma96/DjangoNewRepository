from django.urls import path
from . import views


urlpatterns = [
     path('', views.register, name='register'),
     path('profile/', views.profile, name='profile'),
     path('home/', views.HomeView.as_view(), name='home'),
     # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
     # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]





