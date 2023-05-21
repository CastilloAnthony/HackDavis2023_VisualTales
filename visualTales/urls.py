from django.contrib import admin
from django.urls import path, include
from .views import generate_image_from_txt

app_name = "visualTales"

urlpatterns =[
  path("admin/", admin.site.urls),
  path("",generate_image_from_txt, name="generate_image_from_txt"),
]
  
