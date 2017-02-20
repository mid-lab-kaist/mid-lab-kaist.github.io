---
title: people
layout: people
weight: 3
---


<section class="members">
	<h1 style = "text-align: center;">People</h1>
	<section style = "max-width: 1024px; margin-left: auto; margin-right: auto;">
	{% for member in site.data.members %}		
			<div class='grid no-gutters'>
			 <div class='unit one-fifth'><img style = "margin-left: 10px;" src='img/{{ member.picture }}' alt="{{ member.name }}" /></div>
			 <div class='unit four-fifths'>
			<h3>{{ member.name }} / {{ member.title }}</h3>
			<p><small><a href = "http://{{ member.website }}" target = "_blank"> {{ member.website }} </a> / <a href = "mailto:{{ member.email }}" target = "_blank">{{ member.email }}</a></small></p>
			<p>{{ member.bio }}</p>
			</div>
			</div>
			<div class="clearfix"></div>
	{% endfor %}

	<br>
		<table style = "width: 80%; margin-left: 20px;">
			<caption>Undergradute Students</caption>
			<tr>
				<td style = "width: 30%;"><b>Name</b></td>
				<td style = "width: 15%;"><b>Duration</b></td>
				<td style = "width: 55%;"><b>Project</b></td>
			</tr>							
			<tr>
				<td>Juhyung Park</td>
				<td>2016</td>
				<td><a href = "../projects/ledraw/">LEDraw</a> and Interactive Video Projections</td>
			</tr>
		</table>
	</section>
	
	<hr>

<section style = "max-width: 1024px; margin-left: auto; margin-right: auto;">
{% for member in site.data.alumni %}
	
	<div class='grid no-gutters'>
	 <div class='unit one-fifth'><img style = "margin-left: 10px;" src = 'img/{{ member.picture }}' alt="{{ member.name }}" /></div>
	 <div class='unit four-fifths'>
	<h3>{{ member.name }} / {{ member.title }}</h3>
	<p><small><a href = "http://{{ member.website }}" target = "_blank"> {{ member.website }} </a> / <a href = "mailto:{{ member.email }}" target = "_blank">{{ member.email }}</a></small></p>
	<p>{{ member.bio }}</p>
	</div>
	</div>
	<div class="clearfix"></div>

	{% endfor %}

	<br>

		<table style = "width: 80%; margin-left: 20px;">
			<caption>Previous Undergradute Students</caption>
			<tr>
				<td style = "width: 30%;"><b>Name</b></td>
				<td style = "width: 15%;"><b>Duration</b></td>
				<td style = "width: 55%;"><b>Project</b></td>
			</tr>						
			<tr>
				<td>Minkyeong Lee</td>
				<td>2016</td>
				<td>Interactive Video Projections</td>
			</tr>			
			<tr>
				<td>Seungryeol Kim</td>
				<td>Summer 2016</td>
				<td><a href = "../publications/files/2016_gesture_trafficator_paper.pdf">Gesture-Based Trafficator</a></td>
			</tr>
			<tr>
				<td>Sumin Jang</td>
				<td>Summer 2016</td>
				<td>Visualizing Furniture Layouts in AR</td>
			</tr>			
			<!--<tr>
				<td>Maria Reyes</td>
				<td>Spring 2016</td>
				<td>Tangible Programming Toolkit</td>
			</tr>-->
			<tr>
				<td>Jaewoong Han</td>
				<td>Spring 2016</td>
				<td>3D Printing and Mold Making</td>
			</tr>			
			<tr>
				<td>Tanya Parshakova</td>
				<td>2015 - 2016</td>
				<td><a href = "../projects/ratchair/">RatChair</a></td>
			</tr>
			<tr>
				<td>Sangyeob Lee</td>
				<td>Summer 2015</td>
				<td>Interactive Camera System Interface</td>
			</tr>
			<tr>
				<td>Seoyoung Baek and Joonhee Min</td>
				<td>Summer 2015</td>
				<td>Surface Texturing in 3D Printing</td>
			</tr>
			<tr>
				<td>Alex Balio and Sam Ukolov</td>
				<td>2014 - 2015</td>
				<td><a href = "../projects/misc/painting_drone.pdf">Painting Drone</a></td>
			</tr>
			<tr>
				<td>Felix Shin</td>
				<td>2013 - 2015</td>
				<td><a href = '../projects/tag_radar/'>TagRadar</a></td>
			</tr>
			<tr>
				<td>Hayeon Jeong</td>
				<td>Winter 2013</td>
				<td><a href = '../projects/i_eng/'>I-Eng</a></td>
			</tr>
		</table>
	</section>
</section>

