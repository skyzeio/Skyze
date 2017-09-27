# Ref: https://github.com/F483/apigen/blob/master/Makefile

# First command in the make file is the default
help:
	@echo "COMMANDS:"
	@echo "setup		Setup development enviorment"
	@echo "lint			Run analysis tools."
	@echo "test     Run tests."
setup:
	pipenv install
lint: setup
	pipenv run pylint --rcfile=.pylintrc * -f colorized -r y && \
test: setup
