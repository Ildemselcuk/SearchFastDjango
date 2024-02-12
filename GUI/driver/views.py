from django.shortcuts import render
from django.views import View
import requests

BASE_API_URL = 'http://localhost:5000/'


def _extend_api(path):
    return BASE_API_URL + path


def get(self, request, *args, **kwargs):
    # Query parameters
    min_date = request.GET.get('minDate')
    max_date = request.GET.get('maxDate')
    min_score = request.GET.get('minScore')
    max_score = request.GET.get('maxScore')
    limit = int(request.GET.get('limit', 50))
    offset = int(request.GET.get('offset', 0))
    # API request
    r = requests.get(
        _extend_api('/drivers'),
        params={
            'startDate': min_date,
            'endDate': max_date,
            'minScore': min_score,
            'maxScore': max_score,
            'limit': limit,
            'offset': offset
        })
    # Response handling
    if r.status_code == 200:
        data = r.json().get('records', [])
    else:
        data = []
    # Render template
    context = {'drivers': data}
    return render(request, "driver_list.html", context)
