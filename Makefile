all: requirements install unittest flake8 xcop

clean:
	rm -rf build
	rm -rf pyeo.egg-info
	rm -rf dist
	rm -rf sphinx html

requirements:
	pip3 install -r requirements.txt
	gem install xcop

unittest:
	python3 -m coverage run -m unittest discover
	python3 pyeo --version

install:
	pip3 install .

xcop:
	xcop $(find . -name '*.xml')

flake8:
	python3 -m flake8 pyeo test setup.py

doc:
	rm -rf sphinx html
	sphinx-apidoc -o sphinx pyeo --full
	sphinx-build sphinx html

