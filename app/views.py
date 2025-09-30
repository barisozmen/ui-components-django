from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm, RegistrationForm


def showcase(request):
    """Main showcase page displaying all UI components"""
    
    # Sample data for components
    navbar_items = [
        {'label': 'Home', 'url': '/', 'active': True},
        {'label': 'Components', 'url': '/showcase/'},
        {'label': 'Forms', 'url': '/forms/'},
        {'label': 'Kanban', 'url': '/kanban/'},
    ]
    
    context = {
        'navbar_items': navbar_items,
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Components', 'url': '/showcase/'},
            {'label': 'Showcase'}
        ],
        'dropdown_items': [
            {'label': 'Action', 'url': '#'},
            {'label': 'Another action', 'url': '#'},
            {'divider': True},
            {'label': 'Something else', 'url': '#'},
        ],
        'tab_items': [
            {'label': 'Home', 'content': '<p>This is the home tab content.</p>'},
            {'label': 'Profile', 'content': '<p>This is the profile tab content.</p>'},
            {'label': 'Messages', 'content': '<p>This is the messages tab content.</p>'},
        ],
        'accordion_items': [
            {'title': 'Accordion Item #1', 'content': '<p>This is the first item\'s accordion body.</p>', 'show': True},
            {'title': 'Accordion Item #2', 'content': '<p>This is the second item\'s accordion body.</p>', 'show': False},
            {'title': 'Accordion Item #3', 'content': '<p>This is the third item\'s accordion body.</p>', 'show': False},
        ],
        'datatable_columns': [
            {'label': 'Name', 'key': 'name'},
            {'label': 'Email', 'key': 'email'},
            {'label': 'Role', 'key': 'role'},
        ],
        'datatable_data': [
            {'name': 'John Doe', 'email': 'john@example.com', 'role': 'Admin'},
            {'name': 'Jane Smith', 'email': 'jane@example.com', 'role': 'User'},
            {'name': 'Bob Johnson', 'email': 'bob@example.com', 'role': 'Manager'},
        ],
        'kanban_columns': [
            {'id': 'todo', 'title': 'To Do', 'variant': 'secondary'},
            {'id': 'progress', 'title': 'In Progress', 'variant': 'primary'},
            {'id': 'done', 'title': 'Done', 'variant': 'success'},
        ],
        'kanban_cards': [
            {'id': 1, 'column': 'todo', 'title': 'Task 1', 'description': 'Description for task 1'},
            {'id': 2, 'column': 'todo', 'title': 'Task 2', 'description': 'Description for task 2'},
            {'id': 3, 'column': 'progress', 'title': 'Task 3', 'description': 'Description for task 3'},
            {'id': 4, 'column': 'done', 'title': 'Task 4', 'description': 'Description for task 4'},
        ],
    }
    
    return render(request, 'showcase.html', context)


def forms_showcase(request):
    """Forms showcase page"""
    
    navbar_items = [
        {'label': 'Home', 'url': '/'},
        {'label': 'Components', 'url': '/showcase/'},
        {'label': 'Forms', 'url': '/forms/', 'active': True},
        {'label': 'Kanban', 'url': '/kanban/'},
    ]
    
    contact_form = ContactForm()
    registration_form = RegistrationForm()
    
    if request.method == 'POST':
        if 'contact-submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                messages.success(request, 'Contact form submitted successfully!')
        elif 'registration-submit' in request.POST:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                messages.success(request, 'Registration form submitted successfully!')
    
    wizard_steps = [
        {
            'title': 'Personal Info',
            'content': '<div class="mb-3"><label class="form-label">Full Name</label><input type="text" class="form-control" placeholder="Enter your name"></div><div class="mb-3"><label class="form-label">Email</label><input type="email" class="form-control" placeholder="Enter your email"></div>'
        },
        {
            'title': 'Account Details',
            'content': '<div class="mb-3"><label class="form-label">Username</label><input type="text" class="form-control" placeholder="Choose a username"></div><div class="mb-3"><label class="form-label">Password</label><input type="password" class="form-control" placeholder="Enter password"></div>'
        },
        {
            'title': 'Confirmation',
            'content': '<div class="alert alert-success"><h5>All set!</h5><p>Review your information and click finish to complete registration.</p></div>'
        }
    ]
    
    context = {
        'navbar_items': navbar_items,
        'contact_form': contact_form,
        'registration_form': registration_form,
        'wizard_steps': wizard_steps,
    }
    
    return render(request, 'forms_showcase.html', context)


def kanban_showcase(request):
    """Kanban board showcase page"""
    
    navbar_items = [
        {'label': 'Home', 'url': '/'},
        {'label': 'Components', 'url': '/showcase/'},
        {'label': 'Forms', 'url': '/forms/'},
        {'label': 'Kanban', 'url': '/kanban/', 'active': True},
    ]
    
    # Basic kanban board
    basic_columns = [
        {'id': 'todo', 'title': 'To Do', 'variant': 'secondary'},
        {'id': 'progress', 'title': 'In Progress', 'variant': 'primary'},
        {'id': 'done', 'title': 'Done', 'variant': 'success'},
    ]
    
    basic_cards = [
        {'id': 1, 'column': 'todo', 'title': 'Design Homepage', 'description': 'Create wireframes and mockups for the new homepage'},
        {'id': 2, 'column': 'todo', 'title': 'Update Documentation', 'description': 'Add API documentation for new endpoints'},
        {'id': 3, 'column': 'todo', 'title': 'Fix Navigation Bug', 'description': 'Mobile navigation not closing on tap'},
        {'id': 4, 'column': 'progress', 'title': 'Implement User Auth', 'description': 'Add OAuth2 authentication flow'},
        {'id': 5, 'column': 'progress', 'title': 'Database Migration', 'description': 'Migrate from SQLite to PostgreSQL'},
        {'id': 6, 'column': 'done', 'title': 'Setup CI/CD', 'description': 'Configure GitHub Actions for automated deployment'},
        {'id': 7, 'column': 'done', 'title': 'Write Unit Tests', 'description': 'Add test coverage for core modules'},
    ]
    
    # Development workflow
    dev_columns = [
        {'id': 'backlog', 'title': 'Backlog', 'variant': 'light'},
        {'id': 'dev', 'title': 'Development', 'variant': 'info'},
        {'id': 'review', 'title': 'Code Review', 'variant': 'warning'},
        {'id': 'testing', 'title': 'Testing', 'variant': 'primary'},
        {'id': 'deployed', 'title': 'Deployed', 'variant': 'success'},
    ]
    
    dev_cards = [
        {'id': 101, 'column': 'backlog', 'title': 'User Profile Page', 'description': 'Allow users to edit their profile information'},
        {'id': 102, 'column': 'backlog', 'title': 'Email Notifications', 'description': 'Send email alerts for important events'},
        {'id': 103, 'column': 'dev', 'title': 'Search Feature', 'description': 'Implement full-text search with filters'},
        {'id': 104, 'column': 'review', 'title': 'Payment Integration', 'description': 'Integrate Stripe payment processing'},
        {'id': 105, 'column': 'testing', 'title': 'Dashboard Analytics', 'description': 'Add charts and metrics to dashboard'},
        {'id': 106, 'column': 'deployed', 'title': 'Login System', 'description': 'User authentication and session management'},
    ]
    
    # Sales pipeline
    sales_columns = [
        {'id': 'lead', 'title': 'New Leads', 'variant': 'info'},
        {'id': 'qualified', 'title': 'Qualified', 'variant': 'primary'},
        {'id': 'proposal', 'title': 'Proposal Sent', 'variant': 'warning'},
        {'id': 'negotiation', 'title': 'Negotiation', 'variant': 'danger'},
        {'id': 'closed', 'title': 'Closed Won', 'variant': 'success'},
    ]
    
    sales_cards = [
        {'id': 201, 'column': 'lead', 'title': 'Acme Corp', 'description': 'Interested in Enterprise plan - $50k/year'},
        {'id': 202, 'column': 'lead', 'title': 'TechStart Inc', 'description': 'Startup looking for Team plan - $5k/year'},
        {'id': 203, 'column': 'qualified', 'title': 'Global Industries', 'description': 'Fortune 500 client - $200k/year potential'},
        {'id': 204, 'column': 'proposal', 'title': 'SmartSolutions', 'description': 'Custom integration required - $75k'},
        {'id': 205, 'column': 'negotiation', 'title': 'InnovateCo', 'description': 'Negotiating contract terms - $100k/year'},
        {'id': 206, 'column': 'closed', 'title': 'DataCorp', 'description': 'Signed 3-year contract - $150k/year'},
    ]
    
    # Project management
    project_columns = [
        {'id': 'planning', 'title': 'Planning', 'variant': 'secondary'},
        {'id': 'design', 'title': 'Design', 'variant': 'info'},
        {'id': 'development', 'title': 'Development', 'variant': 'primary'},
        {'id': 'launch', 'title': 'Launch', 'variant': 'success'},
    ]
    
    project_cards = [
        {'id': 301, 'column': 'planning', 'title': 'Q4 Marketing Campaign', 'description': 'Plan holiday season promotions'},
        {'id': 302, 'column': 'planning', 'title': 'Mobile App Redesign', 'description': 'Update UI/UX for iOS and Android apps'},
        {'id': 303, 'column': 'design', 'title': 'Brand Guidelines', 'description': 'Create comprehensive brand identity guide'},
        {'id': 304, 'column': 'development', 'title': 'API v2.0', 'description': 'Build next generation REST API'},
        {'id': 305, 'column': 'development', 'title': 'Customer Portal', 'description': 'Self-service portal for customers'},
        {'id': 306, 'column': 'launch', 'title': 'Website Relaunch', 'description': 'Successfully launched new website'},
    ]
    
    context = {
        'navbar_items': navbar_items,
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Kanban Showcase'}
        ],
        'basic_columns': basic_columns,
        'basic_cards': basic_cards,
        'dev_columns': dev_columns,
        'dev_cards': dev_cards,
        'sales_columns': sales_columns,
        'sales_cards': sales_cards,
        'project_columns': project_columns,
        'project_cards': project_cards,
    }
    
    return render(request, 'kanban_showcase.html', context)