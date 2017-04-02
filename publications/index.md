---
title: publications
layout: simple
weight: 5
---

<section class="publications">

{% for year in site.data.bib %}
<!-- <h2>{{ year[0] }} {{ year[1] | size}}</h2> -->
{% for entry in year[1] %}
{% if entry == year[1].first %}
<h2>{{ year[0] }}</h2>
{% endif %}
<p>{{entry.authors}}. {% if entry.pdf.size != undefined %}<a href = "files/{{ entry.id }}.pdf">{{entry.title}}.</a>{% else %}{{entry.title}}{% endif %} In <i>{{entry.publication}}</i>. {{entry.date}}. {% if entry.doi.size != undefined %}<a href = "https://dx.doi.org/{{entry.doi}}">[doi]</a>{% endif %} <a href="files/{{entry.id}}.bib">[bib]</a> {% if entry.project.size != undefined %}<a href = "/projects/{{entry.project}}">[project page]</a>{% endif %} {% if entry.prize.size != undefined %}<em>{{entry.prize}}.</em>{% endif %}</p>
{% endfor %}
{% endfor %}

</section>
