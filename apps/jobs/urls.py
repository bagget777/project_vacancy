from django.urls import path
from apps.jobs import views
from django.views.decorators.csrf import csrf_protect
urlpatterns = [
    path('company_listing_single/<int:id>/', views.company_listing_single,name = "company_listing_single"),
    path('company_listing', views.company_listing,name = "company_listing"),
    path('listing_single', views.listing_single,name = "listing_single"),
    path('cv', views.cv,name = "cv"),
    path('cv_add', views.cv_add,name = "cv_add"),
    path('cv_download/', csrf_protect(views.cv_download), name="cv_download"),
    path('about', views.about,name= "about"),
    path('contact', views.contact,name= "contact"),
]