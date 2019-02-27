#
#
#

import os
import sys
import glob
import datetime

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def clean_latex_escapes(s) :
    s = s.replace("\&","&")
    return s


class Publication():
    def __init__(self, bibtex):
        assert( len(bibtex.entries) == 1)
        self.bib = bibtex.entries[0]
        
        self.key = self.bib['ID'].replace(':','_') 
        
        self.year = int(self.bib['year'])
        self.title = clean_latex_escapes(self.bib['title'])
        self.authors = self.make_author_string()
        self.publication = self.make_publication_string()
        self.date = self.make_date_string()
        self.isodate = self.make_iso_date()
        self.project = None
        if 'doi' in self.bib:
            self.doi = self.bib['doi']

    def __repr__(self):
        return "{} {}".format(self.key, self.title)

    def set_award(self, a):
        self.award = a

    def set_hidden(self, h):
        self.hidden = h


    def make_publication_string(self) :
        if 'series' in self.bib:
            return self.bib['series']
        if self.bib['ENTRYTYPE'] == "article":
            s = self.bib['journal']
            if 'volume' in self.bib and 'number' in self.bib:
                s += '. {0}({1})'.format(self.bib['volume'], self.bib['number'])
            return s
        if self.bib['ENTRYTYPE'] == "incollection":
            return '{0}, {1}, {2}'.format(clean_latex_escapes(self.bib['booktitle']), self.bib['publisher'], self.bib['address'])
        if self.bib['ENTRYTYPE'] == "book":
            return self.bib['publisher']
        return self.bib['booktitle']

    def make_iso_date(self):
        #if 'month' in self.bib:
        #    months = ['jan','feb','mar',"apr","may","jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        #    return datetime.date(year=int(self.bib['year']), month=int(self.bib['month']))
        return datetime.date(year=int(self.bib['year']), month=1, day=1)


    def make_date_string(self) :
        if 'month' in self.bib:
            return '{0} {1}'.format(self.bib['month'], self.bib['year'])
        return self.bib['year']

    def make_author_string(self):	
        authors = []
        author_list = self.bib['author'].split(" and ")
        for a in author_list:
            name = a.split(",")
            authors.append(name[1].strip() + " " + name[0].strip())            
        if( len(authors) == 1) :
            return a
        ret = ""
        for a in authors[0:-2]:
            ret += a + ", "
        ret += authors[-2] + " and " + authors[-1]
        return ret

def parse_folder(folder):
    publications = {}
    for f in glob.glob( os.path.join(folder, "*.bib")):
        with open(f) as bibtex_file:
            p = Publication( bibtexparser.loads( bibtex_file.read() ) )

            # check pdf:
            if not os.path.isfile( os.path.join(folder, p.key +".pdf") ):
                #print("pdf does not exist:", p.key)
                p.has_pdf = False
            else:
                p.has_pdf = True

            publications[p.key] = p
    return publications

def make_sorted_list_per_year(publications):
    l = list(publications.values())
    l.sort(key= lambda r:r.isodate, reverse=True) 

    d = {}
    # then sort per year
    for p in l:
        if p.year in d:
            d[p.year].append(p)
        else:
            d[p.year] = [p]
    return d


def add_properties(publications, props):
    """ add extra properties to the publication dict. Things that we don't 
        want in the bibtex files such as awards.

    Args:
        param1 (dict): The publication dict { publication_key: { ... } )
        param2 (dict): A dict with dicts. { publication_key : {property: value} }
    """
    for key, value in props.items():
        if key in publications:
            if "award" in value:
                #print("AWARD")
                publications[key].set_award(value["award"])
            if "hide" in value:
                #print("HIDDEN", key, value)
                publications[key].set_hidden(value["hide"])
