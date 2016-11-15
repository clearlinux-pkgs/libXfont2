#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXfont2
Version  : 2.0.1
Release  : 1
URL      : https://www.x.org/releases/individual/lib/libXfont2-2.0.1.tar.bz2
Source0  : https://www.x.org/releases/individual/lib/libXfont2-2.0.1.tar.bz2
Summary  : X font Library version 2
Group    : Development/Tools
License  : ICU
Requires: libXfont2-lib
BuildRequires : pkgconfig(fontenc)
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xtrans)
BuildRequires : xmlto

%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font file
formats, and rasterizing them.   It is used by the X servers, the
X Font Server (xfs), and some font utilities (bdftopcf for instance),
but should not be used by normal X11 clients.  X11 clients access fonts
via either the new API's in libXft, or the legacy API's in libX11.

%package dev
Summary: dev components for the libXfont2 package.
Group: Development
Requires: libXfont2-lib
Provides: libXfont2-devel

%description dev
dev components for the libXfont2 package.


%package lib
Summary: lib components for the libXfont2 package.
Group: Libraries

%description lib
lib components for the libXfont2 package.


%prep
%setup -q -n libXfont2-2.0.1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/fonts/libxfont2.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
