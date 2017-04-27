---
title: projects
layout: default
weight: 4
---
<section class="projects">

{% for p in site.data.projects %}
{%capture pos %}{% cycle 'first', 'second', 'third' %}{% endcapture %}
{% if pos == 'first' %}
<div class="grid">
{% endif %}
<div class="unit one-third">
<a href="{{ p.link }}"><img src="/projects/{{ p.id }}/img/{{ p.picture }}" alt="{{ p.title }}" /></a><h2>{{p.title}}</h2><p>{{ p.abstract }}</p>
</div>
{% if pos == 'third' %}
</div> <!-- grid -->
{% endif %}
{% endfor %}

{% if pos != 'third' %}
</div> <!-- grid -->
{% endif %}

</section>

<div class="clearfix"/>
