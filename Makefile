.SILENT:

check:
	./check.sh python3

install: check
	python3 -m venv venv
	( \
		. venv/bin/activate && \
		pip3 install -r requirements.txt \
	)

test: check
	( \
		. venv/bin/activate && \
		python3 -m unittest discover -s src/test -p '*_test.py' \
	)

clean:
	if [ -f diffie.db ]; then rm -f diffie.db; fi
	echo 'OK'
