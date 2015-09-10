---
title: people
layout: people
weight: 3
---


<section class="members">

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
<li>Tetiana Parshakova is currently working in the lab on an undergraduate research project dealing with moving everyday objects wirelessly with gestured controls.</li>
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

<ul>
<li>Shin Hyung Sup (Felix) joined the lab in the Winter of 2013 as an undergraduate research intern working on <a href = '../projects/tag_radar/'>TagRadar</a>, a smart phone accessory for locating items.</li>
<li>Seoyoung Baek and Joonhee Min joined the lab through the KAIST Undergraduate Research Proposal scholarship. They worked on surface texture experience in 3D printing until the Summer of 2015.</li>
<li>Alex Balio and Sam Ukolov joined the lab through the KAIST Undergraduate Research Proposal scholarship from Winter 2014 to Summer 2015. They worked on the <a href = "../projects/misc/painting_drone.pdf">Painting Drone</a>.</li>
<li>Hayeon Jeong joined the lab for the 2013/2014 Winter break for undergraduate individual study.</li>
</ul>

</section>

