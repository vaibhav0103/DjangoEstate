from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor


def index(request):

	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {
				"home_page": "active",
				"listings": listings,
				"price_choices": price_choices, 
				"bedroom_choices": bedroom_choices, 
				"state_choices": state_choices,

			}
	return render(request, 'pages/index.html', context)


def about(request):
	# Get all Realtors
	realtors = Realtor.objects.order_by('-hire_date')

	# Get MVP Realtors
	mvp_realtors = Realtor.objects.filter(is_mvp=True)

	context = {
		"about_page": "active",
		"realtors": realtors,
		"mvp_realtors": mvp_realtors
		}
	return render(request, 'pages/about.html', context)