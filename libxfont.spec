%define major 1
%define libname %mklibname xfont %{major}
%define develname %mklibname xfont -d
%define staticname %mklibname xfont -s -d

Name: libxfont
Summary:  X font Library
Version: 1.4.4
Release: 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2
# submitted upstream as bug #11573
Patch3: libXfont-1.3.4-rescan-catalogue-dir-fontpaths-on-directory-change.patch

BuildRequires: libfontenc-devel >= 1.0.1
BuildRequires: freetype2-devel >= 2.1.10
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0
BuildRequires: bzip2-devel

%description
X font Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X font Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X font Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: libxfont-devel = %{version}-%{release}
Obsoletes: %{_lib}xfont1-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%{_libdir}/libXfont.so
#{_libdir}/libXfont.la
%{_libdir}/pkgconfig/xfont.pc
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libxfont-static-devel = %{version}-%{release}
Obsoletes: %{_lib}xfont1-static-devel
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%{_libdir}/libXfont.a

#-----------------------------------------------------------

%prep
%setup -q -n libXfont-%{version}
%patch3 -p1 -b .check-dirs-mtime

%build
%configure2_5x \
	--with-bzip2 \
	--without-fop
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/libXfont.so.%{major}*

