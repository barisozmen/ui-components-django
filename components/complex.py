from django_components import register
from . import ComplexComponent


@register("datatable")
class Datatable(ComplexComponent):
    def get_context_data(self, columns=None, data=None, sortable=True, searchable=True, paginated=True, **kwargs):
        return {
            "columns": columns or [],
            "data": data or [],
            "sortable": sortable,
            "searchable": searchable,
            "paginated": paginated,
            "attrs": kwargs
        }


@register("wizard")
class Wizard(ComplexComponent):
    def get_context_data(self, steps=None, current_step=0, **kwargs):
        return {
            "steps": steps or [],
            "current_step": current_step,
            "total_steps": len(steps) if steps else 0,
            "attrs": kwargs
        }


@register("fileupload")
class Fileupload(ComplexComponent):
    def get_context_data(self, multiple=False, accept="*/*", max_size=None, drag_drop=True, **kwargs):
        return {
            "multiple": multiple,
            "accept": accept,
            "max_size": max_size,
            "drag_drop": drag_drop,
            "attrs": kwargs
        }


@register("calendar")
class Calendar(ComplexComponent):
    def get_context_data(self, events=None, view="month", selectable=True, **kwargs):
        return {
            "events": events or [],
            "view": view,
            "selectable": selectable,
            "attrs": kwargs
        }


@register("chart")
class Chart(ComplexComponent):
    def get_context_data(self, chart_type="bar", data=None, labels=None, options=None, **kwargs):
        return {
            "chart_type": chart_type,
            "data": data or [],
            "labels": labels or [],
            "options": options or {},
            "attrs": kwargs
        }


@register("kanban")
class Kanban(ComplexComponent):
    def get_context_data(self, columns=None, cards=None, **kwargs):
        return {
            "columns": columns or [],
            "cards": cards or [],
            "attrs": kwargs
        }


@register("statcard")
class Statcard(ComplexComponent):
    def get_context_data(self, title="", value="", icon=None, trend=None, trend_value=None, variant="primary", **kwargs):
        return {
            "title": title,
            "value": value,
            "icon": icon,
            "trend": trend,
            "trend_value": trend_value,
            "variant": variant,
            "attrs": kwargs
        }
