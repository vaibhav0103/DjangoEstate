from django.shortcuts import render


def index(request):
	context = {"listings_page": "active"}
	return render(request, "listings/listings.html", context) 


def listing(request):
	return render(request, "listings/listing.html") 


def search(request):
	return render(request, "listings/search.html") 