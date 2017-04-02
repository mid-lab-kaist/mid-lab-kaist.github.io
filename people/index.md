---
title: people
layout: bare
weight: 3
---




<section class="people">
<div class="grid">
		 <div class="unit whole">
		 <h1>People</h1>
		 </div>
</div>



	{% for member in site.data.members %}		

			<div class='grid'>

			 <div class='unit two-thirds'>

			 <img style=" border: 1px solid #cccccc; float: left; margin:4px; max-width:160px;" src='img/{{ member.picture }}' alt="{{ member.name }}" />
			 <h2>{{ member.name }} / {{ member.title }}</h2>
			<p>{{ member.bio }}
			<a href = "http://{{ member.website }}">{{ member.website }}</a>
			<a href = "mailto:{{ member.email }}" >{{ member.email }}</a>
			</p>
			</div>

			</div>
	{% endfor %}

</section>


<section class = "join">
 <div class='grid'>
  <div class = "unit two-thirds" style="background-color:#ffddff">
    <h1>Join My Design Lab</h1>
    <p style = "margin-left: auto; margin-right: auto;">We are always looking for new students and partners so please <a href="/contact/">contact us</a> for more information.</p>
   </div>
  <div class = "unit one-third" style="background-color:#ddffff">
	 <h1>sajdfhaksjdf</h1>
 </div>
</div>
</section>

<div class = "clearfix" />
