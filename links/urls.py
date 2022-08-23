from django.urls import path
from .import views


urlpatterns=[
    path('',views.Linkshortener.as_view(),name='link-shortener'),
    path('<str:short_url>', views.redirect_view)
]