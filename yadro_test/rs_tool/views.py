from django.shortcuts import render
from django.views import View
from .forms import CreateDocForm
import json
from random import randint
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializer import ValidateRequestDataSerializer, ContentSerializer
from yadro_test.settings import CONF_BASE_PATH


class CreateDoc(View):

    def get(self, request):
        form = CreateDocForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = CreateDocForm(request.POST)

        json_data = {
            'type': 'page',
            'title': request.POST['doc_title'],
            'space': {
                'key': request.POST['space_name'],
            },
            'body': {
                'storage': {
                    'value': request.POST['doc_text'],
                    'representation': 'storage',
                },
            },
        }

        try:
            response = requests.post(
            CONF_BASE_PATH + 'rest/api/content/',
            headers={'Content-Type': 'application/json'},
            json=json_data,
            auth=(request.POST['user_name'], request.POST['user_password']),
            )

            if response.status_code == 201:
                content_id = response.get('id')

        except Exception as err:
            print(err)
            content_id = randint(0, 100)

        return render(request, 'index.html', {'form': form, 'id': content_id})


class GetContent(APIView):
    
    def get(self, request):
        input = ValidateRequestDataSerializer(data=request.GET)
        if input.is_valid():
            conf_api = f"{CONF_BASE_PATH}rest/api/content?spaceKey={input.data['space_name']}&title={input.data['page_name']}"
            try:
                response_data = requests.get(conf_api).json()
            except Exception as err:
                print('Ошбка доступа к API', err)
                response_data = None
            content_serializer = ContentSerializer(data=response_data)
            if content_serializer.is_valid():
                pass
                return Response(data=content_serializer.data)
        
        return Response(data=json.dumps({'content_data':'No data'}))
    