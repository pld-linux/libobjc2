# TODO: make gcc-objc separate libobjc
# - separate libobjcxx? (requires libstdc++ while libobjc doesn't)
# - use -DLIBOBJC_NAME=objc2 to allow parallel installation with gcc's libobjc?
#
Summary:	GNUStep runtime for Objective C
Summary(pl.UTF-8):	Biblioteka uruchomieniowa dla Objective C z projektu GNUstep
Name:		libobjc2
Version:	1.7
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://download.gna.org/gnustep/%{name}-%{version}.tar.bz2
# Source0-md5:	7bd9f154ed2f78b3cf55ede7dea536bd
Patch0:		%{name}-link.patch
URL:		http://www.gnustep.org/
BuildRequires:	clang
BuildRequires:	cmake >= 2.8
BuildRequires:	gnustep-make
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNUstep Objective-C runtime (a.k.a. libobjc2). This
runtime was designed to support the features of Objective-C 2 for use
with GNUstep and other Objective-C programs.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę uruchomieniową Objective-C z projektu
GNUstep (znaną także jako libobjc2). Ta biblioteka została
zaprojektowana, aby wspierać cechy języka Objective-C 2, w celu
używania w GNUstepie i innych programach w Objective-C.

%package devel
Summary:	Development files for programs using libobjc2
Summary(pl.UTF-8):	Pliki programistyczne do biblioteki libobjc2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed for developing programs
using the libobjc2 library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do tworzenia programów
wykorzystujących bibliotekę libobjc2.

%package static
Summary:	Static libobjc2 library
Summary(pl.UTF-8):	Statyczna biblioteka libobjc2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libobjc2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libobjc2.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_STATIC_LIBOBJC=ON \
	-DCMAKE_C_COMPILER="clang" \
	-DCMAKE_CXX_COMPILER="clang++" \
	-DGNUSTEP_INSTALL_TYPE=SYSTEM

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE* API COPYING README
%attr(755,root,root) %{_libdir}/libobjc.so.*.*
%attr(755,root,root) %{_libdir}/libobjcxx.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobjc.so
%attr(755,root,root) %{_libdir}/libobjcxx.so
%{_includedir}/objc

%files static
%defattr(644,root,root,755)
%{_libdir}/libobjc.a
