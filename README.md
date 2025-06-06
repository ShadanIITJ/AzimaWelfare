
# Azima Nishat Welfare Trust Website (Django)

This is a modular static website for Azima Nishat Welfare Trust, built with Django and ready for deployment on PythonAnywhere.

## Features
- **Home, About, Contact, Gallery**: Static pages for Azima Nishat Welfare Trust's information.
- **Events**: Add a new event by creating a folder under `media/events/` with images. The site will auto-list events and show their pictures.
- **Members**: Add or update member details in `members/members.json`.
- **Modern, clean design** with easy-to-edit HTML and CSS.

## Adding Events
1. Create a new folder in `media/events/` (e.g., `media/events/charity_walk_2025`).
2. Add images (jpg, png, etc.) to this folder.
3. The event will appear automatically on the Events page.

## Adding Members
1. Edit `members/members.json` and add a new member object.
2. Optionally, add a member photo to `static/` and update the `photo` path.

## Running Locally
1. Install dependencies: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`
4. Visit `http://127.0.0.1:8000/`

## Deployment
- Ready for PythonAnywhere. Set `DEBUG = False` and update `ALLOWED_HOSTS` in `ngo_site/settings.py` for production.

## Customization
- Update HTML in `pages/templates/pages/`, `events/templates/events/`, and `members/templates/members/` as needed.
- Update CSS in `static/style.css`.

---

*Replace placeholder content and images with Azima Nishat Welfare Trust's real information.*
#   A z i m a W e l f a r e  
 