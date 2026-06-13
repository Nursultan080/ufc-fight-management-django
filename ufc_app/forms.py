from django import forms

from .models import Event, Fight, Fighter, FightResult, WeightClass


class BaseStyledForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault("class", "checkbox")
            else:
                widget.attrs.setdefault("class", "control")


class WeightClassForm(BaseStyledForm):
    class Meta:
        model = WeightClass
        fields = ["name", "max_weight_lb"]


class FighterForm(BaseStyledForm):
    class Meta:
        model = Fighter
        fields = ["full_name", "nickname", "country", "weight_class", "wins", "losses"]


class EventForm(BaseStyledForm):
    class Meta:
        model = Event
        fields = ["title", "event_date", "city", "country"]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }


class FightForm(BaseStyledForm):
    class Meta:
        model = Fight
        fields = ["event", "fighter_red", "fighter_blue", "weight_class", "rounds_scheduled"]


class FightResultForm(BaseStyledForm):
    class Meta:
        model = FightResult
        fields = ["fight", "winner", "method", "round_finished", "time_finished"]
