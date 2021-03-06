ifeq ("$(origin V)", "command line")
    Q=
else
    Q=@
endif
all: configure
	$(Q)./configure

configure: configure.ac
	$(Q)[ -e configure ] && autoreconf || autoconf
clean:
	$(Q)rm -f configure procszoo/c_functions/macros.py
	$(Q)find . -name "*.pyc" | xargs rm -f
	$(Q)find . -name "*~" | xargs rm -f
	$(Q)find . -name "__pycache__" -print0 | xargs -0 rm -rf
	$(Q)rm -rf autom4te.cache config.log config.status
