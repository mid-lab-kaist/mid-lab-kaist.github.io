---
title: projects
layout: default
weight: 4
---
<section class="projects">

{% for p in site.data.projects %}
{%capture pos %}{% cycle 'first', 'second', 'third' %}{% endcapture %}
{% if pos == 'first' %}
<div class="grid" style="background-color:#ddffdd;">
{% endif %}
<div class="unit one-third" style="background-color:#ffffff;">
<a href="{{ p.link }}"><img src='img/{{ p.picture }}' onmouseover="this.src='img/{{ p.picture_change }}'" onmouseout="this.src='img/{{ p.picture }}'" alt="{{ p.title }}" /></a><h2>{{p.title}}</h2><p>{{ p.abstract }}</p>
</div>
{% if pos == 'third' %}
</div> <!-- grid -->
{% endif %}
{% endfor %}

{% if pos != 'third' %}
</div> <!-- grid -->
{% endif %}

</section>
