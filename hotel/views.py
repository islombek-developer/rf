from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product,Taom
from .forms import CreatProduct

def home(request):
    products = Product.objects.all().order_by('name')
    categories = Category.objects.all()

    return render(request, 'home.html', context={"products": products, "cats": categories})

def salom(request):
    products = Product.objects.all().order_by('name')
    categories = Category.objects.all()

    return render(request, 'salom.html', context={"products": products, "cats": categories})

def single(request):
    products = Product.objects.all().order_by('name')
    categories = Category.objects.all()
    return render(request, 'single.html', context={"products": products, "cats": categories})



def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all().order_by('name')
    categories = Category.objects.all()
    return render(request, 'room.html', context={"products": products, "cats": categories})

def batafsil(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    return render(request, 'about.html', context={"product": product, "cats": categories})

def create(request):
    form = CreatProduct()
    if request.method == 'POST':
        form = CreatProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', context={"form": form})

def update(request, id):
    product = Product.objects.get(id=id)
    form = CreatProduct(instance=product)
    if request.method == 'POST':
        form = CreatProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', context={"form": form})

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')

def alik(request,id):
    cat = get_object_or_404(Product, id=id)
    products = cat.taom.all().order_by('name')
    categories = Product.objects.all()
    return render(request, 'room1.html', context={"products": products, "cats": categories})

def singlet(request):
    products = Taom.objects.all()
    categories = Product.objects.all().order_by('name')
    return render(request, 'batafsil.html', context={"products": products, "cats": categories})

