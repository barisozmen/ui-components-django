from django_components import register
from django_components.component import Component
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


@register("crispy_form")
class CrispyForm(Component):
    template_name = "forms/crispy_form.html"
    
    def get_context_data(self, form, form_id=None, method="post", action="", **kwargs):
        if not hasattr(form, 'helper'):
            form.helper = FormHelper()
            form.helper.form_method = method
            form.helper.form_action = action
            if form_id:
                form.helper.form_id = form_id
        
        return {
            "form": form,
            "attrs": kwargs
        }


@register("form_field")
class FormField(Component):
    template_name = "forms/field.html"
    
    def get_context_data(self, field, show_label=True, **kwargs):
        return {
            "field": field,
            "show_label": show_label,
            "attrs": kwargs
        }


@register("inline_form")
class InlineForm(Component):
    template_name = "forms/inline_form.html"
    
    def get_context_data(self, form, action="", submit_text="Submit", **kwargs):
        return {
            "form": form,
            "action": action,
            "submit_text": submit_text,
            "attrs": kwargs
        }
