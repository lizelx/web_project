from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
import random
from .models import Dict, Dict_custom, Customs


def db_get_word(request):
    words = Dict.objects.all()
    terms = []
    for i, item in enumerate(words):
        terms.append([i+1, item.angl.title(), item.rus.title()])
    term1 = random.choice(terms)
    return render(request, "term_list_random.html", context={"term1": term1})


def index(request):
    db_terms = 500
    words_all = len(Dict.objects.all())
    words_custom = len(Dict_custom.objects.all())
    users = len(Customs.objects.all())
    stats = {
        "terms_all": words_all,
        "terms_own": db_terms,
        "terms_added": words_custom,
        "users": users}
    return render(request, "index.html", stats)


def terms_list(request):
    words = Dict.objects.all()
    terms = []
    for i, item in enumerate(words):
        terms.append([i+1, item.angl.title(), item.rus.title()])
    return render(request, "term_list.html", context={"terms": terms})


def terms_list_sort(request):
    words = Dict.objects.all()
    terms = []
    for i, item in enumerate(words):
        terms.append([i+1, item.angl.title(), item.rus.title()])
    terms.sort(key=lambda x: (x[1]))
    return render(request, "term_list_sort.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def customs(request):
    return render(request, "customs.html")


def customs_request(request):
    if request.method == "POST":
        cache.clear()
        first_Name = request.POST.get("firstName")
        last_Name = request.POST.get("lastName")
        user_name = request.POST.get("username")
        e_mail = request.POST.get("email")
        c_ountry = request.POST.get("country")
        users = Customs.objects.all()
        users_list = []
        users_name = []
        for item in users:
            users_list.append(item.email)
            users_name.append(item.username)
        context = {"user": first_Name, "users": users_list}
        if e_mail in users_list:
            context["success"] = False
            context["comment"] = "Еmail уже занят"
        elif user_name in users_name:
            context["success"] = False
            context["comment"] = "Имя пользователя уже занято"
        else:
            context["success"] = True
            context["comment"] = "Вы зарегистрированы"
            Customs(firstName=first_Name, lastName=last_Name, username=user_name, email=e_mail, country=c_ountry).save()
        if context["success"]:
            context["success-title"] = ""
            return render(request, "customs_request.html", context)
        else:
            add_term(request)
            return render(request, "customs_request.html", context)


def customs_all(request):
    users = Customs.objects.all()
    users_info = []
    for item in users:
        users_info.append([item.firstName, item.lastName, item.country])
    return render(request, "customs_all.html", context={"users_info": users_info})


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Перевод не должен быть пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Слово не должно быть пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            Dict(angl=new_term, rus=new_definition).save()
            Dict_custom(angl=new_term).save()
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    db_terms = 500
    words_all = len(Dict.objects.all())
    words_custom = len(Dict_custom.objects.all())
    stats = {
        "terms_all": words_all,
        "terms_own": db_terms,
        "terms_added": words_custom}
    return render(request, "stats.html", stats)
