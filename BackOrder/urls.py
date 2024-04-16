from django.urls import path , include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from BackOrder import views
from rest_framework.urlpatterns import format_suffix_patterns

#api router
router = routers.DefaultRouter()

urlpatterns = [
    path('backorders/', views.BackOrderList.as_view()),
    path('backorders/<int:pk>/', views.BackOrderDetail.as_view()),
    path('docs/', include_docs_urls(title='Cars Dealer API'))
]
urlpatterns = format_suffix_patterns(urlpatterns)
