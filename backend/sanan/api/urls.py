from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView 
)



router = DefaultRouter()

router.register('posts', views.PostViewSet, basename='posts')
router.register('projects', views.ProjectViewSet, basename='projects')
router.register( 
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet, 
    basename='comments' 
)
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='token-create'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
