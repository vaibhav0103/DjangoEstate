from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
	if request.method == 'POST':
		# Getting Form values
		listing_id		= request.POST['listing_id']
		listing 		= request.POST['listing']
		name			= request.POST['name']
		email			= request.POST['email']
		phone			= request.POST['phone']
		message			= request.POST['message']
		user_id			= request.POST['user_id']
		realtor_email	= request.POST['realtor_email']

		# If User inquiry for property already exist
		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
			if has_contacted:
				messages.error(request, 'You have already made an enquiry for this property')
				return redirect('/listings/'+listing_id)

		contact = Contact(listing=listing, listing_id=listing_id, 
			name=name, email=email, phone=phone, message=message,
			user_id=user_id)

		contact.save()

		# Send Mail to realtor
		# send_mail(
		# 	'Property Listing Inquiry', 
		# 	'message', 
		# 	'from@example.com', 
		# 	[realtor_email,], 
		# 	fail_silently=False,
		# 	)

		messages.success(request, 'Your request has been submiited, a realtor will get back to you soon')

		return redirect('/listings/'+listing_id)