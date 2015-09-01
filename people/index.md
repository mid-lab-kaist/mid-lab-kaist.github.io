---
title: people
layout: people
weight: 3
---


<section class="people">

<h1>Members</h1>
{% for member in site.data.members %}
<div class='grid no-gutters'>
 <div class='unit one-fifth'><img src='img/{{ member.picture }}' alt="{{ member.name }}" /></div>
 <div class='unit four-fifths'>
<h3>{{ member.name }} / {{ member.title }}</h3>
<p>{{ member.bio }}</p>
</div>
</div>
<div class="clearfix"></div>

{% endfor %}


<ul>
<li>Alex Dalio and Sam Stark joined the lab through the KAIST Undergraduate Research Proposal scholarship.</li>
<li>Hayeon Jeong joined the lab for the 2013/2014 Winter break for undergraduate individual study.</li>
<li>Shin Hyung Sup (Felix) joined the lab in the Winter of 2013 as an undergraduate research intern.</li>
<li>Seoyoung Baek and Joonhee Min joined the lab through the KAIST Undergraduate Research Proposal scholarship. They worked on surface texture experience in 3D printing until the Summer of 2015.
</li>
</ul>


<h1>Alumni</h1>
{% for member in site.data.alumni %}
<div class='grid no-gutters'>
 <div class='unit one-fifth'><img src='img/{{ member.picture }}' alt="{{ member.name }}" /></div>
 <div class='unit four-fifths'>
<h3>{{ member.name }} / {{ member.title }}</h3>
<p>{{ member.bio }}</p>
</div>
</div>
<div class="clearfix"></div>

{% endfor %}

</section>

