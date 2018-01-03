# -*- coding=utf-8 -*-
import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ArticleSerializer
from .models import Article


class ArticleViewSets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data['article'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {'data':serializer.data, 'status':status.HTTP_201_CREATED, 'msg':"success"}
        return HttpResponse(json.dumps(response),{"contentType":'application/json'})

def getConfig(request):
    with open('blogBackend/config.json') as json_file:
        # all_the_text = json_file.read()
        data = json.load(json_file)
    print data
    return HttpResponse(json.dumps(data),{"contentType":'application/json'})