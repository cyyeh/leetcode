build:
	docker build -t python-3.8-slim:latest -f docker/Dockerfile .

run:
	make build && \
	docker run \
	--rm \
	-it \
	-v ${PWD}:/code \
	--name python-3.8-slim \
	python-3.8-slim:latest \
	/bin/bash

rm:
	docker image rm python-3.8-slim:latest python:3.8-slim

lint:
	pylint --disable=R,C **/*.py

test:
	pytest -vv --cov=**/test_*.py **/test_*.py

format:
	black **/*.py
