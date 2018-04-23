ROOT_DIR := $(abspath $(lastword $(MAKEFILE_LIST)))
DEFAULT_GOAL := build

default: test build

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  test    						to run tests using pytest"
	@echo "  tox-tests    					to run tests using pytest over python 2.7 and 3.6"
	@echo "  build    						to run the tests and then build the project"
	@echo "  docker-build    				to build docker services."
	@echo "  docker-run    					to run 'http' docke service command 'task2-http-server'."


.PHONY: docker-build
docker-build:
	docker-compose build http

.PHONY: docker-run
docker-run:
	docker-compose up --no-recreate --remove-orphans http

.PHONY: test
test:
	python3.6 setup.py test

.PHONY: tox-tests
tox-tests:
	tox

.PHONY: build
build:
	python3.6 setup.py build

.PHONY: install
install:
	python3.6 setup.py install
