%define major 1
%define libname %mklibname xfont %{major}
%define devname %mklibname xfont -d

Summary:	X font Library
Name:		libxfont
Version:	1.5.4
Release:	3
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2
Source1:	libxfont.rpmlintrc
# submitted upstream as bug #11573
Patch3:		libXfont-1.3.4-rescan-catalogue-dir-fontpaths-on-directory-change.patch
Patch4:		libXfont-1.4.8-clang.patch

BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xtrans)

%description
X font Library.

%package -n %{libname}
Summary:	X font Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
X font Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxfont-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXfont-%{version}
%autopatch -p1
autoreconf -fi

%build
%configure \
	--disable-static \
	--with-bzip2 \
	--without-fop

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXfont.so.%{major}*

%files -n %{devname}
%{_libdir}/libXfont.so
%{_libdir}/pkgconfig/xfont.pc
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/*
