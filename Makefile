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
		python3 src/main.py $(ARGS) \
	)

test:
	( \
		. venv/bin/activate && \
		python3 -m unittest discover -s src/test -p '*_test.py' \
	)

clean:
	if [ -f diffie.db ]; then rm -f diffie.db; fi
