from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render




class SongList(APIView):
    
    def get(self,request):
        """Get a song by request from client, allow multiple values to return based on user criteria"""
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def post(self,request):
        """POST results to user with HTTP status messages upon success or fail"""
        try:
            serializer = SongSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetail(APIView):
        
    def get_song(self, pk):
        """Try to get a song by ID, if ID does not exist, then HTTP 404"""
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk):
        """GET by ID endpoint"""
        song=self.get_song(pk)
        serializer=SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        """PUT to update by ID endpoint"""
        try:
            song=self.get_song(pk)
            serializer = SongSerializer(song, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        """DELETE by ID endpoint"""
        song=self.get_song(pk)
        song.delete()
        return Response(song.title, status=status.HTTP_200_OK)



class SongLikes(APIView):
    
    def get_song(self,pk):
        try: 
            return Song.object(pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        try:
            song = self.get_object(pk)
            serializer = SongSerializer(song)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        """PATCH to increment Song likes counter"""
        try:
            song= self.get_song(pk)
            data = {"likes": song.likes + int(1)}
            serializer = SongSerializer(song, data=data, partial=True)
            if serializer.is_valid:
                serializer.save()
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)