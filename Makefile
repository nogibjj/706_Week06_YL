install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py mylib/*.py
	ruff check *.py mylib/*.py

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py