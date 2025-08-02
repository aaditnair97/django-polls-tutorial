# Django Polls Tutorial Project

This is my completed version of the official Django tutorial project. It includes:

- Poll question and choice model structure
- Admin interface with custom display and inlines
- Static file support with background image
- Working voting system with results
- SQLite database containing a sample question: "Who will be the 2025 F1 WDC?"

## How to run

1. Clone the repository
```
git clone https://github.com/aaditnair97/django-polls-tutorial.git
cd django-polls-tutorial
```

2. Install dependencies (requires Python 3 and Django)
```
pip install django
```

3. Run the development server
```
python manage.py runserver
```

4. Visit `http://127.0.0.1:8000/polls/` in your browser

Access the admin interface at:  
`http://127.0.0.1:8000/admin/`

## Preview

Static assets such as background image are included in:
`polls/static/polls/images/background.jpg`

## Notes

This project is based on the official Django tutorial. All views, models, and admin configurations follow best practices.
