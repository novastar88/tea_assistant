from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from pydantic_core import ValidationError
import products.models as models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import products.serializers as serializers
import products.pydantic_models as p_models
from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist


class ContainerViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.ContainerSerializer

    def get_queryset(self):
        return models.Container.objects.all()


class CompanyViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.CompanySerializer

    def get_queryset(self):
        return models.Company.objects.all()


class StatusViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.StatusSerializer

    def get_queryset(self):
        return models.Status.objects.all()


class ProductViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["rating", "status"]
    ordering_fields = ["rating", "last_used",
                       "status", "shop", "created_at", "amount"]

    def get_queryset(self):
        return models.Product.objects.all()


class GetDosageForContainer(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        req_data = request.data

        try:
            model_req = p_models.GetDosageForContainerPost(**req_data)
        except ValidationError as ve:
            return Response(status=422, data={"error": "invalid data structure", "details": str(ve)})

        try:
            container = models.Container.objects.get(pk=model_req.container_id)
            product = models.Product.objects.get(pk=model_req.product_id)
        except ObjectDoesNotExist as ve:
            return Response(status=404, data={"error": "object not found", "details": str(ve)})

        if product.amount == Decimal(0):
            return Response(status=422, data={"error": "unknown product dosage", "details": None})

        a1 = container.capacity * product.amount
        a2 = round(a1)

        if a2 == 0:
            a2 = 1

        return Response(status=200, data={"dosage": a2})


class SetAmountForProduct(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        req_data = request.data

        try:
            model_req = p_models.SetAmountForProductPost(**req_data)
        except ValidationError as ve:
            return Response(status=422, data={"error": "invalid data structure", "details": str(ve)})

        try:
            container = models.Container.objects.get(pk=model_req.container_id)
            product = models.Product.objects.get(pk=model_req.product_id)
        except ObjectDoesNotExist as ve:
            return Response(status=404, data={"error": "object not found", "details": str(ve)})

        a1 = Decimal(model_req.amount / container.capacity)

        product.amount = a1
        product.save()

        return Response(status=200, data={"dosage": a1, "details": "object saved"})
