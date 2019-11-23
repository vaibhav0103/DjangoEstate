from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def register(request):
	if request.method == 'POST':
		# Get Form values
		first_name	= request.POST['first_name']
		last_name	= request.POST['last_name']
		username	= request.POST['username']
		email		= request.POST['email']
		password	= request.POST['password']
		password2	= request.POST['password2']

		# Validations

		# Check passwords match
		if password == password2:
			# Check Username
			if User.objects.filter(username=username).exists():
				messages.error(request, 'That username is taken')
				return redirect('register')
			else:
				# Check Email
				if User.objects.filter(email=email).exists():
					messages.error(request, 'The email already exists')
					return redirect('register')
				else:
					# Create User
					user = User.objects.create_user(username=username, email=email, 
						password=password, first_name=first_name, last_name=last_name)

					# To directly Login user after registered
					# auth.login(request.user)
					# messages.success(request, 'You are now logged in')
					# return redirect('index')

					# only register and send to login
					user.save()
					messages.success(request, 'You have registered successfully and can now log in')
					return redirect('login')

		else:
			messages.error(request, 'Passwords do not match')
			return redirect('register')

	else:
		context = {
			"register_page": "active",
		}
		return render(request, 'accounts/register.html', context)


def login(request):

	if request.method == 'POST':
		# get username and password
		username = request.POST['username']
		password = request.POST['password']

		# authenticate user
		user = auth.authenticate(username=username, password=password)

		# login if authenticated
		if user is not None:
			auth.login(request, user)
			messages.success(request, 'You are now logged in')
			return redirect('dashboard')
		else:
			# redirect
			messages.error(request, 'Invlaid Credentials')
			return redirect('login')

	else:
		context = {
			"login_page": "active",
		}
		return render(request, 'accounts/login.html', context)


def logout(request):
	auth.logout(request)
	messages.success(request, 'You are now logged out')
	return redirect('index')


def dashboard(request):

	user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

	context = {
		"dashboard_page": "active",
		"contacts": user_contacts
	}
	return render(request, 'accounts/dashboard.html', context)