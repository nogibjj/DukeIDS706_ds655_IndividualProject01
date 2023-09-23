#Adding this to install all the packages in requirements.txt - I have not included versions of the individual packages in the requirements file
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

#Adding this to format code using black
format:	
	nbqa black  Codes/*.ipynb &&\
		black Codes/*.py

test:
	python -m py.test --nbval Codes/test_*.ipynb 
	python -m py.test -vv --cov=python_script Codes/*.py
	python -m py.test -vv --cov=lib

lint:
	nbqa ruff Codes/*.ipynb &&\
		ruff check Codes/*.py

all: install format lint test
