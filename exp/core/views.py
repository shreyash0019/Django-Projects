from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from exp.serializers import TransactionSerializer
from rest_framework.decorators import api_view



@api_view()
def get_transaction(request):
    queryset=Transaction.objects.all()
    serializer=TransactionSerializer(queryset,many=True)

    return Response({
        "data": serializer.data
})

# Create your views here.
