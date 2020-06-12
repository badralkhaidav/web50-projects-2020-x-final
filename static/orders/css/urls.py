from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = []
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.order, name="order"),
    path("result", views.result, name="result"),
    path("check", views.check, name="check"),
    path("order_result", views.order_result, name="order_result"),
    path("transfer_index", views.transfer_index, name="transfer_index"),
    path("transfer_order", views.transfer_order, name="transfer_order"),
    path("transfer_result", views.transfer_result, name="transfer_result"),
    path("transfer_check", views.transfer_check, name="transfer_check"),
]
