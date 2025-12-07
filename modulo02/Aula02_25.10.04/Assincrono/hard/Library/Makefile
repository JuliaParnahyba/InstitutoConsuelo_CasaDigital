run:
	@python3 main.py

lint:
	@flake8 .

format:
	@black .

clean:
	@find . -type f -name "*.pyc" -delete

reset-data:
	@rm -f data/livros.json data/usuarios.json

install:
	@pip install -r requirements.txt

.PHONY: run lint format clean reset-data install
