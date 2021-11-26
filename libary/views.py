from django.shortcuts import render, redirect
from .forms import BookForm
from .models import *

# Create your views here.

def home(request):
  books = Book.objects.all()

  dados = {
    'books': books,
  }

  return render(request, "index.html", dados)

def edit(request, id):
  book = Book.objects.get(id=id)

  if request.method == 'POST':
    if book:
      form = BookForm(request.POST, instance = book)
    else:
      form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      print(request, "Produto editado com sucesso!")
    else:
      print(request, "Erro ao editar o produto!")

    args = {
      'form': form
    }

    return redirect('home')
  else:
    if book:
      form = BookForm(instance = book)
      args = {}
      args.update(request)
    else:
      form = BookForm()

    args = {
      'form': form
    }
    
    return render(request, 'edit_book.html', args)


def register(request):
  if request.method=='POST':
    form = BookForm(request.POST)

    if form.is_valid():
      try:
        instance = form.save(commit=False)
        instance.save()
        return redirect('home')
      except:
        print(request, "Error to register a new book!")

  form = BookForm()
  dados = {"form": form}

  return render(request, "register_book.html", dados)

def delete(request, id):
  book = Book.objects.get(id=id)
  
  if book:
    book.delete()
    return redirect('home')
  else:
    return redirect('home')
  