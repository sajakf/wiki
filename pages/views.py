from django.shortcuts import render
from .models import page

# Create your views here.
def test_api_view(request):
	response = requests.get(url)
	url = "https://api.github.com/events"
	#return JsonResponse(response.json()), safe=False
	context = {
		"response": response.json(),

	}
	return render(requests, 'pretty.html', context)

def details_view(request, page_id):
	context = {
		"details": page.objects.get(id=page_id),
		

		}

	return render(request, 'detail.html', context)

def list_view(request):
	context = {
	"list": page.objects.all(),
	
	
		}

	return render(request, 'list.html', context)