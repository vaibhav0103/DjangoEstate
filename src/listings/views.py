from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404

from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing

def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)

	# Pagination
	paginator 		= Paginator(listings, 6)
	page      		= request.GET.get('page')
	paged_listings 	= paginator.get_page(page)

	context = {
	"listings_page": "active",
	"listings": paged_listings,
	}
	return render(request, "listings/listings.html", context) 


def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk=listing_id)
	context = {
		'listing': listing,
	}
	return render(request, "listings/listing.html", context) 


def search(request):
	qs = Listing.objects.order_by('-list_date')

	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			qs = qs.filter(description__icontains=keywords)

	# City
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			qs = qs.filter(city__iexact=city)

	# State
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			qs = qs.filter(state__iexact=state)

	# Bedrooms
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			qs = qs.filter(bedrooms__lte=bedrooms)

	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			qs = qs.filter(price__lte=price)


	context = {
		"price_choices": price_choices,
		"bedroom_choices": bedroom_choices, 
		"state_choices": state_choices,
		"listings": qs,
		"values": request.GET
		}
	return render(request, "listings/search.html", context) 