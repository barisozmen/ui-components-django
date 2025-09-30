from django_components import register
from . import ModerateComponent


@register("card")
class Card(ModerateComponent):
    def get_context_data(self, title=None, subtitle=None, img_top=None, img_bottom=None, **kwargs):
        return {
            "title": title,
            "subtitle": subtitle,
            "img_top": img_top,
            "img_bottom": img_bottom,
            "attrs": kwargs
        }


@register("modal")
class Modal(ModerateComponent):
    def get_context_data(self, id, title=None, size="md", centered=False, scrollable=False, **kwargs):
        return {
            "id": id,
            "title": title,
            "size": size,
            "centered": centered,
            "scrollable": scrollable,
            "attrs": kwargs
        }


@register("dropdown")
class Dropdown(ModerateComponent):
    def get_context_data(self, label="Dropdown", variant="primary", items=None, split=False, **kwargs):
        return {
            "label": label,
            "variant": variant,
            "items": items or [],
            "split": split,
            "attrs": kwargs
        }


@register("tabs")
class Tabs(ModerateComponent):
    def get_context_data(self, items=None, active=0, style="tabs", **kwargs):
        return {
            "items": items or [],
            "active": active,
            "style": style,
            "attrs": kwargs
        }


@register("accordion")
class Accordion(ModerateComponent):
    def get_context_data(self, id, items=None, always_open=False, **kwargs):
        return {
            "id": id,
            "items": items or [],
            "always_open": always_open,
            "attrs": kwargs
        }


@register("pagination")
class Pagination(ModerateComponent):
    def get_context_data(self, current_page=1, total_pages=1, page_url="?page=", **kwargs):
        return {
            "current_page": current_page,
            "total_pages": total_pages,
            "page_url": page_url,
            "attrs": kwargs
        }


@register("progress")
class Progress(ModerateComponent):
    def get_context_data(self, value=0, max_value=100, variant="primary", striped=False, animated=False, **kwargs):
        return {
            "value": value,
            "max_value": max_value,
            "variant": variant,
            "striped": striped,
            "animated": animated,
            "percentage": int((value / max_value) * 100) if max_value > 0 else 0,
            "attrs": kwargs
        }


@register("toast")
class Toast(ModerateComponent):
    def get_context_data(self, title=None, delay=5000, variant="info", autohide=True, **kwargs):
        return {
            "title": title,
            "delay": delay,
            "variant": variant,
            "autohide": autohide,
            "attrs": kwargs
        }


@register("navbar")
class Navbar(ModerateComponent):
    def get_context_data(self, brand=None, brand_url="/", items=None, variant="dark", expand="lg", **kwargs):
        return {
            "brand": brand,
            "brand_url": brand_url,
            "items": items or [],
            "variant": variant,
            "expand": expand,
            "attrs": kwargs
        }
