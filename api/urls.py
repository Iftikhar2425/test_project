from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, RoleViewSet, UserViewSet, TestimonialViewSet, SetupCreateView,SetupRetrieveView


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'testimonials', TestimonialViewSet)
#router.register(r'setup',SetupCreateView.as_view)


urlpatterns = [
    path('', include(router.urls)),
   path('setup/', SetupCreateView.as_view(), name='setup_view'),
    path('setup/<int:pk>/', SetupRetrieveView.as_view(), name='setup-retrieve'),
] 
