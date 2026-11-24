from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Item
from .forms import ItemForm, CustomUserCreationForm


def home(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    items = Item.objects.all().order_by('-date')

    if query:
        items = items.filter(title__icontains=query)

    if category:
        items = items.filter(category=category)

    # pagination
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # dynamic counts
    lost_count = Item.objects.filter(category='Lost').count()
    found_count = Item.objects.filter(category='Found').count()

    return render(request, 'home.html', {
        'items': page_obj,
        'query': query,
        'category': category,
        'lost_count': lost_count,
        'found_count': found_count
    })


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('home')
    else:
        form = ItemForm()

    return render(request, 'add_item.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('/accounts/login/')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def edit_item(request, id):
    item = get_object_or_404(Item, id=id, user=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form})


@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id, user=request.user)

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    return render(request, 'delete_item.html', {'item': item})