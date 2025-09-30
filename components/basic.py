from django_components import register
from . import BasicComponent


@register("button")
class Button(BasicComponent):
    def get_context_data(self, variant="primary", size="md", disabled=False, type="button", **kwargs):
        return {
            "variant": variant,
            "size": size,
            "disabled": disabled,
            "type": type,
            "attrs": kwargs
        }


@register("badge")
class Badge(BasicComponent):
    def get_context_data(self, variant="primary", pill=False, **kwargs):
        return {
            "variant": variant,
            "pill": pill,
            "attrs": kwargs
        }


@register("alert")
class Alert(BasicComponent):
    def get_context_data(self, variant="info", dismissible=False, **kwargs):
        return {
            "variant": variant,
            "dismissible": dismissible,
            "attrs": kwargs
        }


@register("avatar")
class Avatar(BasicComponent):
    def get_context_data(self, src=None, alt="", size="md", shape="circle", **kwargs):
        return {
            "src": src,
            "alt": alt,
            "size": size,
            "shape": shape,
            "attrs": kwargs
        }


@register("spinner")
class Spinner(BasicComponent):
    def get_context_data(self, size="md", variant="primary", type="border", **kwargs):
        return {
            "size": size,
            "variant": variant,
            "type": type,
            "attrs": kwargs
        }


@register("divider")
class Divider(BasicComponent):
    def get_context_data(self, text=None, **kwargs):
        return {
            "text": text,
            "attrs": kwargs
        }


@register("breadcrumb")
class Breadcrumb(BasicComponent):
    def get_context_data(self, items=None, **kwargs):
        return {
            "items": items or [],
            "attrs": kwargs
        }


@register("tooltip")
class Tooltip(BasicComponent):
    def get_context_data(self, text="", placement="top", **kwargs):
        return {
            "text": text,
            "placement": placement,
            "attrs": kwargs
        }
