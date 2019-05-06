from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('api/vendors/', views.switch_vendor_list, name='switch_vendor_list'),
    path('vendors/', views.homepage_vendors, name='homepage_vendors'),
    path('api/vendors/detail/<int:pk>/', views.switch_vendor_detail, name='switch_vendor_detail'),
    path('api/switch_models/', views.SwitchModelList.as_view(), name='switch_model_list'),
    path('switch_models/', views.homepage_switch_models, name='homepage_switch_models'),
    path('api/switch_models/detail/<int:pk>/', views.SwitchModelDetailList.as_view(), name='switch_model_detail'),
    path('api/user_places/', views.UserPlaceList.as_view(), name='user_places_list'),
    path('user_places/', views.homepage_user_places, name='homepage_user_places'),
    path('api/user_places/active/', views.UserPlacesWithActiveList.as_view(), name='user_places_with_active_list'),
    path('api/user_places/detail/<int:pk/>', views.UserPlaceDetail.as_view(), name='user_place_detail'),
    path('api/users/', views.UserList.as_view(), name='users'),
    path('users/', views.homepage_users, name='homepage_users'),
    path('api/users/active/', views.UsersWithActiveList.as_view(), name='users_with_active'),
    path('api/users/detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)











# urlpatterns = [
#     path('', views.all_switches, name='all_switches'),
#     path('detail_switch/<int:pk>', views.detail_switch, name='detail_switch')
# ]