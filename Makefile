.PHONY: default, install, demo, fasttest

default:
	@echo "[USAGE: 'make install', 'make demo']"

install:
	git clone https://github.com/SweepFlaw/position-learning.git
	python3 position-learning/setup.py install --user

demo:
	python3 app.py demodata/wrongCode1.cpp demodata/TC_1204B/input demodata/TC_1204B/output tmp/demoResult.json

fasttest:
	python3 app.py demodata/shortWrongCode1.cpp demodata/TC_swc1/input demodata/TC_swc1/output tmp/fasttestResult.json