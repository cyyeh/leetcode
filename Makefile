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
	pylint --disable=R,C --recursive=y .

test:
	pytest -v **/**/*.py

format:
	black **/**/*.py
