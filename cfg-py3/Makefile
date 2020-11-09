default: help

VE_DIR = venv
BIN_DIR = $(VE_DIR)/bin
PIP_CMD = $(BIN_DIR)/pip3
PYTHON_CMD = $(BIN_DIR)/python3
BUILD_DIR = build
DIST_DIR = dist
#
SYS_PYTHON_CMD = $(shell which python3)

dev:
	@echo "Creating virtualenv with: $(SYS_PYTHON_CMD)"
	$(SYS_PYTHON_CMD) -m venv $(VE_DIR)
	$(PIP_CMD) install --upgrade pip wheel setuptools
	$(PYTHON_CMD) setup.py develop

clean:
	rm -rf $(VE_DIR)
	rm -rf $(BUILD_DIR)
	rm -rf $(DIST_DIR)

help:
	@echo "Choose from the following:"
	@echo "	dev	Create virtualenv"
	@echo "	clean	Remove virtualenv, build and dist dirs"
	@echo "	help	This message"
