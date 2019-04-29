virtualenv:
	echo "Creating virtual environment"
	virtualenv -p python3 venv
	. venv/bin/activate
	echo "Installing python dependencies"
	pip install -r requirements.txt
	echo "Installing node modules"
	npm install