# TODO: make gcc-objc separate libobjc
#
Summary:	GNUStep runtime for Objective C
Name:		libobjc2
Version:	1.2
Release:	0.1
License:	MIT
Group:		Development/Libraries
URL:		http://www.gnustep.org/
Source0:	http://download.gna.org/gnustep/libobjc2-1.2.tar.bz2
# Source0-md5:	ef692c6edfdeba360fe714d589552efc
BuildRequires:	gnustep-make
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the 1.2 release of the GNUstep Objective-C runtime (a.k.a.
libobjc2).  This runtime was designed to support the features of Objective-C 2
for use with GNUstep and other Objective-C programs.  This release contains
several bug fixes, and is tested with the current GNUstep trunk, so will be
compatible with the upcoming GNUstep release.

%package devel
Summary:	Development tools for programs using libobjc2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the 1.2 release of the GNUstep Objective-C runtime (a.k.a.
libobjc2).  This runtime was designed to support the features of Objective-C 2
for use with GNUstep and other Objective-C programs.  This release contains
several bug fixes, and is tested with the current GNUstep trunk, so will be
compatible with the upcoming GNUstep release.

This package contains the header files and libraries needed for
developing programs using the libobjc2 library.

%prep
%setup -q

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
%{__make} -j1 \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} -j1 install \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=$RPM_BUILD_ROOT 

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_libdir}/libobjc.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/objc/*.h
%{_libdir}/libobjc.so
