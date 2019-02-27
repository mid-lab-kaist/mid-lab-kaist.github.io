#
#
#

import os
import sys
import glob
import datetime

from lab import load_content_file
from lab import rest_to_html

class NewsItem():
    def __init__(self, date, name, front_matter, content):
        self.date = date
        self.name = name
        self.front_matter = front_matter
        self.content = content
        self.permalink = "/news/{}/{}/{}/{}/".format(date.year, date.month, date.day, name )
        self.next = None
        self.prev = None
    def __lt__(self, other):
        return self.date < other.date

def extract_first_paragraph(text):
    paragraphs = text.split("\n\n")
    if len(paragraphs) > 1:
        return paragraphs[0]
    return None

def parse_folder(folder):
    items = {}
    ordered_items = []
    files = os.listdir(folder)
    files.sort(reverse=True)
    # make objects
    for f in files:
        if f=="index.html":
            continue
        # no folders
        if not os.path.isfile(os.path.join(folder,f)):
            continue
        # no dot files (.DS_Store)
        if f[0] == '.':
            continue
        u = f.split("-")
        date = datetime.date(year=int(u[0]), month=int(u[1]), day=int(u[2]) )
        name = u[3].split(".")[0]
        fm, c_rest = load_content_file(os.path.join(folder, f))

        c = rest_to_html(c_rest)
        i = NewsItem(date, name, fm, c)

        # make a short version (only first paragraph)
        short = extract_first_paragraph(c_rest)
        if short:
            i.short = rest_to_html(short)
            i.has_short = True
        else:
            i.has_short = False
            
        items[ (date,name) ] = i
        ordered_items.append(i)

    # add next, prev 
    for i in range(len(ordered_items)):
        # array is in reverse order

        if i != 0:
            ordered_items[i].next = ordered_items[i-1]
        if i != len(ordered_items)-1:
            ordered_items[i].prev = ordered_items[i+1]


    return ordered_items, items