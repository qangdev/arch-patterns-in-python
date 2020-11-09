env:
	echo "[S T A R T E D]"
	rm -rf venv
	python3.8 -m venv venv
	venv/bin/pip3 install -r requirements.txt
	echo "[D O N E]"