ROOT_DIR := $(abspath $(lastword $(MAKEFILE_LIST)))
DEFAULT_GOAL := build

default: test build

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  test    			to run tests using pytest"
	@echo "  build    			to run the tests and then build the project"

.PHONY: test
test:
	python3.6 setup.py test

.PHONY: build
build:
	python3.6 setup.py build

.PHONY: install
install:
	python3.6 setup.py install
