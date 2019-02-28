#
#
#

import os
import sys
import glob
import datetime

import re

from ruamel.yaml import YAML
yaml=YAML(typ='safe')   # default, if not specfied, is 'rt' (round-trip)

from docutils import core
from docutils.writers.html4css1 import Writer,HTMLTranslator
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils import nodes
from docutils.nodes import TextElement, Inline, image


# https://gist.github.com/mastbaum/2655700


class vimeo(image):
    '''This node class is a no-op -- just a fun way to define some parameters.
    There are lots of base classes to choose from in `docutils.nodes`.
    See examples in `docutils.nodes`
    '''
    pass

# https://stackoverflow.com/questions/3819917/single-py-file-for-convert-rst-to-html
class Vimeo(Directive):
    """Insert video."""
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'caption': directives.unchanged,
                  }
    has_content = False

    def run(self):
        s = '<div class="vimeo"><iframe src="https://player.vimeo.com/video/' + self.arguments[0] + '" frameborder="0" allowfullscreen> </iframe></div>'
        #s = '\ninsert video: ' + self.arguments[0] + '\n'
        #video_node = nodes.paragraph(text = s)
        return [ vimeo(text=self.arguments[0]) ]

directives.register_directive("vimeo", Vimeo)

# https://stackoverflow.com/questions/3819917/single-py-file-for-convert-rst-to-html

class HTMLFragmentTranslator( HTMLTranslator ):
    def __init__( self, document ):
        HTMLTranslator.__init__( self, document )
        self.head_prefix = ['','','','','']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []
    def astext(self):
        return ''.join(self.body)

    def visit_vimeo(self, node):
        # don't start tags; use 
        #     self.starttag(node, tagname, suffix, empty, **attributes)
        # keyword arguments (attributes) are turned into html tag key/value
        # pairs, e.g. `{'style':'background:red'} => 'style="background:red"'`
        s= 'http://player.vimeo.com/video/' + node.attlist()[0][1]
        self.body.append(self.starttag(node, 'div', '', CLASS='embed-responsive embed-responsive-16by9'))
        self.body.append(self.starttag(node, 'iframe','', CLASS='embed-responsive-item', src=s, frameborder="0", allowfullscreen="allowfullscreen"))
    
    def depart_vimeo(self, node):
        self.body.append('</iframe></div>\n')

html_fragment_writer = Writer()
html_fragment_writer.translator_class = HTMLFragmentTranslator

def rest_to_html( s ):
    #return core.publish_string( s, writer = html_fragment_writer )
    return core.publish_parts( s, writer = html_fragment_writer )['fragment']




# https://github.com/eyeseast/python-frontmatter/blob/master/frontmatter/default_handlers.py
fm_boundary = re.compile(r'^-{3,}$', re.MULTILINE)

# https://stackoverflow.com/questions/3819917/single-py-file-for-convert-rst-to-html


def get_yaml_parser():
    return yaml

def load_content_file(filename):
    """load a file and extract the front matter
    
    Args:
        filename (string): name of the file.

    Returns:
        frontmatter: if available, otherwise returns {}
        content: if available, otherwise returns empty string
    """

    with open(filename) as file:
        txt = file.read()
    
        if fm_boundary.match(txt):
            _, front_matter, content = fm_boundary.split(txt, 2)
            fm = get_yaml_parser().load(front_matter)
            return fm, content


