%define url_ver %(echo %{version} | cut -d "." -f -2)

Name:		zenity
Summary:	Call GNOME dialog boxes from the command line
Version:	3.28.1
Release:	2%{?dist}
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
URL:		https://download.gnome.org/sources/%{name}
License:	LGPLv2+
Group:		Development/GNOME and GTK+
BuildRequires:  gnome-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libnotify) >= 0.6.1
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	intltool >= 0.40.0
BuildRequires:	itstool
BuildRequires:	libxslt-proc
BuildRequires:	libxml2-utils
BuildRequires:	yelp-tools
Conflicts:	gnome-utils < 2.3.3
Provides:	xmsg-dialog

%description
Zenity allows you to display dialog boxes from the commandline and shell
scripts.

%prep
%autosetup -p1

%build
# Needed by patch0
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
%make_install

%find_lang %{name}-0.1 --with-gnome --all-name

%files -f %name-0.1.lang
%doc AUTHORS COPYING HACKING NEWS README THANKS TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
* Wed Apr 11 2018 Jeremiah Summers <jsummers@glynlyon.com> 3.28.1-2
- new package built with tito
- Bump for rebuild

