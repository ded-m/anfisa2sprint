from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
    ice_cream_list = (
        IceCream.objects.values(
            'id', 'title', 'description',
            )
        .filter(
            Q(is_on_main=True)
            &Q(is_published=True)
            |Q(title__contains='пломбир')
            &Q(is_published=True)
            )
        )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)