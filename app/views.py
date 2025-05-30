from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Author
from .forms import ItemForm, AuthorForm, PublisherForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'app/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'app/item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'item': item})

# ============================================ CRUD Author

def autor_list(request):
    autor = Author.objects.all()
    return render(request, 'app/item_list.html', {'autor': autor})

def autor_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = AuthorForm()
    return render(request, 'app/item_form.html', {'autor': autor})

def autor_update(request, pk):
    autor = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = AuthorForm(instance=autor)
    return render(request, 'app/item_form.html', {'autor': autor})

def autor_delete(request, pk):
    autor = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'autor': autor})

# ============================================ CRUD Publisher

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'app/publisher_list.html', {'publishers': publishers})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'app/item_form.html', {'form': form, 'title': 'Novo Publisher'})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'app/publisher_form.html', {'form': form})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'app/publisher_confirm_delete.html', {'publisher': publisher})