import os
import pprint
import datetime

import argparse

from flask import Flask, render_template, redirect, send_from_directory, abort
from flask_frozen import Freezer

import lab
import lab.publications
import lab.projects
import lab.news

#
# prepare publications
#

publications = lab.publications.parse_folder("./publications/files/")
publications_per_year = lab.publications.make_sorted_list_per_year(publications)

print("publications loaded from bibtex")

with open("./publications/extra_properties.yaml") as f:
   try:
      lab.publications.add_properties(publications, lab.get_yaml_parser().load(f))
      print("additional properties added to publications")
   except:
      print("error loading extra properties")

#
# prepare projects
#

featured_projects, all_projects = lab.projects.parse_folder("./projects/")

print("projects loaded")

print("add cross references to project information and publications")
lab.projects.cross_ref_projects_publications(all_projects, publications)

#
#  prepare news items
#
print("prepare news")

news_items_sorted, news_items = lab.news.parse_folder("./news/")


#
#  prepare events
#

print("prepare events")


# 
# run flask
#


app = Flask(__name__,static_folder=os.path.abspath("./"), static_url_path='')
app.config.from_pyfile('settings.py')
freezer = Freezer(app)


menu = ["people", "projects", "publications", "contact"]



@app.route("/people/")
def people():
   # read file
   fm, content = lab.load_content_file("./people/people.rst")
   return render_template('people_template.html', top_menu_item="people", top_menu_list=menu, front_matter=fm, page_content=content )

#@app.route('/people/img/')
#def send_people_img():
#    return send_from_directory( , path)


@app.route("/projects/")
def projects_list():
   return render_template('projects_list_template.html', top_menu_item="projects", projects=featured_projects, top_menu_list=menu)

@app.route("/projects/<name>/")
def project(name):
   if name in all_projects:
      return render_template('project_template.html', top_menu_item="projects", project=all_projects[name], top_menu_list=menu)
   else:
      abort(404)
      
#@app.route('/projects/<name>/img/<path:path>')
#def send_project_img(name,path):
#   print( os.path.join('/projects/', name, "img/"), path )
#   return send_from_directory( os.path.join('/projects/', name, "img/"), path)
   

@app.route("/publications/")
def publication_list():
    # fetch publications
   return render_template('publications_template.html', top_menu_item="publications", papers=publications_per_year, top_menu_list=menu)

@app.route("/news/")
def news_list():
   pprint.pprint(news_items_sorted)
   return render_template('news_template.html', top_menu_item="news", news = news_items_sorted, top_menu_list=menu)


@app.route("/news/<int:year>/<int:month>/<int:day>/<name>/")
def news_item(year, month, day, name):
   # construct date
   print(year ,month, day, name)
   date = datetime.date(year=year, month=month, day=day )
   if (date,name) in news_items:
      n = news_items[ (date, name) ]
      return render_template('news_item_template.html', top_menu_item="news", news=n, top_menu_list=menu)
   # fetch publication
   return abort(404)
   

@app.route("/events/")
def events_list():
    return render_template('events_list_template.html', top_menu_item="events", top_menu_list=menu)

@app.route("/events/<name>")
def event(name):
    # fetch publication
    return render_template('event_template.html', top_menu_item="events", top_menu_list=menu)

@app.route("/contact/")
def contact():
    return render_template('contact_template.html', top_menu_item="contact", top_menu_list=menu)


@app.route("/")
def home():
    return render_template('home_template.html', news=news_items_sorted[:4], projects=all_projects, top_menu_item="home", top_menu_list=menu,  autoescape=True)


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
   
