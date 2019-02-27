
run :
	python3 app.py

check :
	echo "check"

upload :
	echo "upload"

freeze :
	python3 freeze.py

clean :
	rm index.html people/index.html projects/index.html publications/index.html news/index.html contact/index.html events/index.html
	rm projects/*/index.html
	rm -rdv news/2013 news/2014 news/2015 news/2016 news/2017 news/2018 news/2019 news/2020
	

