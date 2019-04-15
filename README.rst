lab website
============

We moved from Jekyll (Ruby) to a simple Flask/Jinja2/Python contraption. 
We kept the "front matter" in yaml to set properties such as for people and projects, 
but switched from Markdown to Restructured Text. Although this is less of a standard, 
it allows to create custom directives and makes the inclusion of videos and such much easier.

A consequence of not using Ruby is that we deal with two branches or two repositories, 
one with the source code and one with the rendered version.

For sake of simplicity, i made one dev repository to be used to develop and test the site locally:
"group_website_dev'. This repository contains a make file to build the static html site,
which in turn can be uploaded to github with another makefile command.

I cleaned both archives, so they are relatively small in size, but site assets such as pdf, are twice on your machine.


installation
------------

Install python3 and the following libraries (see also requirements.txt):

pip3 install flask frozen_flask docutils ruamel.yaml bibtexparser

Clone this repository ( group_website_dev ) and clone the mid-lab-kaist.github.io repository. 

make sure that both repositories are cloned in the same folder. For instance you can choose any name for "my-website":

my-website/group_website_dev
my-website/mid-lab-kaist.github.io


git clone  https://github.com/mid-lab-kaist/group_website.git
git clone https://github.com/mid-lab-kaist/mid-lab-kaist.github.io.git


Once that is done you can keep the mid-lab-kaist untouched.


running the flask server locally
--------------------------------

cd into the "group_website_dev" repository folder

make run

render a static version
-----------------------

In the "group_website_dev" repository folder

make freeze

uploading website to github
---------------------------

In the "group_website_dev" repository folder

make upload

good practise is to check the website functioning online after a few minutes 
to confirm that your changes are uploaded.


Adding a project to the website
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

