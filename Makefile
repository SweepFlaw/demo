.PHONY: default, install, demo

default:
	@echo "[USAGE: 'make install', 'make demo']"

install:
	git clone https://github.com/SweepFlaw/position-learning.git
	python3 position-learning/setup.py install --user

demo:
	python3 app.py demodata/wrongCode1.cpp demodata/TC_1204B/input demodata/TC_1204B/output
