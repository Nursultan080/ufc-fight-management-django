from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm, FightForm, FighterForm, FightResultForm, WeightClassForm
from .models import Event, Fight, Fighter, FightResult, WeightClass


def save_list_view(request, model, form_class, template_name, context_name, redirect_name, queryset=None):
    form = form_class(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Запись добавлена.")
        return redirect(redirect_name)

    objects = queryset if queryset is not None else model.objects.all()
    return render(request, template_name, {"form": form, context_name: objects})


def edit_view(request, model, form_class, pk, title, back_url):
    obj = get_object_or_404(model, pk=pk)
    form = form_class(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Изменения сохранены.")
        return redirect(back_url)

    return render(request, "ufc_app/form_page.html", {"form": form, "title": title, "back_url": back_url})


def delete_view(request, model, pk, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    try:
        obj.delete()
        messages.success(request, "Запись удалена.")
    except ProtectedError:
        messages.error(request, "Нельзя удалить запись, пока на неё ссылаются другие таблицы.")
    return redirect(redirect_name)


def weight_classes_list(request):
    return save_list_view(request, WeightClass, WeightClassForm, "ufc_app/weight_classes.html", "weight_classes", "weight_classes_list")


def weight_class_update(request, pk):
    return edit_view(request, WeightClass, WeightClassForm, pk, "Редактировать весовую категорию", "weight_classes_list")


def weight_class_delete(request, pk):
    return delete_view(request, WeightClass, pk, "weight_classes_list")


def fighters_list(request):
    queryset = Fighter.objects.select_related("weight_class")
    return save_list_view(request, Fighter, FighterForm, "ufc_app/fighters.html", "fighters", "fighters_list", queryset)


def fighter_update(request, pk):
    return edit_view(request, Fighter, FighterForm, pk, "Редактировать бойца", "fighters_list")


def fighter_delete(request, pk):
    return delete_view(request, Fighter, pk, "fighters_list")


def events_list(request):
    return save_list_view(request, Event, EventForm, "ufc_app/events.html", "events", "events_list")


def event_update(request, pk):
    return edit_view(request, Event, EventForm, pk, "Редактировать турнир", "events_list")


def event_delete(request, pk):
    return delete_view(request, Event, pk, "events_list")


def fights_list(request):
    queryset = Fight.objects.select_related("event", "fighter_red", "fighter_blue", "weight_class")
    return save_list_view(request, Fight, FightForm, "ufc_app/fights.html", "fights", "fights_list", queryset)


def fight_update(request, pk):
    return edit_view(request, Fight, FightForm, pk, "Редактировать бой", "fights_list")


def fight_delete(request, pk):
    return delete_view(request, Fight, pk, "fights_list")


def results_list(request):
    queryset = FightResult.objects.select_related("fight", "winner", "fight__fighter_red", "fight__fighter_blue")
    return save_list_view(request, FightResult, FightResultForm, "ufc_app/results.html", "results", "results_list", queryset)


def result_update(request, pk):
    return edit_view(request, FightResult, FightResultForm, pk, "Редактировать результат", "results_list")


def result_delete(request, pk):
    return delete_view(request, FightResult, pk, "results_list")
