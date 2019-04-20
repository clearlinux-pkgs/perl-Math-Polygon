#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Polygon
Version  : 1.10
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Math-Polygon-1.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Math-Polygon-1.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-polygon-perl/libmath-polygon-perl_1.10-1.debian.tar.xz
Summary  : 'basic polygon calculations'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
=   Generated on Wed Dec 27 11:14:17 2017 by OODoc 2.02
There are various ways to install this module:

%package dev
Summary: dev components for the perl-Math-Polygon package.
Group: Development
Provides: perl-Math-Polygon-devel = %{version}-%{release}

%description dev
dev components for the perl-Math-Polygon package.


%prep
%setup -q -n Math-Polygon-1.10
cd ..
%setup -q -T -D -n Math-Polygon-1.10 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Math-Polygon-1.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon.pm
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon.pod
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Calc.pm
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Calc.pod
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Clip.pm
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Clip.pod
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Convex.pm
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Convex.pod
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Surface.pm
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Surface.pod
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Transform.pm
/usr/lib/perl5/vendor_perl/5.28.2/Math/Polygon/Transform.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Polygon.3
/usr/share/man/man3/Math::Polygon::Calc.3
/usr/share/man/man3/Math::Polygon::Clip.3
/usr/share/man/man3/Math::Polygon::Convex.3
/usr/share/man/man3/Math::Polygon::Surface.3
/usr/share/man/man3/Math::Polygon::Transform.3
