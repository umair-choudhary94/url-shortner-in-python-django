from django.shortcuts import render
import pyshorteners

def index(request):
	if request.method == "POST":
		url = request.POST['url']
		result = pyshorteners.Shortener().tinyurl.short(url)
		context = {
			'url':result
		}
		return render(request,'shortner/shortner.html',context)
	return render(request,'shortner/shortner.html')
