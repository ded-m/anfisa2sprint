from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream, Category


def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
    ice_cream_list = (
        # IceCream.objects.all()
        IceCream.objects.values(
            'id', 'title', 'description', 'category__title'
            )
        .filter(is_published=True, is_on_main=True)
        .order_by('title')[1:4]
            # Q(is_on_main=True)
            # & Q(is_published=True)
            # | Q(title__contains='пломбир')
            # & Q(is_published=True)
            # )
        )
    # categories
    context = {
        'ice_cream_list': ice_cream_list,
        # 'categories': categories
    }
    return render(request, template, context)
