from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
 
from .filters import OrderFilter
from .serializers import OrderSerializer
from .models import Order, OrderStatus

# Create your views here.

# ************ Create an Order ************
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_an_order(request):
    try:
        user = request.user
        data = request.data

        Order.objects.create(
            user = user,
            title = data['title'],
            description = data['description'],
            price = data['price'],
        )
         
        return Response({'detail': 'Order create success'}, status=status.HTTP_201_CREATED)

    except ValidationError as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ************ Read an Order ************
@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()

    serializer = OrderSerializer(orders, many=True)

    if not serializer.data:
        return Response({'detail': 'No Order found'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'detail': 'Success', 'data': serializer.data})
    
# ************ Read an Order by Id ************
@api_view(['GET'])
def get_order_by_id(request, pk):
    order = get_object_or_404(Order, id=pk)

    serializer = OrderSerializer(order)

    return Response({'detail': 'Success', 'data': serializer.data})
    
# ************ Update an Order ************
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_order(request, pk):
    user = request.user
    data = request.data
    order = get_object_or_404(Order, id=pk, user=user)

    try:
        order.title = data['title']
        order.description = data['description']
        order.price = data['price']
        statusData = data['status']

        if (statusData == OrderStatus.PENDING):
            return Response({'detail': 'Can not change this status'},  status= status.HTTP_400_BAD_REQUEST)
        if (statusData == OrderStatus.CANCELLED):
            return Response({'detail': 'Can not change this status'},  status= status.HTTP_400_BAD_REQUEST)
        if (statusData == OrderStatus.PROCESSING):
            if(order.status == OrderStatus.PENDING):
                order.status = statusData
            else:
              return Response({'detail': 'Can not change this status'},  status= status.HTTP_400_BAD_REQUEST)
        elif (statusData == OrderStatus.SHIPPED):
            if(order.status == OrderStatus.PROCESSING):
                order.status = statusData
            else:
              return Response({'detail': 'Can not change this status'},  status= status.HTTP_400_BAD_REQUEST)
        elif (statusData == OrderStatus.DELIVERED):
            if(order.status == OrderStatus.SHIPPED):
                order.status = statusData
            else:
              return Response({'detail': 'Can not change this status'},  status= status.HTTP_400_BAD_REQUEST)
       
        order.save(update_fields=['title','description', 'price', 'status'])

        serializer = OrderSerializer(order) 

        return Response({'detail': 'Success', 'data': serializer.data})

    except ValidationError as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# ************ Delete an Order ************
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cancel_order(request, pk):
    user = request.user
    order = get_object_or_404(Order, id=pk, user=user)

    if(order.status == OrderStatus.PENDING):
        order.status = OrderStatus.CANCELLED
        order.save(update_fields=['status'])

        return Response({'detail': 'Cancel order is done'})
    
    return Response({'detail': 'You can\'t Cancel order'})

# ************ Search an Order ************
@api_view(['GET'])
def get_search_orders(request):
    filterset = OrderFilter(request.GET, queryset=Order.objects.all())
    count = filterset.qs.count()

    paginator = PageNumberPagination()
    paginator.page_size = 6

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = OrderSerializer(queryset, many=True)

    if not serializer.data:
        return Response({'detail': 'No Order found',}, status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response({'detail': 'Success', 'data': {'Order':serializer.data, 'per page' : 6, 'count': count}})
    