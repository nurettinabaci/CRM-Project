import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .decorators import unauthenticated_user, authenticated_user
from .models import Customer
from .forms import CreateUserForm, CustomerForm

logger = logging.getLogger(__name__)


@authenticated_user
def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('New customer addsced')
            return redirect('/')
        else:
            logger.warning('New customer operation failed')

    context = {'form': form}
    return render(request, "create_customer.html", context)


@authenticated_user
def update_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            logger.info('Customer updated successfully.')
            return redirect(reverse("index"))
        else:
            logger.warning("Customer couldn't updated")

    context = {'form': form}
    return render(request, 'update_customer.html', context)


@authenticated_user
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == "POST":
        customer.delete()
        logger.info('Customer deleted successfully.')
        return redirect(reverse("index"))
    context = {'item': customer}
    return render(request, 'delete_customer.html', context)


@authenticated_user
def index(request):
    customers = Customer.objects.all()
    # customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'index.html', context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'You successfuly created an '
                             f'account for {username}.')
            logger.info(f'New user {username} is created.')
            return redirect('login')
        else:
            logger.warning("New user couldn't is created.")
    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.warning(f"User {username} logged in.")
            return redirect("index")

        else:
            messages.info(request, 'Username or password incorrect!')
            logger.warning("User login failed.")

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
