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
		python3 -m unittest src/test/diffie_test.py && \
		python3 -m unittest src/test/aes_test.py \
	)
