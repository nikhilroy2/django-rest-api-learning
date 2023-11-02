from rest_framework.decorators import api_view
from django.db.models.query_utils import Q
from rest_framework import viewsets, generics
from rest_framework.response import Response

from app1.models import PersonalInfo
from .serializers import PersonalInfo_Serializer
from rest_framework import status



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def PersonalAPI(request, pk=None):
    # GET request to retrieve a list of all personal info
    if request.method == 'GET':
        if pk is not None:
            try:
                personal_info = PersonalInfo.objects.get(pk=pk)
                serializer = PersonalInfo_Serializer(personal_info)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PersonalInfo.DoesNotExist:
                return Response({'message': 'PersonalInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        
        personal_info = PersonalInfo.objects.all()
        serializer = PersonalInfo_Serializer(personal_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new personal info
    elif request.method == 'POST':
        serializer = PersonalInfo_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request to update an existing personal info
    elif request.method == 'PUT':
        if pk is not None:
            try:
                personal_info = PersonalInfo.objects.get(pk=pk)
                serializer = PersonalInfo_Serializer(personal_info, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except PersonalInfo.DoesNotExist:
                return Response({'message': 'PersonalInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Please provide a valid primary key for updating'}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request to delete an existing personal info
    elif request.method == 'DELETE':
        if pk is not None:
            try:
                personal_info = PersonalInfo.objects.get(pk=pk)
                personal_info.delete()
                return Response({'message': 'PersonalInfo deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except PersonalInfo.DoesNotExist:
                return Response({'message': 'PersonalInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Please provide a valid primary key for deleting'}, status=status.HTTP_400_BAD_REQUEST)
