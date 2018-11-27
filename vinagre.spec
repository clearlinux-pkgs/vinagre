#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vinagre
Version  : 3.22.0
Release  : 7
URL      : https://download.gnome.org/sources/vinagre/3.22/vinagre-3.22.0.tar.xz
Source0  : https://download.gnome.org/sources/vinagre/3.22/vinagre-3.22.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: vinagre-bin = %{version}-%{release}
Requires: vinagre-data = %{version}-%{release}
Requires: vinagre-license = %{version}-%{release}
Requires: vinagre-locales = %{version}-%{release}
Requires: vinagre-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk-vnc-2.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(spice-client-gtk-3.0)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : sed

%description
Vinagre
=======
This is Vinagre, a remote desktop viewer for the GNOME Desktop.
You can download or see more information about it on:
https://wiki.gnome.org/Apps/Vinagre

%package bin
Summary: bin components for the vinagre package.
Group: Binaries
Requires: vinagre-data = %{version}-%{release}
Requires: vinagre-license = %{version}-%{release}
Requires: vinagre-man = %{version}-%{release}

%description bin
bin components for the vinagre package.


%package data
Summary: data components for the vinagre package.
Group: Data

%description data
data components for the vinagre package.


%package doc
Summary: doc components for the vinagre package.
Group: Documentation
Requires: vinagre-man = %{version}-%{release}

%description doc
doc components for the vinagre package.


%package license
Summary: license components for the vinagre package.
Group: Default

%description license
license components for the vinagre package.


%package locales
Summary: locales components for the vinagre package.
Group: Default

%description locales
locales components for the vinagre package.


%package man
Summary: man components for the vinagre package.
Group: Default

%description man
man components for the vinagre package.


%prep
%setup -q -n vinagre-3.22.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543349259
%configure --disable-static --with-ssh
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1543349259
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vinagre
cp COPYING %{buildroot}/usr/share/package-licenses/vinagre/COPYING
%make_install
%find_lang vinagre

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vinagre

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/org.gnome.Vinagre.convert
/usr/share/appdata/vinagre.appdata.xml
/usr/share/applications/vinagre-file.desktop
/usr/share/applications/vinagre.desktop
/usr/share/glib-2.0/schemas/org.gnome.Vinagre.gschema.xml
/usr/share/icons/hicolor/16x16/mimetypes/application-x-remote-connection.png
/usr/share/icons/hicolor/16x16/mimetypes/application-x-vnc.png
/usr/share/icons/hicolor/16x16/status/view-minimize.png
/usr/share/icons/hicolor/22x22/mimetypes/application-x-remote-connection.png
/usr/share/icons/hicolor/22x22/mimetypes/application-x-vnc.png
/usr/share/icons/hicolor/22x22/status/view-minimize.png
/usr/share/icons/hicolor/24x24/mimetypes/application-x-remote-connection.png
/usr/share/icons/hicolor/24x24/mimetypes/application-x-vnc.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-remote-connection.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-vnc.png
/usr/share/icons/hicolor/32x32/status/view-minimize.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-remote-connection.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-vnc.png
/usr/share/icons/hicolor/48x48/status/view-minimize.png
/usr/share/icons/hicolor/scalable/mimetypes/application-x-remote-connection.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-vnc.svg
/usr/share/mime-packages/vinagre-mime.xml
/usr/share/vinagre/vinagre-ui.xml
/usr/share/vinagre/vinagre.ui

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/vinagre/connect-file.page
/usr/share/help/C/vinagre/connect-reverse.page
/usr/share/help/C/vinagre/connect.page
/usr/share/help/C/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/C/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/C/vinagre/fullscreen.page
/usr/share/help/C/vinagre/index.page
/usr/share/help/C/vinagre/introduction.page
/usr/share/help/C/vinagre/keyboard-shortcuts.page
/usr/share/help/C/vinagre/legal.xml
/usr/share/help/C/vinagre/scaling.page
/usr/share/help/C/vinagre/take-screenshot.page
/usr/share/help/C/vinagre/view-only.page
/usr/share/help/cs/vinagre/connect-file.page
/usr/share/help/cs/vinagre/connect-reverse.page
/usr/share/help/cs/vinagre/connect.page
/usr/share/help/cs/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/cs/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/cs/vinagre/fullscreen.page
/usr/share/help/cs/vinagre/index.page
/usr/share/help/cs/vinagre/introduction.page
/usr/share/help/cs/vinagre/keyboard-shortcuts.page
/usr/share/help/cs/vinagre/legal.xml
/usr/share/help/cs/vinagre/scaling.page
/usr/share/help/cs/vinagre/take-screenshot.page
/usr/share/help/cs/vinagre/view-only.page
/usr/share/help/de/vinagre/connect-file.page
/usr/share/help/de/vinagre/connect-reverse.page
/usr/share/help/de/vinagre/connect.page
/usr/share/help/de/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/de/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/de/vinagre/fullscreen.page
/usr/share/help/de/vinagre/index.page
/usr/share/help/de/vinagre/introduction.page
/usr/share/help/de/vinagre/keyboard-shortcuts.page
/usr/share/help/de/vinagre/legal.xml
/usr/share/help/de/vinagre/scaling.page
/usr/share/help/de/vinagre/take-screenshot.page
/usr/share/help/de/vinagre/view-only.page
/usr/share/help/el/vinagre/connect-file.page
/usr/share/help/el/vinagre/connect-reverse.page
/usr/share/help/el/vinagre/connect.page
/usr/share/help/el/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/el/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/el/vinagre/fullscreen.page
/usr/share/help/el/vinagre/index.page
/usr/share/help/el/vinagre/introduction.page
/usr/share/help/el/vinagre/keyboard-shortcuts.page
/usr/share/help/el/vinagre/legal.xml
/usr/share/help/el/vinagre/scaling.page
/usr/share/help/el/vinagre/take-screenshot.page
/usr/share/help/el/vinagre/view-only.page
/usr/share/help/es/vinagre/connect-file.page
/usr/share/help/es/vinagre/connect-reverse.page
/usr/share/help/es/vinagre/connect.page
/usr/share/help/es/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/es/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/es/vinagre/fullscreen.page
/usr/share/help/es/vinagre/index.page
/usr/share/help/es/vinagre/introduction.page
/usr/share/help/es/vinagre/keyboard-shortcuts.page
/usr/share/help/es/vinagre/legal.xml
/usr/share/help/es/vinagre/scaling.page
/usr/share/help/es/vinagre/take-screenshot.page
/usr/share/help/es/vinagre/view-only.page
/usr/share/help/eu/vinagre/connect-file.page
/usr/share/help/eu/vinagre/connect-reverse.page
/usr/share/help/eu/vinagre/connect.page
/usr/share/help/eu/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/eu/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/eu/vinagre/fullscreen.page
/usr/share/help/eu/vinagre/index.page
/usr/share/help/eu/vinagre/introduction.page
/usr/share/help/eu/vinagre/keyboard-shortcuts.page
/usr/share/help/eu/vinagre/legal.xml
/usr/share/help/eu/vinagre/scaling.page
/usr/share/help/eu/vinagre/take-screenshot.page
/usr/share/help/eu/vinagre/view-only.page
/usr/share/help/fa/vinagre/connect-file.page
/usr/share/help/fa/vinagre/connect-reverse.page
/usr/share/help/fa/vinagre/connect.page
/usr/share/help/fa/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/fa/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/fa/vinagre/fullscreen.page
/usr/share/help/fa/vinagre/index.page
/usr/share/help/fa/vinagre/introduction.page
/usr/share/help/fa/vinagre/keyboard-shortcuts.page
/usr/share/help/fa/vinagre/legal.xml
/usr/share/help/fa/vinagre/scaling.page
/usr/share/help/fa/vinagre/take-screenshot.page
/usr/share/help/fa/vinagre/view-only.page
/usr/share/help/fr/vinagre/connect-file.page
/usr/share/help/fr/vinagre/connect-reverse.page
/usr/share/help/fr/vinagre/connect.page
/usr/share/help/fr/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/fr/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/fr/vinagre/fullscreen.page
/usr/share/help/fr/vinagre/index.page
/usr/share/help/fr/vinagre/introduction.page
/usr/share/help/fr/vinagre/keyboard-shortcuts.page
/usr/share/help/fr/vinagre/legal.xml
/usr/share/help/fr/vinagre/scaling.page
/usr/share/help/fr/vinagre/take-screenshot.page
/usr/share/help/fr/vinagre/view-only.page
/usr/share/help/gl/vinagre/connect-file.page
/usr/share/help/gl/vinagre/connect-reverse.page
/usr/share/help/gl/vinagre/connect.page
/usr/share/help/gl/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/gl/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/gl/vinagre/fullscreen.page
/usr/share/help/gl/vinagre/index.page
/usr/share/help/gl/vinagre/introduction.page
/usr/share/help/gl/vinagre/keyboard-shortcuts.page
/usr/share/help/gl/vinagre/legal.xml
/usr/share/help/gl/vinagre/scaling.page
/usr/share/help/gl/vinagre/take-screenshot.page
/usr/share/help/gl/vinagre/view-only.page
/usr/share/help/hu/vinagre/connect-file.page
/usr/share/help/hu/vinagre/connect-reverse.page
/usr/share/help/hu/vinagre/connect.page
/usr/share/help/hu/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/hu/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/hu/vinagre/fullscreen.page
/usr/share/help/hu/vinagre/index.page
/usr/share/help/hu/vinagre/introduction.page
/usr/share/help/hu/vinagre/keyboard-shortcuts.page
/usr/share/help/hu/vinagre/legal.xml
/usr/share/help/hu/vinagre/scaling.page
/usr/share/help/hu/vinagre/take-screenshot.page
/usr/share/help/hu/vinagre/view-only.page
/usr/share/help/id/vinagre/connect-file.page
/usr/share/help/id/vinagre/connect-reverse.page
/usr/share/help/id/vinagre/connect.page
/usr/share/help/id/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/id/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/id/vinagre/fullscreen.page
/usr/share/help/id/vinagre/index.page
/usr/share/help/id/vinagre/introduction.page
/usr/share/help/id/vinagre/keyboard-shortcuts.page
/usr/share/help/id/vinagre/legal.xml
/usr/share/help/id/vinagre/scaling.page
/usr/share/help/id/vinagre/take-screenshot.page
/usr/share/help/id/vinagre/view-only.page
/usr/share/help/lv/vinagre/connect-file.page
/usr/share/help/lv/vinagre/connect-reverse.page
/usr/share/help/lv/vinagre/connect.page
/usr/share/help/lv/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/lv/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/lv/vinagre/fullscreen.page
/usr/share/help/lv/vinagre/index.page
/usr/share/help/lv/vinagre/introduction.page
/usr/share/help/lv/vinagre/keyboard-shortcuts.page
/usr/share/help/lv/vinagre/legal.xml
/usr/share/help/lv/vinagre/scaling.page
/usr/share/help/lv/vinagre/take-screenshot.page
/usr/share/help/lv/vinagre/view-only.page
/usr/share/help/pt_BR/vinagre/connect-file.page
/usr/share/help/pt_BR/vinagre/connect-reverse.page
/usr/share/help/pt_BR/vinagre/connect.page
/usr/share/help/pt_BR/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/pt_BR/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/pt_BR/vinagre/fullscreen.page
/usr/share/help/pt_BR/vinagre/index.page
/usr/share/help/pt_BR/vinagre/introduction.page
/usr/share/help/pt_BR/vinagre/keyboard-shortcuts.page
/usr/share/help/pt_BR/vinagre/legal.xml
/usr/share/help/pt_BR/vinagre/scaling.page
/usr/share/help/pt_BR/vinagre/take-screenshot.page
/usr/share/help/pt_BR/vinagre/view-only.page
/usr/share/help/ru/vinagre/connect-file.page
/usr/share/help/ru/vinagre/connect-reverse.page
/usr/share/help/ru/vinagre/connect.page
/usr/share/help/ru/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/ru/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/ru/vinagre/fullscreen.page
/usr/share/help/ru/vinagre/index.page
/usr/share/help/ru/vinagre/introduction.page
/usr/share/help/ru/vinagre/keyboard-shortcuts.page
/usr/share/help/ru/vinagre/legal.xml
/usr/share/help/ru/vinagre/scaling.page
/usr/share/help/ru/vinagre/take-screenshot.page
/usr/share/help/ru/vinagre/view-only.page
/usr/share/help/sl/vinagre/connect-file.page
/usr/share/help/sl/vinagre/connect-reverse.page
/usr/share/help/sl/vinagre/connect.page
/usr/share/help/sl/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/sl/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/sl/vinagre/fullscreen.page
/usr/share/help/sl/vinagre/index.page
/usr/share/help/sl/vinagre/introduction.page
/usr/share/help/sl/vinagre/keyboard-shortcuts.page
/usr/share/help/sl/vinagre/legal.xml
/usr/share/help/sl/vinagre/scaling.page
/usr/share/help/sl/vinagre/take-screenshot.page
/usr/share/help/sl/vinagre/view-only.page
/usr/share/help/sv/vinagre/connect-file.page
/usr/share/help/sv/vinagre/connect-reverse.page
/usr/share/help/sv/vinagre/connect.page
/usr/share/help/sv/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/sv/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/sv/vinagre/fullscreen.page
/usr/share/help/sv/vinagre/index.page
/usr/share/help/sv/vinagre/introduction.page
/usr/share/help/sv/vinagre/keyboard-shortcuts.page
/usr/share/help/sv/vinagre/legal.xml
/usr/share/help/sv/vinagre/scaling.page
/usr/share/help/sv/vinagre/take-screenshot.page
/usr/share/help/sv/vinagre/view-only.page
/usr/share/help/zh_CN/vinagre/connect-file.page
/usr/share/help/zh_CN/vinagre/connect-reverse.page
/usr/share/help/zh_CN/vinagre/connect.page
/usr/share/help/zh_CN/vinagre/figures/preferences-desktop-remote-desktop.png
/usr/share/help/zh_CN/vinagre/figures/vinagre-connected-3-16.png
/usr/share/help/zh_CN/vinagre/fullscreen.page
/usr/share/help/zh_CN/vinagre/index.page
/usr/share/help/zh_CN/vinagre/introduction.page
/usr/share/help/zh_CN/vinagre/keyboard-shortcuts.page
/usr/share/help/zh_CN/vinagre/legal.xml
/usr/share/help/zh_CN/vinagre/scaling.page
/usr/share/help/zh_CN/vinagre/take-screenshot.page
/usr/share/help/zh_CN/vinagre/view-only.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vinagre/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/vinagre.1

%files locales -f vinagre.lang
%defattr(-,root,root,-)

