#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Inline
Summary:	Test::inline Perl module - Embedded tests
Summary(pl):	Modu³ Perla Test::Inline - funkcje testuj±ce 
Name:		perl-Test-Inline
Version:	0.15
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Inline Perl module provides utility functions to embedded tests

%description -l pl
Modu³ Perla Test::Data udostêpnia funkcje us³ugowe sprawdzaj±ce

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%dir %{perl_sitelib}/Pod
%{perl_sitelib}/Pod/*.pm
%{_mandir}/man3/*
