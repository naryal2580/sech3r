DESTDIR ?= /usr/local/bin

install:
	@sudo -H pip3 install -U -r requirements.txt
	@pyinstaller --onefile sech3r.py
	@sudo cp ./dist/sech3r $(DESTDIR)/sech3r
	@echo "\nSeCh3r_v3.0 has been installed sucessfully to PATH."

uninstall:
	@sudo rm -f $(DESTDIR)/sech3r
	@echo "SeCh3r_v3.0 has been sucessfully removed."
