from django.urls import path
from .views import (get_users, create_user, 
MyTokenObtainPairView, get_user_inventories, 
get_user_id, get_items, create_inventory, 
create_item, delete_item, update_item, get_item, delete_inventory,
update_inventory, get_inventory)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('signup/', create_user, name='create_user'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('inventories/user/<uuid:user_id>/', get_user_inventories, name='get_user_inventories'),
    path('user/<str:username>/', get_user_id, name='get_user_id'),
    path('items/<uuid:inventory_id>/', get_items, name='get_items'),
    path('inventory/', create_inventory, name='create_inventory'),
    path('item/', create_item, name='create_item'),
    path('items/<uuid:item_id>/delete/', delete_item, name='delete_item'),
    path('items/<uuid:item_id>/update/', update_item, name='update_item'),
    path('item/<uuid:item_id>/', get_item, name='get_item'),
    path('inventory/<uuid:inventory_id>/delete/', delete_inventory, name='delete_inventory'),
    path('inventories/<uuid:inventory_id>/update/', update_inventory, name='update_inventory'),
    path('inventory/<uuid:inventory_id>/', get_inventory, name='get_inventory')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
