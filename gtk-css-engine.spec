%define name gtk-css-engine
%define version 0.3.1
%define release %mkrel 2

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: %{libname} = %{version}
BuildRequires: gtk2-devel >= 2.12
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
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_sysconfdir}/gtk-css-engine/user-agent.css
%{_datadir}/themes/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/*.*

