**Introduction**

For local rendering, use the [recommended Ruby and Jekyll versions](https://pages.github.com/versions/)

We use "collections" that requires Jekyll Version 3. *May 2017*: Installing things on OSX is troublesome. I use rbenv and ruby version 2.1.9 because of several dependencies.

**Getting Started**

You will need a basic knowledge of:
- github (using the desktop application)
- [symantic html 5](https://www.w3schools.com/html/html5_semantic_elements.asp) *no* styling in the html use *css*
- [markdown markup language](https://daringfireball.net/projects/markdown/syntax).
and some terminal skills to install the software.

In github check-out the repository. Every time you make a change, commit your code in the github app and push it. The website will be updated within a few minutes.

I urge you to run the software locally, so that you can preview your changes before you put it online.
In my case i render with the following terminal command:

`jekyll serve`

then point your browser to

`localhost:4000`


**Adding New Projects**

The preferred *naming* of projects is all *lowercase* using *underscore* _ to separate words. For instance consumer_to_creator, or calm_automaton.

Put projects in the \_projects folder, and will be automatically rendered in the projects folder on the website. In rare cases we add things to the projects folder. For instance, i moved LeDraw to the DIY folder, but since already a few pages linked to it, i keep a redirect in the projects folder.

The first few lines of a project is the so called *front matter*. Which is used for various functionality, such as helping search engines, compiling a list of projects and finding related papers.
Example front matter:

\-\-\-
project: user_review_analysis
permalink: /projects/user_review_analysis/
title: User Review Analysis
short: A new technique that uses big data to uncover user needs for product designers.
long: A new technique that uses big data to uncover user needs for product designers.
picture: user_review_analysis.jpg
layout: project
\-\-\-

*project:* this should match the folder
*permalink:* the absolute path to the project folder, end with a /
*title:* a human readable title.
*short:* a description. Used in the project overview page for the summary.
*long:* a description that is used in google searches and when pages are linked in facebook.
*picture:* a picture of the project 16:9 aspect ratio (go for 1920x1080 or 1280x720)
*thumbnail:* the same picture but a low resolution version: (640x360)
*layout:* we have several layouts. *project* is the simple layout. *project_advanced* has more options. Check the other projects for examples

optional items for the frontmatter are
*team:*
*demos:*




Finally, add the project to the front matter of the index.md in the projects folder. In this way you can make *hidden* projects that are not yet visible on the homepage.


**Adding Data to Projects**

The main file of the project is *index.md* When you use the *project* layout things are really simple. Use the [markdown syntax](https://daringfireball.net/projects/markdown/syntax)
Add images in a *img* subfolder.

The *project_advanced* provides you with more options, but you have setup the columns yourself. We use [gridism](http://cobyism.com/gridism/) css and use a 3 column layout.

**Image Guidelines**

We like sites that load fast. So, try to optimize images. Photos should be jpg, illustrations are sometimes better with png.
