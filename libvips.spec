%global shortname vips
%global majorminor 8.9
%global soversion 42

Name: libvips
Version: 8.9.0
Release: 1%{?dist}

License: LGPLv2.1+
URL: https://github.com/%{name}/%{name}
Summary: Fast image processing library with low memory needs
Source0: %{url}/releases/download/v%{version}/%{shortname}-%{version}.tar.gz

BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(ImageMagick)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(imagequant)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(openslide)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libgsf-1)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(orc-0.4)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(matio)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(zlib)

BuildRequires: gettext-devel
BuildRequires: giflib-devel
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: gtk-doc
BuildRequires: gcc

%description
Libvips is a demand-driven, horizontally threaded image processing library.
Compared to similar libraries, libvips runs quickly and uses little memory.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development files and headers for fast image processing library with low
memory needs.

%package tools
Summary: Tools for fast image processing library with low memory needs

%description tools
Libvips is a demand-driven, horizontally threaded image processing library.
Compared to similar libraries, libvips runs quickly and uses little memory.

%package doc
Summary: Documentation for fast image processing library with low memory needs
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description doc
Libvips is a demand-driven, horizontally threaded image processing library.
Compared to similar libraries, libvips runs quickly and uses little memory.

%prep
%autosetup -n %{shortname}-%{version}
sed -e 's@#!/usr/bin/python@#!/usr/bin/python3@g' -i tools/vipsprofile

%build
%configure --disable-static --disable-pyvips8
%make_build

%install
%make_install
%find_lang %{shortname}%{majorminor}
rm -f %{buildroot}%{_libdir}/*.la

%files -f %{shortname}%{majorminor}.lang
%doc AUTHORS ChangeLog NEWS THANKS
%license COPYING
%{_libdir}/%{name}*.so.%{soversion}*

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%doc %{_datadir}/gtk-doc/html/%{name}

%files devel
%{_includedir}/%{shortname}/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{shortname}*.pc

%changelog
* Wed Jan 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 8.9.0-1
- Initial SPEC release.
