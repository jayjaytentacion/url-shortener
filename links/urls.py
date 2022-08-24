from django.urls import path
from .import views


urlpatterns=[
    path('',views.api_root),
    path('shorten/',views.Linkshortener.as_view(),name='links'),
    path('<str:short_url>', views.redirect_view)
]
