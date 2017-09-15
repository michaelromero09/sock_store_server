from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib import messages
from ..admin_app.models import Admins
from .models import Products, Sizes, Product_Sizes, Designs

def get_all_products(request):
  products = Products.objects.all()
  data = serializers.serialize("json", products)
  return HttpResponse(data, content_type='application/json')


def get_product_by_id(id):
  return Products.objects.get(id = id)

def filter_product_by_id(id):
  return Products.objects.filter(id = id)

def add_product(name, dept, style, design, material, price, cost, image):
  return Products.objects.create(name = name, dept = dept, style = style, design = design, material = material, price = price, cost = cost, image = image)

def delete_product(id):
  print 'Deleting product with id: ' + str(id)
  Products.objects.get(id = id).delete()
  return 'Done-zo'

def get_sizes(post_data, product):
  if 'size_1' in post_data:
    size_id = int(post_data['size_1'])
    link_size_to_product(size_id, product.id)
  if 'size_2' in post_data:
    size_id = int(post_data['size_2'])
    link_size_to_product(size_id, product.id)
  if 'size_3' in post_data:
    size_id = int(post_data['size_3'])
    link_size_to_product(size_id, product.id)
  if 'size_4' in post_data:
    size_id = int(post_data['size_4'])
    link_size_to_product(size_id, product.id)
  if 'size_5' in post_data:
    size_id = int(post_data['size_5'])
    link_size_to_product(size_id, product.id)
  if 'size_6' in post_data:
    size_id = int(post_data['size_6'])
    link_size_to_product(size_id, product.id)
  if 'size_7' in post_data:
    size_id = int(post_data['size_7'])
    link_size_to_product(size_id, product.id)
  if 'size_8' in post_data:
    size_id = int(post_data['size_8'])
    link_size_to_product(size_id, product.id)
  if 'size_9' in post_data:
    size_id = int(post_data['size_9'])
    link_size_to_product(size_id, product.id)
  return 'Done done done'

def link_size_to_product(size_id, product_id):
  print 'LINKING SIZE TO PRODUCT'
  size = Sizes.objects.get(id = size_id)
  product = Products.objects.get(id = product_id)
  print size.size
  print product.name
  Product_Sizes.objects.create(size = size, product = product)
  return 'Done-zo'

def add_design(design):
  return Designs.objects.create(design = design)

# Create your views here.

def index(request):
  print 'IT\'S WORKING'
  # Designs.objects.create(design = 'Solid')
  print Designs.objects.all()
  products = get_all_products()
  sizes = Sizes.objects.all()
  print 'IMAGE RIGHT HERE'
  print type(products[0].image)
  for size in sizes:
    print size.size
    print size.product_sizes
  #   for relationship in size.product_sizes.all():
  #     print relationship
  # product_sizes = Product_Sizes.objects.all()
  # product_sizes = Product_Sizes.objects.all()
  # for relationship in product_sizes:
  #   print relationship.product.name + ':' + relationship.size.size
  # print sizes[0].products
  # print products[0].sizes
  context = {
    'products' : products
  }
  return render(request, 'manage_products/index.html', context)

def add_product_page(request):
  sizes = Sizes.objects.all()
  designs = Designs.objects.all()
  for size in sizes:
    print str(size.id) + ': ' + size.size
  context = {
    'sizes' : sizes,
    'designs' : designs,
  }
  return render(request, 'manage_products/add_product.html', context)

def add_product_to_db(request):
  print "It's working! It's working!"
  post_data = request.POST
  name = request.POST['name']
  dept = request.POST['dept']
  style = request.POST['style']
  design = request.POST['design']
  if design == 'other':
    new_design = request.POST['other_design']
    design = add_design(new_design)
  else:
    design = Designs.objects.get(id = design)
  material = request.POST['material']
  price = request.POST['price']
  cost = request.POST['cost']
  image = request.POST['image']
  print 'name: ' + name
  print 'dept: ' + dept
  print 'style: ' + style
  # print 'design: ' + design
  print 'material: ' + material
  print 'price: ' + price
  print 'cost: ' + cost
  product = add_product(name, dept, style, design, material, price, cost, image)
  get_sizes(post_data, product)
  return redirect(reverse('manage_products_index'))

def edit_product_page(request, id):
  sizes = Sizes.objects.all()
  designs = Designs.objects.all()
  for design in designs:
    print str(design.id) + ': ' + design.design
  products = filter_product_by_id(id)
  print products[0].name
  context = {
    'products' : products,
    'sizes' : sizes,
    'designs' : designs
  }
  return render(request, 'manage_products/edit_product.html', context)

def edit_product(request):
  post_data = request.POST
  id = request.POST['id']
  name = request.POST['name']
  dept = request.POST['dept']
  style = request.POST['style']
  design = request.POST['design']
  if design == 'other':
    new_design = request.POST['other_design']
    design = add_design(new_design)
  else:
    design = Designs.objects.get(id = design)
  material = request.POST['material']
  price = request.POST['price']
  cost = request.POST['cost']
  image = request.POST['image']
  product = get_product_by_id(id)
  product.name = name
  product.dept = dept
  product.style = style
  product.design = design
  product.material = material
  product.price = price
  product.cost = cost
  product.image = image
  product.save()
  Product_Sizes.objects.filter(product__id = id).delete()
  get_sizes(post_data, product)
  return redirect(reverse('manage_products_index'))

def delete_product_from_db(request):
  id = request.POST['id']
  print 'product id: ' + str(id)
  print delete_product(id)
  return redirect(reverse('manage_products_index'))