from django.shortcuts import render

def index_view(request):
    return render(request, 'third_task/game.html')

def shop_view(request):
    items = {
        "Игра A": "500 руб.",
        "Игра B": "1000 руб.",
        "Игра C": "1500 руб."
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart_view(request):
    return render(request, 'third_task/cart.html')

