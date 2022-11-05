from django.shortcuts import render
from django.http import HttpResponse
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.

def index(request):
    return HttpResponse()

def ArtisteView(request):

    if request.method == 'GET':
        artiste = Artiste.objects.all()
        serializer = ArtisteSerializer(artiste, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'ARTISTE':
        data = JSONParser().parse(request)
        serializer = ArtisteSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def SongView(request):

    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'SONG':
        data = JSONParser().parse(request)
        serializer = SongSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def LyricView(request):

    if request.method == 'GET':
        lyric = Lyric.objects.all()
        serializer = LyricSerializer(lyric, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'LYRIC':
        data = JSONParser().parse(request)
        serializer = LyricSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)