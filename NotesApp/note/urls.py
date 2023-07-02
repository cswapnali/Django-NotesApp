from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogOutPage, name='logout'),
    path('notes/', views.notes, name='notes'),
    path('note/add/', views.add_note, name='add_note'),
    path('note/<int:note_id>/delete/', views.delete_note, name='delete_note'),
    path('note/<int:note_id>/share/', views.share_note, name='share_note'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
