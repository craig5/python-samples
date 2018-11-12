default: help

WANTED_PYTHON = python3
SYS_PYTHON_CMD = $(shell which $(WANTED_PYTHON))
#
VE_DIR = venv
BIN_DIR = $(VE_DIR)/bin
BUILD_DIR = build
DIST_DIR = dist
PYTHON_CMD = $(BIN_DIR)/python3
PIP_CMD = $(BIN_DIR)/pip3
#
FLAKE8_CMD = $(BIN_DIR)/flake8

# for testing install
INSTALL_DIR = install


dev:
	$(SYS_PYTHON_CMD) -m venv $(VE_DIR)
	$(PIP_CMD) install --upgrade pip setuptools wheel
	$(PIP_CMD) install flake8
	$(PYTHON_CMD) setup.py develop

versions:
	$(PIP_CMD) freeze

clean:
	rm -rf $(INSTALL_DIR)
	rm -rf $(BUILD_DIR)
	rm -rf $(DIST_DIR)
	rm -rf $(VE_DIR)
	rm -rf *.egg-info
	find . -depth -name __pycache__ -exec rm -rf {} \;

test:
	$(FLAKE8_CMD) my-script
	$(FLAKE8_CMD) setup.py

test-install:
	$(SYS_PYTHON_CMD) -m venv $(INSTALL_DIR)
	$(PYTHON_CMD) setup.py bdist_wheel
	$(INSTALL_DIR)/bin/pip3 install dist/root_script-0.0.1-py3-none-any.whl
	$(INSTALL_DIR)/bin/my-script.py

help:
	@echo "Please choose from the following:"
	@echo "	dev	Create virtualenv and populate"
	@echo "	clean	Remove dev dirs ($(VENV_DIR))"
	@echo "	test	Run the tests"
	@echo "	install	Test 'pip install' of wheel"
	@echo "	help	This message"
