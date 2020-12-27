#######################################################
# preinstall requirements
# 1. install gcc
# 2. install gtk (clibs)
# 3. install vte2.9 (clibs)
#######################################################



CC=gcc

GTKFLAGS=-pthread -I/usr/include/gtk-3.0 -I/usr/include/at-spi2-atk/2.0 -I/usr/include/at-spi-2.0 -I/usr/include/dbus-1.0 -I/usr/lib/x86_64-linux-gnu/dbus-1.0/include -I/usr/include/gtk-3.0 -I/usr/include/gio-unix-2.0 -I/usr/include/cairo -I/usr/include/pango-1.0 -I/usr/include/fribidi -I/usr/include/harfbuzz -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/pixman-1 -I/usr/include/uuid -I/usr/include/freetype2 -I/usr/include/libpng16 -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/libmount -I/usr/include/blkid -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -lgtk-3 -lgdk-3 -lpangocairo-1.0 -lpango-1.0 -lharfbuzz -latk-1.0 -lcairo-gobject -lcairo -lgdk_pixbuf-2.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0

TERMFLAGS=-pthread -I/usr/include/vte-2.91 -I/usr/include/gtk-3.0 -I/usr/include/at-spi2-atk/2.0 -I/usr/include/at-spi-2.0 -I/usr/include/dbus-1.0 -I/usr/lib/x86_64-linux-gnu/dbus-1.0/include -I/usr/include/gtk-3.0 -I/usr/include/gio-unix-2.0 -I/usr/include/cairo -I/usr/include/pango-1.0 -I/usr/include/fribidi -I/usr/include/harfbuzz -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/pixman-1 -I/usr/include/uuid -I/usr/include/freetype2 -I/usr/include/libpng16 -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/libmount -I/usr/include/blkid -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -lvte-2.91 -lgtk-3 -lgdk-3 -lpangocairo-1.0 -lpango-1.0 -lharfbuzz -latk-1.0 -lcairo-gobject -lcairo -lgdk_pixbuf-2.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0

SOURCEINSTALL=install-pck3r-ubuntu/

SOURCEUPDATE=updator-pck3r/

binary=bin/

all: pck3r pck3r-termial-emu pck3r-termial-emu-tilix installer updator

pck3r: core.c
		${CC} -o $(binary)pck3r core.c

pck3r-termial-emu: pck3r-terminal-emu.c
		${CC} -o $(binary)pck3r-terminal-emu-tilix pck3r-terminal-emu-tilix.c

pck3r-termial-emu-tilix: pck3r-terminal-emu-tilix.c
		${CC} pck3r-terminal-emu.c  ${TERMFLAGS}  -o $(binary)pck3r-terminal-emu

installer: $(SOURCEINSTALL)installer.c
		${CC}   $(SOURCEINSTALL)installer.c  ${GTKFLAGS} -o $(SOURCEINSTALL)/installer

updator: $(SOURCEUPDATE)updator.c
		${CC}   $(SOURCEUPDATE)updator.c     ${GTKFLAGS} -o $(SOURCEUPDATE)/updator
		
install:
		./${SOURCEINSTALL}/installer
