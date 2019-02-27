lab website
============


installation
------------

pip3 install ruamel.yaml markdown bibtexparser

currently depends on bibtexparser https://github.com/sciunto-org/python-bibtexparser

running the flask server locally
--------------------------------

make run

render a static version
-----------------------

make static

uploading website to github
---------------------------

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




python library
--------------

lab
* publications
* events
* projects
* news

