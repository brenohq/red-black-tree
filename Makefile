PYTHON=python3
PIP=pip3


run:
	$(PYTHON) scripts/red-black-tree.py

test:
	$(PYTHON) tests/red-black-tree.spec.py
