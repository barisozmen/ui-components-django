# Component Usage Guide

## Quick Start

```django
{% load component_tags %}

{% component "button" variant="primary" %}
  Click Me
{% endcomponent %}
```

## Basic Components

### Button
```django
{% component "button" variant="primary" size="lg" type="submit" %}
  Submit Form
{% endcomponent %}

<!-- Available variants: primary, secondary, success, danger, warning, info, light, dark -->
<!-- Available sizes: sm, md, lg -->
```

### Badge
```django
{% component "badge" variant="success" pill=True %}
  Active
{% endcomponent %}
```

### Alert
```django
{% component "alert" variant="warning" dismissible=True %}
  Warning: Please review your input!
{% endcomponent %}
```

### Avatar
```django
{% component "avatar" src="/media/avatar.jpg" size="lg" shape="circle" alt="John Doe" %}
{% endcomponent %}

<!-- Without image (shows initials) -->
{% component "avatar" size="md" alt="John Doe" %}
  JD
{% endcomponent %}
```

### Spinner
```django
{% component "spinner" variant="primary" size="md" type="border" %}
{% endcomponent %}
```

### Breadcrumb
```django
{% component "breadcrumb" items=breadcrumb_items %}
{% endcomponent %}

<!-- In views.py -->
breadcrumb_items = [
    {'label': 'Home', 'url': '/'},
    {'label': 'Products', 'url': '/products/'},
    {'label': 'Widget'}  # Last item (no URL)
]
```

## Moderate Components

### Card
```django
{% component "card" title="Card Title" subtitle="Subtitle" %}
  <p>Card body content goes here.</p>
  <a href="#" class="btn btn-primary">Action</a>
{% endcomponent %}

<!-- With images -->
{% component "card" title="Product" img_top="/static/product.jpg" %}
  Product description
{% endcomponent %}
```

### Modal
```django
<!-- Button to trigger -->
<button data-bs-toggle="modal" data-bs-target="#myModal">Open</button>

<!-- Modal component -->
{% component "modal" id="myModal" title="My Modal" size="lg" centered=True %}
  <p>Modal content here</p>
  
  {% slot "footer" %}
    <button class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
    <button class="btn btn-primary">Confirm</button>
  {% endslot %}
{% endcomponent %}

<!-- Available sizes: sm, md, lg, xl -->
```

### Dropdown
```django
{% component "dropdown" label="Actions" variant="primary" items=dropdown_items %}
{% endcomponent %}

<!-- In views.py -->
dropdown_items = [
    {'label': 'Edit', 'url': '/edit/'},
    {'label': 'Delete', 'url': '/delete/'},
    {'divider': True},
    {'header': 'More Options'},
    {'label': 'Archive', 'url': '/archive/', 'disabled': True}
]
```

### Tabs
```django
{% component "tabs" items=tab_items active=0 style="tabs" %}
{% endcomponent %}

<!-- In views.py -->
tab_items = [
    {'label': 'Overview', 'content': '<p>Overview content</p>'},
    {'label': 'Settings', 'content': '<p>Settings content</p>'},
    {'label': 'History', 'content': '<p>History content</p>'}
]

<!-- Available styles: tabs, pills -->
```

### Accordion
```django
{% component "accordion" id="myAccordion" items=accordion_items always_open=False %}
{% endcomponent %}

<!-- In views.py -->
accordion_items = [
    {'title': 'Section 1', 'content': '<p>Content 1</p>', 'show': True},
    {'title': 'Section 2', 'content': '<p>Content 2</p>', 'show': False}
]
```

### Progress Bar
```django
{% component "progress" value=65 max_value=100 variant="success" striped=True animated=True %}
{% endcomponent %}

<!-- Custom text -->
{% component "progress" value=75 variant="info" %}
  75% Complete
{% endcomponent %}
```

### Navbar
```django
{% component "navbar" brand="MyApp" brand_url="/" items=nav_items variant="dark" expand="lg" %}
{% endcomponent %}

<!-- In views.py -->
nav_items = [
    {'label': 'Home', 'url': '/', 'active': True},
    {'label': 'About', 'url': '/about/'},
    {'label': 'Contact', 'url': '/contact/'}
]
```

## Complex Components

### DataTable
```django
{% component "datatable" columns=columns data=data sortable=True searchable=True %}
{% endcomponent %}

<!-- In views.py -->
columns = [
    {'label': 'Name', 'key': 'name'},
    {'label': 'Email', 'key': 'email'},
    {'label': 'Status', 'key': 'status'}
]

data = [
    {'name': 'John Doe', 'email': 'john@example.com', 'status': 'Active'},
    {'name': 'Jane Smith', 'email': 'jane@example.com', 'status': 'Inactive'}
]
```

### Multi-Step Wizard
```django
{% component "wizard" steps=wizard_steps current_step=0 %}
{% endcomponent %}

<!-- In views.py -->
wizard_steps = [
    {'title': 'Step 1', 'content': '<div>Step 1 form fields</div>'},
    {'title': 'Step 2', 'content': '<div>Step 2 form fields</div>'},
    {'title': 'Finish', 'content': '<div>Confirmation</div>'}
]
```

### File Upload
```django
{% component "fileupload" multiple=True accept="image/*" drag_drop=True max_size=5242880 %}
{% endcomponent %}

<!-- max_size in bytes (5MB = 5242880) -->
```

### Kanban Board
```django
{% component "kanban" columns=kanban_columns cards=kanban_cards %}
{% endcomponent %}

<!-- In views.py -->
kanban_columns = [
    {'id': 'todo', 'title': 'To Do', 'variant': 'secondary'},
    {'id': 'doing', 'title': 'In Progress', 'variant': 'primary'},
    {'id': 'done', 'title': 'Done', 'variant': 'success'}
]

kanban_cards = [
    {'id': 1, 'column': 'todo', 'title': 'Task 1', 'description': 'Do something'},
    {'id': 2, 'column': 'doing', 'title': 'Task 2', 'description': 'Working on it'}
]
```

### Stat Card
```django
{% component "statcard" title="Total Revenue" value="$45,678" icon="bi bi-currency-dollar" trend="up" trend_value="+12%" variant="success" %}
{% endcomponent %}

<!-- Available trends: up, down, neutral -->
```

### Chart
```django
{% component "chart" chart_type="bar" data=chart_data labels=chart_labels %}
{% endcomponent %}

<!-- In views.py -->
chart_data = [65, 59, 80, 81, 56, 55, 40]
chart_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

<!-- Available types: bar, line, pie, doughnut, radar -->
```

## Form Components

### Crispy Form
```python
# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='mb-3'),
            Field('email', css_class='mb-3'),
            Submit('submit', 'Send', css_class='btn btn-primary')
        )
```

```django
<!-- template.html -->
{% component "crispy_form" form=my_form form_id="myForm" %}
{% endcomponent %}
```

### Individual Form Field
```django
{% component "form_field" field=form.name show_label=True %}
{% endcomponent %}
```

### Inline Form
```django
{% component "inline_form" form=search_form action="/search/" submit_text="Search" %}
{% endcomponent %}
```

## Advanced Patterns

### Passing Attributes
```django
{% component "button" variant="primary" class="my-custom-class" data-action="submit" %}
  Button
{% endcomponent %}

<!-- Renders as: -->
<!-- <button class="btn btn-primary btn-md" class="my-custom-class" data-action="submit">Button</button> -->
```

### Nesting Components
```django
{% component "card" title="User Actions" %}
  <div class="d-flex gap-2">
    {% component "button" variant="primary" %}Edit{% endcomponent %}
    {% component "button" variant="danger" %}Delete{% endcomponent %}
  </div>
{% endcomponent %}
```

### Dynamic Variants
```django
{% for status, variant in status_map.items %}
  {% component "badge" variant=variant %}{{ status }}{% endcomponent %}
{% endfor %}
```

## Tips & Best Practices

1. **Always load component_tags**: `{% load component_tags %}` at the top of templates
2. **Use slots for complex content**: Multi-line or nested HTML
3. **Pass data from views**: Keep templates clean, logic in views
4. **Bootstrap classes work**: Add custom Bootstrap classes via attrs
5. **jQuery is available**: All pages include jQuery for interactions
6. **Tooltips need initialization**: Handled automatically in base template

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Dependencies

- Bootstrap 5.3+
- jQuery 3.7+
- Chart.js (for chart component)
- Bootstrap Icons (optional, for icons)
