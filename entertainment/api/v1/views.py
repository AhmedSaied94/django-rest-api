from django.shortcuts import render
from rest_framework import response
from entertainment.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import *

# Create your views here.
@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()
    ser_movies = MovieSerializer(instance=movies, many= True)

    #------------------------------------------------------#
    for i in ser_movies.data:
        for l in i['casts']:
            cn = Cast.objects.get(id=str(l))
            i['casts'][i['casts'].index(l)]=str(cn)
        for l in i['catigories']:
            cn = Catigorie.objects.get(id=str(l))
            i['catigories'][i['catigories'].index(l)]=str(cn)
    #-------------------------------------------------------------#
    
    return Response(data=ser_movies.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_details(request, pk):
    movies = Movie.objects.filter(id=pk)
    if movies.exists():
        movie = movies.first()
        ser_movies = MovieSerializer(instance=movie)

        #---------------------------------------#
        for l in ser_movies.data['casts']:
            cn = Cast.objects.get(id=str(l))
            ser_movies.data['casts'][ser_movies.data['casts'].index(l)]=str(cn)
        for l in ser_movies.data['catigories']:
            cn = Catigorie.objects.get(id=str(l))
            ser_movies.data['catigories'][ser_movies.data['catigories'].index(l)]=str(cn)
        return Response(data=ser_movies.data, status=status.HTTP_200_OK)
    else: return Response(data={'error':"query hadn't founded"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def movie_create(request):

    if request.method =='POST':
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(data=[movie.data['id'], movie.data['title']], status=status.HTTP_200_OK)
        else:
            return Response(data=movie.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def movie_delete(request, pk):
    response = {}

    try:
        movie = Movie.objects.get(id=pk)
        movie.delete()
        response['data'] = {'message':'deleted success'}
        response['status']= status.HTTP_200_OK
    except Exception as e :
        response['data'] = {'message':f"error while delete {e}"}
        response['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(**response)

@api_view(['PUT', 'PATCH'])
def movie_update(request, pk):

    try:
        movie = Movie.objects.get(id=pk)
    except Exception as e:
        return Response(data={'message':f"error while update {e}"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method=='PUT':
        ser_movie = MovieSerializer(data=request.data, instance=movie)

    elif request.method == 'PATCH':
        ser_movie = MovieSerializer(data=request.data, instance=movie, partial=True)

    if ser_movie.is_valid():
        ser_movie.save()
        return Response(data=ser_movie.data['title'], status=status.HTTP_200_OK)
    return Response(data=ser_movie.errors, status=status.HTTP_400_BAD_REQUEST)


