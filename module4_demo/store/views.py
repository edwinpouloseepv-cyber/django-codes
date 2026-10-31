from django.http import HttpResponse
from django.shortcuts import render


def home(request):
#     return HttpResponse("<h1>Hello Django</h1>")
    # return render(request, "store/home.html")
    print("Request method:", request.method)
    user_agent = request.headers.get("User-Agent")
    context = {
            "message": "This is my first Django website",
            "user_agent": user_agent
    }

    return render(request, "store/home.html", context)
# def products(request):

#     items = [
#         {
#             "name": "Laptop",
#             "price": 55000
#         },
#         {
#             "name": "Phone",
#             "price": 22000
#         },
#         {
#             "name": "Mouse",
#             "price": 500
#         }
#     ]
def products(request):

    items = [
        {
            "name": "Laptop",
            "price": 55000
        },
        {
            "name": "Phone",
            "price": 22000
        },
        {
            "name": "Mouse",
            "price": 500
        }
    ]

    q = request.GET.get("q")

    if q:
        items = [
            product for product in items
            if q.lower() in product["name"].lower()
        ]

    context = {
        "products": items,
        "q": q
    }

    return render(
        request,
        "store/products.html",
        context
    )

    context = {
        "products": items
    }

    return render(request, "store/products.html", context)