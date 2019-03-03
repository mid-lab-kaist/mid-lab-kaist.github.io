lab website
============

We moved from Jekyll (Ruby) to a simple Flask/Jinja2/Python contraption. We kept the "front matter" in yaml to set properties such as for people and projects, but switched from Markdown to Restructured Text. Although this is less of a standard, it allows to create custom directives and makes the inclusion of videos and such much easier.

A consequence of not using Ruby is that we deal with two branches, one with the source code (the gh-pages branch) and one with the rendered version (the master branch). 

installation
------------

Install python3 and the following libraries (see also requirements.txt):


pip3 install flask frozen_flask docutils ruamel.yaml bibtexparser


Clone repository two times. This is sacrificing hard disk space for simplicity.

make the following folder structure (you can choose any name for "my-website" as long as you keep the src and frozen part):

my-website/src/
my-website/frozen/

in the "src" folder clone the gh-pages branch::

cd src
git clone -b gh-pages https://github.com/mid-lab-kaist/mid-lab-kaist.github.io.git

in the "frozen" folder clone the master branch

git clone https://github.com/mid-lab-kaist/mid-lab-kaist.github.io.git


Once that is done you can keep the frozen folder untouched and do all work in the src folder.


running the flask server locally
--------------------------------

in the "src" repository

make run

render a static version
-----------------------

in the "src" repository

make freeze

uploading website to github
---------------------------

in the "sr" repository

make upload

adding a project to the website
-------------------------------

1. Make a new folder in the projects directory. Default naming is to use lowercase and underscores: e.g. actuated_monitor

2. Copy one of the "index.rst" files from another project into the folder and edit the "front matter"

3. Make a subfolder "img" and add images.

4. To make the project appear in the projects list add it to the "featured.yaml" file.


adding a publication to the website
-----------------------------------

1. Upload the video(s) to vimeo and note the vimeo video id.

2. Make or download a bibtex file. The naming standard is as follows: (all lowercase) author_conference_year
conference names are: siggraph, chi, uist, chi_wip, siggraph_etech. If 1 author has 2 chi papers we append a number e.g. lee_chi_2018_2.
As for the entry in the bibtex file, we follow the same naming except we use : instead of _: lee:dis:2018

3. Make an *authors* version of the pdf, name it accordingly. This is without the acm copyrights. 

4. save both bib and pdf in the publications/files folder. The website automatically updates.

5. if your publication received an award, please update the awards.yaml

6. if your publication is part of an existing project, add it in the project file's front matter. If it is a new project,
start a new project (see above).

basic Restructured Text commands
--------------------------------



python library
--------------

lab
* publications
* events
* projects
* news

