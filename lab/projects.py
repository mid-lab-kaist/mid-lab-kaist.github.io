#
#
#

import os
import sys
import glob
import datetime

from lab import load_content_file
from lab import get_yaml_parser
from lab import rest_to_html

class Project():
    def __init__(self, folder, front_matter, content):
        self.folder = folder
        self.front_matter = front_matter
        self.content = content

def parse_folder(folder):
    projects = {}

    dir_list = next(os.walk(folder))[1]
    for p in dir_list:
        fm, c_rest = load_content_file(os.path.join(folder, p, "index.rst"))
        # make html
        c = rest_to_html(c_rest)
        projects[ fm['project'] ]= Project(os.path.join('/projects/', p), fm, c ) 

    featured_list = []
    with open( os.path.join(folder, "featured.yaml") ) as f:
        featured = get_yaml_parser().load(f)
        for f in featured:
            featured_list.append( projects[f] )

    return featured_list, projects

def cross_ref_projects_publications(projects, publications):
    for key, p in projects.items():

        if "papers" in p.front_matter:
            paper_indexes = p.front_matter["papers"]
            papers = []
            
            for paper in paper_indexes:
                papers.append( publications[paper] )
                publications[paper].project = p
            p.papers = papers
