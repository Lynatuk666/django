from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}

def home_view(request):
    template_name = "calculator/home.html"
    reciepts = {
        "Невкусный омлет": reverse("omlet"),
        "Мак & Чиз": reverse("pasta"),
        "Бутерброд, со всяким": reverse("buter")
    }
    context = {
        "pages": reciepts
    }
    return render(request, template_name, context)

def omlet_view(request):  # если servings  нам не пришел в запросе, то он равняется 1
    servings = 1  # тут хочется оптимизировать количество кода, но пока что так
    if request.GET:  # мб вынести обработку ингридиентов в отдельную функцию
        servings = int(request.GET["servings"])  # или можно переписать с использованием map()
    template_name = 'calculator/index.html'
    inf = {}
    for key, value in DATA["omlet"].items():
        inf[f'{key}'] = f"{value * servings}"
    context = {"recipe": inf}
    return render(request, template_name, context)


def buter_view(request):
    servings = 1
    if request.GET:
        servings = int(request.GET["servings"])
    template_name = 'calculator/index.html'
    inf = {}
    for key, value in DATA["buter"].items():
        inf[f'{key}'] = f"{value * servings}"
    context = {"recipe": inf}
    return render(request, template_name, context)


def pasta_view(request):
    servings = 1
    if request.GET:
        servings = int(request.GET["servings"])
    template_name = 'calculator/index.html'
    inf = {}
    for key, value in DATA["pasta"].items():
        inf[f'{key}'] = f"{value * servings}"
    context = {"recipe": inf}

    return render(request, template_name, context)


