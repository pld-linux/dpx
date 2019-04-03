%define	rel 	4
%define	subver	svn4
Summary:	SMPTE DPX v2 Image Format reader/writer library
Summary(pl.UTF-8):	Biblioteka do odczytu/zapisu obrazów w formacie SMPTE DPX v2
Name:		dpx
Version:	0.5
Release:	0.%{subver}.%{rel}
License:	BSD
Group:		Libraries
# originally: svn checkout http://dpx.googlecode.com/svn/trunk/ dpx
Source0:	%{name}-%{subver}.tar.xz
# Source0-md5:	a6bf177cb29eaaefb5208f3dcf486658
Patch0:		%{name}-shared.patch
URL:		https://github.com/patrickpalmer/dpx
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMPTE DPX v2 Image Format reader/writer library written in portable
C++.

%description -l pl.UTF-8
Biblioteka do odczytu/zapisu obrazów w formacie SMPTE DPX v2, napisana
w przenośnym C++.

%package devel
Summary:	Header files for DPX library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki DPX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for DPX library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki DPX.

%package static
Summary:	Static DPX library
Summary(pl.UTF-8):	Statyczna biblioteka DPX
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static DPX library.

%description static -l pl.UTF-8
Statyczna biblioteka DPX.

%package apidocs
Summary:	DPX API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki DPX
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for DPX library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki DPX.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/dpx2tiff
%attr(755,root,root) %{_bindir}/dpxheader
%attr(755,root,root) %{_libdir}/libdpx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdpx.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdpx.so
%{_libdir}/libdpx.la
%{_includedir}/DPX*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdpx.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,png}
