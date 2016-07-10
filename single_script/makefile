default: help

WANTED_PYTHON = python2
SYS_PYTHON = $(shell which $(WANTED_PYTHON))
#
VE_DIR = venv
TESTS_DIR = tests
BUILD_DIR = build
#
BIN_DIR = $(VE_DIR)/bin
PYTHON_CMD = $(BIN_DIR)/python
PIP_CMD = $(BIN_DIR)/pip
NOSE_CMD = $(BIN_DIR)/nose2
FLAKE8_CMD = $(BIN_DIR)/flake8
#
VE_PYTHON = python2

dev:
ifeq ('venv', $(wildcard $(VE_DIR)))
	$(error Virtual env directory exists.)
endif
	virtualenv --python=$(SYS_PYTHON) $(VE_DIR)
	$(PIP_CMD) install -r requirements.txt
	$(PYTHON_CMD) setup.py develop

test:
	$(PYTHON_CMD) setup.py flake8
	$(PYTHON_CMD) setup.py test

versions:
	$(PIP_CMD) freeze

# Yes, it sucks this isn't the same as above.
# I'll fix it eventually.
# TODO(craig) use setup.py in 'test_verbose'
test_verbose:
	$(PYTHON_CMD) setup.py flake8
	$(NOSE_CMD) --verbose

info:
	$(PYTHON_CMD) setup.py info

clean:
	rm -rf $(BUILD_DIR)
	rm -rf $(VE_DIR)
	rm -rf *.egg
	find . -depth -name __pycache__ -exec rm -rf {} \;

help:
	@echo "Please choose from the following:"
	@echo "	dev	Create virtualenv and populate"
	@echo "	clean	Remove dev dirs ($(VENV_DIR))"
	@echo "	test	Run unit tests"
	@echo "	info	Print package information"
	@echo "	help	This message"
# End of file.
