from django.shortcuts import render
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
import logging
from rest_framework.views import APIView

logger = logging.getLogger(__name__)

class HelloView(APIView):
    def get(self, request):
        try:
            logging.info('Calling Httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logging.info('Recieved Httpbin')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Uche'})

