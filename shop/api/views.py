import redis
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from shop.models import Product
from .serializers import ProductSerializer
from user_app.permissions import IsAdminOrReadOnly


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # Assign the current user as the creator of the product
        serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        # Connect to Redis
        redis_connection = redis.Redis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
        )

        # Increment the query counter in Redis
        redis_key = f"product:{instance.id}:queries"
        redis_connection.incr(redis_key)

        cantidad_vistas = redis_connection.get(redis_key)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
