---
title: events
layout: projects
weight: 4
---

<section>
	<h1 style = "text-align: center;">Events</h1>
</section>

<section class = "projects" style = "max-width: 1400px; margin-left: auto; margin-right: auto;">

{% for p in site.data.events %}
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
