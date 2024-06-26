help:
	@echo "make [target]"
	@echo "     help		-- Display targets and its functions"
	@echo "     install		-- Install prod requirements"
	@echo "     install@dev	-- Install dev requirements"
	
install:
	@echo "Creating virtual enviroment ..."
	@python -v venv venv
	@echo "Install requirements ..."
	@pip install -r requirements.txt
	
install:
	@echo "Creating dev virtual enviroment ..."
	@python -v venv dev_venv
	@echo "Install dev requirements ..."
	@pip install -r requirements-dev.txt