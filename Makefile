# Define variables
PYTHON := python3
PYTHON_GEN := python
PYTEST := pytest
PIP := pip3
PROJECT_NAME := [Tutorial] Automation Testing using Selenium Python

.PHONY: install
install:
	$(PIP) install -r requirements.txt
	@echo "Set env vars LT_USERNAME & LT_ACCESS_KEY"
    # Procure Username and AccessKey from https://accounts.lambdatest.com/security
    export LT_USERNAME=himanshuj
    export LT_ACCESS_KEY=Ia1Miq

.PHONY: test
test:
    export NODE_ENV = test

.PHONY: test
simple_selenium_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/1_simple_selenium_test.py

keyboard_interactions_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no -n 2 tests/pytest/2_keyboard_interactions.py

switch_tabs_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/3_switch_tabs_test.py

locating_web_elements_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/4_locating_web_elements.py

handling_dropdowns_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/5_handling_dropdowns.py

handling_radio_buttons_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/6_handling_radio_buttons.py

locating_check_boxes_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/7_handling_check_boxes.py

handling_alerts_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/8_handling_alerts.py

handling_iframes_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/9_handling_iframes.py

mouse_interactions_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no -n 2 tests/pytest/10_mouse_interactions.py

bitcoin_click_test:
	- echo $(EXEC_PLATFORM)
	- $(PYTEST) --verbose --capture=no tests/pytest/11_bitcoin_click_test.py

simple_selenium_demo:
	- echo "Pytest Selenium Demo"
	- $(PYTEST) --verbose --capture=no tests/pytest/pytest_selenium_demo.py
	- echo "PyUnit Selenium Demo"
	- $(PYTHON_GEN) tests/pyunit/pyunit_selenium_demo.py

.PHONY: clean
clean:
    # This helped: https://gist.github.com/hbsdev/a17deea814bc10197285
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@echo "Clean Succeded"

	find . | grep -E "(.DS_Store)" | xargs rm -rf
	@echo "Clean of DS_Store Succeded"

	find . | grep -E "(.cache)" | xargs rm -rf
	@echo "Pytest Cache clean Succeded"

.PHONY: distclean
distclean: clean
	rm -rf venv

.PHONY: help
help:
	@echo ""
	@echo "install : Install project dependencies"
	@echo "clean : Clean up temp files"
	@echo "simple_selenium_test : Execution simple Selenium Python test"
	@echo "keyboard_interactions_test : Automating keyboard interactions"
	@echo "switch_tabs_test : Demonstration of switching tabs & windows"
	@echo "locating_web_elements_test : Locating WebElements in Selenium Python"
	@echo "handling_dropdowns_test : Handling Dropdowns"
	@echo "handling_radio_buttons_test : Handling RadioButtons"
	@echo "locating_check_boxes_test : Locating & Interacting with Checkboxes"
	@echo "handling_alerts_test : Locating & Interacting with Alerts"
	@echo "handling_iframes_test : Handling Frames & iFrames"
	@echo "mouse_interactions_test : Automating Mouse Interactions"