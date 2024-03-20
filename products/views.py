from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Comment
from .forms import CommentForm
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            messages.success(request, "You successfully left a comment!")
            return redirect('product_detail', product_id=product.id)
    else:
        comment_form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def delete_comment(request, comment_id, product_id):
    comment = get_object_or_404(Comment, id=comment_id, product_id=product_id)

    if request.user != comment.user:
        messages.error(request, "You don't have permission to delete this comment.")
        return redirect('product_detail', product_id=product_id)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Your comment was successfully deleted!")
        return redirect('product_detail', product_id=product_id)
    else:
        context = {
            'comment': comment,
            'product_id': product_id
        }
    return render(request, 'products/delete_comment.html', context)

@login_required
def edit_comment(request, comment_id, product_id):
    comment = get_object_or_404(Comment, id=comment_id, product_id=product_id)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed"
                                     " to edit this comment.")
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully edited your comment!")
            return redirect('product_detail', product_id=product_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'products/edit_comment.html', {'form': form,
                                                 'comment': comment, 
                                                 'product_id': comment.product.id})