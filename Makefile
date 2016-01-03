all:
	python2 scripts/process.py

clean:
	rm data/* cache/*

.PHONY: clean
