from django.urls import path
from .views import *

company = [path("company/all", CompanyViewSet.as_view({"get": "list"})),
           path("company/<int:pk>", CompanyViewSet.as_view({"get": "retrieve", "delete": "destroy", "patch": "partial_update"}))]

container = [path("container/all", ContainerViewSet.as_view({"get": "list"})),
             path("container/<int:pk>", ContainerViewSet.as_view({"get": "retrieve", "delete": "destroy", "patch": "partial_update"}))]

status = [path("status/all", StatusViewSet.as_view({"get": "list"})),
          path("status/<int:pk>", StatusViewSet.as_view({"get": "retrieve", "delete": "destroy", "patch": "partial_update"}))]

product = [path("product/all", ProductViewSet.as_view({"get": "list"})),
           path("product/<int:pk>", ProductViewSet.as_view({"get": "retrieve", "delete": "destroy", "patch": "partial_update"}))]

dosage = [path("dosage-for-container", GetDosageForContainer().as_view()),
          path("set-amount-for-product", SetAmountForProduct().as_view())]

urlpatterns = [*company, *container, *status, *product, *dosage]
