#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Inline
Summary:	Test::inline Perl module - Embedded tests
Summary(pl):	Modu³ Perla Test::Inline - wbudowane testy
Name:		perl-Test-Inline
Version:	0.15
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Inline Perl module provides utility functions to embedded tests.

%description -l pl
Modu³ Perla Test::Data udostêpnia funkcje pomocnicze do wbudowanych
testów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Test/*.pm
%dir %{perl_sitelib}/Test/Inline
%{perl_sitelib}/Pod/*.pm
%{_mandir}/man3/*
