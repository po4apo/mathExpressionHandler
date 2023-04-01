from django.contrib import admin
from django.urls import path

from mathExpressionHandler.webAPI.views import MathExpressionHandlerAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MathExpressionHandlerAPIView.as_view(), name='expression')
]
