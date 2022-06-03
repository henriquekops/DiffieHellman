.SILENT:

install:
	python3 -m venv venv
	( \
		. venv/bin/activate && \
		pip3 install -r requirements.txt \
	)

run:
	( \
		. venv/bin/activate && \
		python3 src/main.py \
	)

test:
	( \
		. venv/bin/activate && \
		python3 -m unittest discover -s src/test -p '*_test.py' \
	)
