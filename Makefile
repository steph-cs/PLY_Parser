install_dependecies:
	@python3 -m pip install ply==3.11

build:
	@python3 alas.py ${FILE_PATH}