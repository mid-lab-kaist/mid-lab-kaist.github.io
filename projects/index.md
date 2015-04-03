---
title: projects
layout: projects
weight: 4
---

<section class="projects">

{% for p in site.data.projects %}
{%capture pos %}{% cycle 'first', 'second', 'third', 'last' %}{% endcapture %}


{% if pos == 'first' %}
<div class='grid no-gutters'>
{% endif %}
<div class='unit one-quarter'>
<a href="{{ p.link }}"><img src='img/{{ p.picture }}' alt="{{ p.title }}" /></a><p>{{ p.abstract }}</p>
</div>
{% if pos == 'last' %}
</div> <!-- grid -->
<div class="clearfix"></div>
{% endif %}
{% endfor %}

{% if pos != 'last' %}
</div> <!-- grid -->
<div class="clearfix"></div>
{% endif %}

</section>
