import requests
from django.shortcuts import render
from .forms import DriverForm

# Base URL for the FastAPI endpoint
BASE_API_URL = 'https://search-fast-django-b5ee864cf0f8.herokuapp.com/'


def _extend_api(path):
    """
    Helper function to extend the base API URL with a given path.
    """
    return BASE_API_URL + path


def get_driver_data(request):
    """
    View function to handle GET requests for driver data.
    """

    # Create the form
    form = DriverForm(request.GET)
    if form.is_valid():
        # Get data from the form
        min_date = form.cleaned_data.get('startDate')
        max_date = form.cleaned_data.get('endDate')
        min_score = form.cleaned_data.get('minScore')
        max_score = form.cleaned_data.get('maxScore')
        limit = form.cleaned_data.get('limit')
        offset = form.cleaned_data.get('offset')
        # Send API request
        r = requests.get(
            _extend_api('/drivers'),
            params={
                'startDate': min_date,
                'endDate': max_date,
                'minScore': min_score,
                'maxScore': max_score,
                'limit': limit,
                'offset': offset
            }
        )
        # Process the response
        if r.status_code == 200:
            data = r.json().get('records', [])
        else:
            data = []
        # Send the data to the template
        context = {'drivers': data, 'form': form}
        return render(request, "driver_list.html", context)

    # If no GET request was made or the form is invalid, reload the page with an empty form
    return render(request, "driver_list.html", {'form': form})
