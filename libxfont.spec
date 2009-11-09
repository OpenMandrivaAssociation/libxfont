%define libxfont %mklibname xfont 1
Name: libxfont
Summary:  X font Library
Version: 1.4.1
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2
# submitted upstream as bug #11573
Patch3: libXfont-1.3.4-rescan-catalogue-dir-fontpaths-on-directory-change.patch
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libfontenc-devel >= 1.0.1
BuildRequires: freetype2-devel >= 2.1.10
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0
BuildRequires: bzip2-devel

%description
X font Library

#-----------------------------------------------------------

%package -n %{libxfont}
Summary:  X font Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}
Requires: x11-font-encodings

%description -n %{libxfont}
X font Library

#-----------------------------------------------------------

%package -n %{libxfont}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxfont} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxfont-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxfont}-devel
Development files for %{name}

%pre -n %{libxfont}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxfont}-devel
%defattr(-,root,root)
%{_libdir}/libXfont.so
%{_libdir}/libXfont.la
%{_libdir}/pkgconfig/xfont.pc
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/*

#-----------------------------------------------------------

%package -n %{libxfont}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxfont}-devel = %{version}
Provides: libxfont-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxfont}-static-devel
Static development files for %{name}

%files -n %{libxfont}-static-devel
%defattr(-,root,root)
%{_libdir}/libXfont.a

#-----------------------------------------------------------

%prep
%setup -q -n libXfont-%{version}
%patch3 -p1 -b .check-dirs-mtime

%build
%configure2_5x \
	--with-encodingsdir=%{_datadir}/fonts/encodings \
	--with-bzip2
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libxfont}
%defattr(-,root,root)
%{_libdir}/libXfont.so.1
%{_libdir}/libXfont.so.1.*
