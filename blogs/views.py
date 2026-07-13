from django.shortcuts import render, redirect, get_object_or_404
from.models import Blog, Category


def posts_by_category(request, category_id):
    # Fetch the category with the id category_id
    post = Blog.objects.filter(status='Published', category=category_id)
    
    # # Use try/except when you want to do some custom action if category does not exist
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    # # Use get_object_404 when you want to show 404 error when category does not exist.
    # category = get_object_or_404(Category, pk=category_id)
    
    context={
        'post':post,
        'category':category,
    }
    return render(request, 'posts_by_category.html', context)