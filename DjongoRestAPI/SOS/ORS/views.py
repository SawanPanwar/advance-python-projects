from django.http.response import JsonResponse
from rest_framework import status
from .models import Marksheet
from .serializers import MarksheetSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def add_marksheet(request):
    if request.method == 'POST':
        serializer = MarksheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_marksheet(request, pk):
    marksheet = get_object_or_404(Marksheet, pk=pk)
    serializer = MarksheetSerializer(marksheet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_marksheets(request):
    if request.method == 'GET':
        marksheets = Marksheet.objects.all()
        serializer = MarksheetSerializer(marksheets, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def delete_marksheet(request, pk):
    marksheet = get_object_or_404(Marksheet, pk=pk)
    marksheet.delete()
    return JsonResponse({'message': 'Marksheet deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
