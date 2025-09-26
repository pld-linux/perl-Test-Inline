#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	Inline
Summary:	Test::inline Perl module - embedded tests
Summary(pl.UTF-8):	Moduł Perla Test::Inline - wbudowane testy
Name:		perl-Test-Inline
Version:	2.214
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c6471fa326d64f649bb0b9298730c9e
URL:		https://metacpan.org/dist/Test-Inline
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Getopt::Long) >= 2.34
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Algorithm-Dependency >= 1.02
BuildRequires:	perl-Config-Tiny >= 2.00
BuildRequires:	perl-File-Find-Rule >= 0.26
BuildRequires:	perl-File-Flat >= 1.00
BuildRequires:	perl-File-Remove >= 0.38
BuildRequires:	perl-File-chmod >= 0.31
BuildRequires:	perl-Params-Util >= 0.21
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Scalar-List-Utils >= 1.19
BuildRequires:	perl-Test-ClassAPI >= 1.02
BuildRequires:	perl-Test-Script >= 1.02
BuildRequires:	perl-Test-Simple >= 0.42
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
%{perl_vendorlib}/Test/Inline.pm
%{perl_vendorlib}/Test/Inline
%{_mandir}/man1/inline2test.1p*
%{_mandir}/man3/Test::Inline*.3pm*
