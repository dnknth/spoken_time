GETTEXT = /usr/local/opt/gettext

POT = spoken_time/locale/spoken_time.pot
LOCALE = spoken_time/locale/de/LC_MESSAGES/spoken_time.po


test: $(POT)
	python3 test.py
	
messages: $(POT)

$(POT): test.py spoken_time/__init__.py
	$(GETTEXT)/bin/xgettext -L python -o $@ $^

%.mo: %.po
	$(GETTEXT)/bin/msgfmt -o $@ $<

clean:
	rm -rf __pycache__ $(LOCALE:.po=.mo)
