import requests
from django.shortcuts import render
from .forms import DriverForm

BASE_API_URL = 'http://api.example.com:5000'

def _extend_api(path):
    return BASE_API_URL + path

def get_driver_data(request):
    if request.method == 'GET':
        # Formu oluştur
        form = DriverForm(request.GET)
        if form.is_valid():
            # Formdan gelen verileri al
            min_date = form.cleaned_data.get('startDate')
            max_date = form.cleaned_data.get('endDate')
            min_score = form.cleaned_data.get('minScore')
            max_score = form.cleaned_data.get('maxScore')
            limit = form.cleaned_data.get('limit')
            offset = form.cleaned_data.get('offset')
            
            # API isteği gönder
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
            # Yanıtı işle
            if r.status_code == 200:
                data = r.json().get('records', [])
            else:
                data = []
            # Template'e veriyi gönder
            context = {'drivers': data, 'form': form}
            return render(request, "driver_list.html", context)
    else:
        # Hatalı formu işle
        form = DriverForm()
    # Eğer GET isteği gönderilmediyse veya form geçerli değilse, boş bir form ile sayfayı yeniden yükle
    return render(request, "driver_list.html", {'form': form})
