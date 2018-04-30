# IDEAS FOR MOVING FORWARD (feel free to add to this)
I think we should frame the tutorial (I want this to be a tutorial) as a list of requests from some faculty member.

## Request 1: The csv has been updated, update the database
The first thing that can happen is an update to a csv, in the form of existing data being updated, new rows being added, and a new column being added. This will have them:

  1. Edit the models to conform with the new field
  2. Create an importer (I like to do this as a manage.py command, but idk if that is best)
 

## Request 2: The database has been updated, add a visualization
The next request could be to display the new data in a visualization. We can point them to a d3 gallery (do we use d3?) or something specific, like [this interactive bar chart](http://bl.ocks.org/Caged/6476579). We could also make it so the data needs to be processed a little in python giving them the opportunity to work more in views. So, this has them:

  1. Make edits to a view, to process/pass data
  2. Add something to a template, and integrate javascript in that
  3. Work with some random code from the internet (which can be a challenge)


## Request 3: Add a totally new page to the site
Next, we can have them add a totally new page to the site. I'm not sure what it will have on it, maybe just a complete list of something from a model? This will have them:
  1. Create a template from scratch
  2. Add a link to the navbar
  3. Add a url to urls
  4. Add a view, and get data from the database to base to the template
  5. Dynamically display data in a template

## Non-Request task
Often, you may notice something wrong with a project, or just something that can be improved. Personally, I like it when the navbar is in its own file, it makes it nice and easy to find. We can then ask them to move the navbar into its own file, which will show them how django blocks work. This also encourages them to fix problems as they see them, which I think is generally a good idea! We could also intentionally have an error a little more significant than this, as long as we comment big that it is done poorly.

## End thoughts
I think this is all I have for now, it might also be good to have them edit some javascript and css. We will also need to include what to do with git, maybe have them make a new branch or even a fork of the project. I think that we shouldn't give them too much instructions on how to do these things. I think my ideal set of instructions is pretty close to what I have written up here: it basically just requests something to be done and loosely tells them where and what needs to be done for that task. I certainly don't want it to be a step-by-step guide, those are very ineffective. By telling them where they need to do the thing, they can look at something we already have there which provides a framework for them to complete the request based on.

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
python3 manage.py runserver 8000
```
The site should now be accessible at [this link](127.0.0.1:8000/).
You can run the site in the background by appending an `&` at the end of the command i.e.
```
python3 manage.py runserver 8000 &
```
To bring this back to the foreground (likely to stop it), use the command `fg` (then you can `crtl-c` to kill it).
