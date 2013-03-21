%define major 1
%define libname %mklibname xfont %{major}
%define develname %mklibname xfont -d

Name:		libxfont
Summary:	X font Library
Version:	1.4.5
Release:	3
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2
Patch0:		libxfont-aarch64.patch
# submitted upstream as bug #11573
Patch3:		libXfont-1.3.4-rescan-catalogue-dir-fontpaths-on-directory-change.patch

BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(xtrans)
BuildRequires:	x11-proto-devel
BuildRequires:	x11-util-macros
BuildRequires:	bzip2-devel

%description
X font Library.

%package -n %{libname}
Summary:	X font Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
X font Library

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxfont-devel = %{version}-%{release}
Obsoletes:	%{_lib}xfont1-devel < 1.4.5
Obsoletes:	%{_lib}xfont-static-devel < 1.4.5
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXfont-%{version}
%patch0 -p1
%patch3 -p1 -b .check-dirs-mtime

%build
%configure2_5x \
	--disable-static \
	--with-bzip2 \
	--without-fop

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXfont.so.%{major}*

%files -n %{develname}
%{_libdir}/libXfont.so
%{_libdir}/pkgconfig/xfont.pc
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/*

