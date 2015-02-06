%define name gtk-css-engine
%define version 0.3.1
%define release 3

%define libname %mklibname %{name}

%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)

Summary: CSS engine for Gtk 2.x
Name:    %{name}
Version: %{version}
Release: %{release}
URL: http://bzr-playground.gnome.org/~robsta/gtk-css-engine/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: 	 Graphical desktop/GNOME
Requires: %{libname} = %{version}
BuildRequires: pkgconfig(gtk+-2.0) >= 2.12
BuildRequires: librsvg-devel >= 2.16
BuildRequires: libccss-devel >= 0.5.0
BuildRequires: libccss >= 0.5.0

%description
This is a GTK theme engine that is configured with Cascading Style
Sheets instead of gtkrc files.

%package -n %{libname}
Summary: Library files for %{name}
Group: System/Libraries

%description -n %{libname}
Library files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_sysconfdir}/gtk-css-engine/user-agent.css
%{_datadir}/themes/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/*.*



%changelog
* Sun Aug 14 2011 Götz Waschk <waschk@mandriva.org> 0.3.1-2mdv2012.0
+ Revision: 694487
- rebuild

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 415503
- new version
- update deps
- update source URL

* Sat Aug 01 2009 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2010.0
+ Revision: 405353
- New version 0.3.0

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2009.1
+ Revision: 291926
- new version
- update file list

* Fri Aug 22 2008 Götz Waschk <waschk@mandriva.org> 0.1.0-1mdv2009.0
+ Revision: 275110
- import gtk-css-engine


