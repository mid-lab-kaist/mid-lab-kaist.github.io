---
title: news
layout: news
weight: 2
---
{% for post in site.posts %}
<div class="grid no-gutters {% cycle 'white', 'blue' %}">
   <div class="unit one-quarter">
{% if post.picture %}
<img src="img/{{ post.picture }}">
{% else %}
<img src="img/white.png">
{% endif %}

</div>
   <div class="unit three-quarters">
     <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>

     <p><b>{{ post.date | date_to_long_string }}.</b> {{ post.excerpt | remove: '<p>' | remove: '</p>' }}
    </p>

 </div>

</div>
<div class="clearfix"></div>

{% endfor %}

<!--
<ul class="posts">
  {% for post in site.posts %}
    <li class="{% cycle 'white', 'blue' %}" >
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p class="small">posted on {{ post.date | date_to_long_string }}</p>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
-->

