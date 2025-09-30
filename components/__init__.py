from django_components.component import Component


class BasicComponent(Component):
    def get_template_name(self, context, **kwargs):
        return 'basic/' + self.__class__.__name__.lower() + ".html"


class ModerateComponent(Component):
    def get_template_name(self, context, **kwargs):
        return 'moderate/' + self.__class__.__name__.lower() + ".html"


class ComplexComponent(Component):
    def get_template_name(self, context, **kwargs):
        return 'complex/' + self.__class__.__name__.lower() + ".html"
