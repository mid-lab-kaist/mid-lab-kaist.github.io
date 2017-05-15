---
title: projects
layout: default
weight: 4
featured:
 - consumer_to_creator
 - "ori-mandu"
 - mirror
 - bodymeter
 - gluons
 - calm_automaton
 - twoshelves
 - ratchair
 - user_review_analysis
 - tag_radar
 - i_eng
 - chopsticks
 - flying_camera
 - lampan
 - photochromic_carpet
 - paccam
 - delftblue_by_me
 - shader_printer
 - slow_display
 - skin
---
<section class="projects">

{% for p in page.featured %}
{%capture pos %}{% cycle 'first', 'second', 'third' %}{% endcapture %}
{% if pos == 'first' %}
<div class="grid">
{% endif %}
<div class="unit one-third">
{% include project_summary.html project=p %}
</div>
{% if pos == 'third' %}
</div> <!-- grid -->
{% endif %}
{% endfor %}

{% if pos != 'third' %}
</div> <!-- grid -->
{% endif %}

</section>
