from django.shortcuts import render
# from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = (
        # IceCream.objects.all()
        IceCream.objects.values(
            'id', 'title', 'description', 'price'
        )
        .filter(
            is_published=True,
            is_on_main=True,
            category__is_published=True
        )
        # .order_by('title')[1:4]
            # Q(is_on_main=True)
            # & Q(is_published=True)
            # | Q(title__contains='пломбир')
            # & Q(is_published=True)
            # )
    )
    # categories
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
