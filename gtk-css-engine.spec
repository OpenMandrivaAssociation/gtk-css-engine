%define name gtk-css-engine
%define version 0.1.0
%define release %mkrel 1

%define libname %mklibname %{name}

%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)

Summary: CSS engine for Gtk 2.x
Name:    %{name}
Version: %{version}
Release: %{release}
URL: http://bzr-playground.gnome.org/~robsta/gtk-css-engine/
Source0: http://download.gnome.org/sources/gtk-css-engine/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: 	 Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: %{libname} = %{version}
BuildRequires: gtk2-devel >= 2.12
BuildRequires: librsvg-devel >= 2.16

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
%define _disable_ld_as_needed 1
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_datadir}/themes/*
%_datadir/gtk-doc/html/ccd

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/*.*

