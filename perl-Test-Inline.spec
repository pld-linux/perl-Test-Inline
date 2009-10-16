#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Inline
Summary:	Test::inline Perl module - embedded tests
Summary(pl.UTF-8):	Moduł Perla Test::Inline - wbudowane testy
Name:		perl-Test-Inline
Version:	2.211
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	214c841a80f9650dd6b73c422221a22d
URL:		http://search.cpan.org/dist/Test-Inline/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Algorithm-Dependency
BuildRequires:	perl-Class-Autouse
BuildRequires:	perl-File-chmod
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-File-Flat
BuildRequires:	perl-File-Remove >= 0.38
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Params-Util
BuildRequires:	perl-Test-ClassAPI
BuildRequires:	perl-Test-Script
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Inline Perl module provides utility functions to embedded tests.

%description -l pl.UTF-8
Moduł Perla Test::Data udostępnia funkcje pomocnicze do wbudowanych
testów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/inline2test
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Inline
%{_mandir}/man[13]/*
