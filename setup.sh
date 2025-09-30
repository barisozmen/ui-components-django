#!/bin/bash

# UI Components Library Setup Script

echo "🎨 Setting up Django UI Components Library..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🔄 Running migrations..."
python manage.py migrate

# Create superuser (optional)
echo ""
echo "💼 Create superuser? (y/n)"
read -r create_superuser
if [ "$create_superuser" = "y" ]; then
    python manage.py createsuperuser
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the development server, run:"
echo "   python manage.py runserver"
echo ""
echo "📚 Then visit:"
echo "   - http://localhost:8000/ (Component Showcase)"
echo "   - http://localhost:8000/forms/ (Forms Showcase)"
echo "   - http://localhost:8000/admin/ (Django Admin)"
echo ""
echo "Happy coding! 🎉"
