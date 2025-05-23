from django.urls import path
from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('add-user/', views.add_user, name='add_user'),
    path('list-users/', views.list_users, name='list_users'),

    path('edit-user/<str:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<str:user_id>/ ', views.delete_user, name='delete_user'),
    path('', views.home , name='home'),
    path('employee/', views.employee , name='employee'),

    path('contact_us/', views.contact_us , name='contact_us'),

    path('info/', views.info , name='info'),

    path('FAQs/', views.FAQs , name='FAQs'),

    path('home/', views.home, name='home'),

    path('UnderstandingTax/', views.UnderstandingTax, name='UnderstandingTax'),

    path('UnderstandingW2/', views.UnderstandingW2, name='UnderstandingW2'),
    path('collect/', views.collect_info, name='collect_info'),
    path('display/', views.display_info, name='display_info'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('save_info/', views.save_info, name='save_info'),
    path('list-users/', views.list_users, name='list_users'),

]

