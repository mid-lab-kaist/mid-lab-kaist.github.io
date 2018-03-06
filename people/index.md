---
title: people
layout: bare
weight: 3
---




<section class="people">
<div class="grid">
		 <div class="unit whole">
		 <h1>Meet the team</h1>
		 <img src="img/all.jpg" alt="image of all lab members">
		 </div>
</div>

	{% for member in site.data.members %}		
			<div class='grid'>
			<a name="{{ member.short }}">
			 <div class='unit two-thirds'>
			 <img style=" border: 1px solid #cccccc; float: left; margin:4px; max-width:160px;" src='img/{{ member.picture }}' alt="{{ member.name }}" />
			 <h2>{{ member.name }} / {{ member.title }}</h2>
			<p><a href = "http://{{ member.website }}">{{ member.website }}</a>
			<a href = "mailto:{{ member.email }}" >{{ member.email }}</a></p>
			<p>{{ member.bio }}
			</p>
			</div>

			</a>

			</div>
	{% endfor %}

	<div class="grid">
			 <div class="unit whole">
			 <h1>Alumni</h1>
			 </div>
	</div>

	{% for member in site.data.alumni %}		
			<div class='grid'>
			<a name="{{ member.short }}">
			 <div class='unit two-thirds'>
			 <img style=" border: 1px solid #cccccc; float: left; margin:4px; max-width:160px;" src='img/{{ member.picture }}' alt="{{ member.name }}" />
			 <h2>{{ member.name }} / {{ member.title }}</h2>
			 
			<p><a href = "http://{{ member.website }}">{{ member.website }}</a>
			<a href = "mailto:{{ member.email }}" >{{ member.email }}</a></p>
			<p>{{ member.bio }}
			</p>
			</div>

			</a>

			</div>
	{% endfor %}

	<div class="grid">
			 <div class="unit two-thirds">
			 <h1>Alumni Researchers and Interns</h1>
			<p>Anthony Wilson (2017 - Spring 2018)</p>
			<p>Woojae Kang (Winter - Spring 2018)</p>
			<p>Jinyoung Jeong (Winter - Spring 2018)</p>
			<p>Alex Calero (February 2018)</p>
			<p>Minkyeong Lee (2016) <a href="/projects/consumer_to_creator">Consumer to Creator</a></p>
			 <p>Sumin Jang	(Summer 2016)	Visualizing Furniture Layouts in AR</p>
			 	<p> Jaewoong Han	(Spring 2016)	3D Printing and Mold Making</p>
			 			 <p>Tetiana Parshakova	(2015 - 2016) <a href="/projects/ratchair">RatChair</a></p>
			 			 <p>Sangyeob Lee	(Summer 2015)	Interactive Camera System Interface</p>
			 			 <p>Seoyoung Baek and Joonhee Min	(Summer 2015)	Surface Texturing in 3D Printing</p>
			 			 <p>Alex Balio and Sam Ukolov	(2014 - 2015)	Painting Drone</p>
			 			 <p>Felix Shin	(2013 - 2015) <a href="/projects/tag_radar">Tagradar</a></p>
			 			 <p>Hayeon Jeong	(Winter 2013) <a href="/projects/i_eng">I-Eng</a></p>





			 </div>
	</div>


</section>


<section class = "join">
 <div class='grid'>
  <div class = "unit two-thirds" >
    <h1>Join My Design Lab</h1>
    <p>We are always looking for new students and partners. Please <a href="/contact/">contact us</a> for more information.</p>
   </div>
</div>
</section>
