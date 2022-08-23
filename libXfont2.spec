#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : libXfont2
Version  : 2.0.5
Release  : 17
URL      : https://www.x.org/releases/individual/lib/libXfont2-2.0.5.tar.bz2
Source0  : https://www.x.org/releases/individual/lib/libXfont2-2.0.5.tar.bz2
Source1  : https://www.x.org/releases/individual/lib/libXfont2-2.0.5.tar.bz2.sig
Summary  : X font Library version 2
Group    : Development/Tools
License  : ICU
Requires: libXfont2-lib = %{version}-%{release}
Requires: libXfont2-license = %{version}-%{release}
BuildRequires : pkgconfig(fontenc)
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xtrans)
BuildRequires : xmlto

%description
libXfont - X font handling library for server & utilities
---------------------------------------------------------

%package dev
Summary: dev components for the libXfont2 package.
Group: Development
Requires: libXfont2-lib = %{version}-%{release}
Provides: libXfont2-devel = %{version}-%{release}
Requires: libXfont2 = %{version}-%{release}

%description dev
dev components for the libXfont2 package.


%package lib
Summary: lib components for the libXfont2 package.
Group: Libraries
Requires: libXfont2-license = %{version}-%{release}

%description lib
lib components for the libXfont2 package.


%package license
Summary: license components for the libXfont2 package.
Group: Default

%description license
license components for the libXfont2 package.


%prep
%setup -q -n libXfont2-2.0.5
cd %{_builddir}/libXfont2-2.0.5
pushd ..
cp -a libXfont2-2.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656134655
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656134655
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXfont2
cp %{_builddir}/libXfont2-2.0.5/COPYING %{buildroot}/usr/share/package-licenses/libXfont2/2b61cd7d9b22e98804387e896a3cfa382c1bc4ef
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/fonts/libxfont2.h
/usr/lib64/libXfont2.so
/usr/lib64/pkgconfig/xfont2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libXfont2.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libXfont2.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libXfont2.so.2.0.0
/usr/lib64/libXfont2.so.2
/usr/lib64/libXfont2.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXfont2/2b61cd7d9b22e98804387e896a3cfa382c1bc4ef
