VENV=.venv
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
PYTEST=$(CURDIR)/$(VENV)/bin/pytest --disable-warnings

.PHONY: venv deps test_all test_unit cov clean rgr

venv:
	python -m venv $(VENV)

deps: venv
	$(PIP) install -r requirements.txt

# Ejecuta pytest en cada sub-actividad
test_all: deps
	cd soluciones/aserciones_pruebas   && $(PYTEST) -q || exit 1
	cd soluciones/pruebas_pytest       && $(PYTEST) -q || exit 1
	cd soluciones/pruebas_fixtures     && $(PYTEST) -q || exit 1
	cd soluciones/coverage_pruebas     && $(PYTEST) --cov=models --cov-report term-missing -q || exit 1
	cd soluciones/factories_fakes      && $(PYTEST) -q || exit 1
	cd soluciones/mocking_objetos      && $(PYTEST) -q || exit 1
	cd soluciones/practica_tdd         && $(PYTEST) -q || exit 1

# Atajo para correr sólo unidad si decides marcar tests con -m "unit"
test_unit:
	cd soluciones && $(PYTEST) -m "unit" -q

# Cobertura sólo para coverage_pruebas (puedes extender a otras)
cov:
	cd soluciones/coverage_pruebas && $(PYTEST) --cov=models --cov-report term-missing -q

clean:
	rm -rf .pytest_cache **/__pycache__ htmlcov .coverage

# Simula el ciclo Red-Green-Refactor
rgr: deps
	@echo "RED: Modificando funciones para que fallen"
	@cd soluciones/practica_tdd && \
		cp counter.py counter.py.bak && \
		cp status.py status.py.bak && \
		printf '%s\n' \
			'import status' \
			'from flask import Flask' \
			'app = Flask(__name__)' \
			'COUNTERS = {}' \
			'@app.route("/counters/<name>", methods=["POST"])' \
			'def create_counter(name):' \
			'    return {"message": "error"}, status.HTTP_404_NOT_FOUND' \
			'@app.route("/counters/<name>", methods=["PUT"])' \
			'def update_counter(name):' \
			'    return {"message": "error"}, status.HTTP_404_NOT_FOUND' \
			'@app.route("/counters/<name>", methods=["GET"])' \
			'def read_counter(name):' \
			'    return {"message": "error"}, status.HTTP_404_NOT_FOUND' \
			'@app.route("/counters/<name>", methods=["DELETE"])' \
			'def delete_counter(name):' \
			'    return {"message": "error"}, status.HTTP_404_NOT_FOUND' \
			> counter.py && \
		$(PYTEST) -q || echo "✓ Tests fallaron como esperado (RED)"
	@echo ""
	@echo "GREEN: Restaurando implementaciones correctas"
	@cd soluciones/practica_tdd && \
		mv counter.py.bak counter.py && \
		mv status.py.bak status.py && \
		$(PYTEST) -q && echo "✓ Tests pasaron (GREEN)"