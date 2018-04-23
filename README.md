# Django showcase for Haverford Digital Scholarship
This project showcases many of the features of the [Django](https://www.djangoproject.com/)
web framework as used by Haverford DS.

## How do I run this?
Within the terminal, navigate to the directory you want the top folder of this project to be in (it will make a django-showcase folder). Type
```
git clone https://github.com/HCDigitalScholarship/django-showcase.git
```

(this is the link from the green "clone or download button")

Make sure you have Django installed. #TODO we might want to talk about setting up a virtualenv.

To run the site, navigate into the first django-shwocase folder (the one with manage.py) and run 
```
python manage.py runserver 8000
```
The site should now be accessible at [this link](127.0.0.1:8000/).
You can run the site in the background by appending an `&` at the end of the command i.e.
```
python manage.py runserver 8000 &
```
To bring this back to the foreground (likely to stop it), use the command `fg` (then you can `crtl-c` to kill it).
