#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Smart
Summary:	A smart, easy and powerful way to access/create XML files/data
# just waiting for qboosh... ;-)
#Summary(pl):	-
Name:		perl-XML-Smart
Version:	1.5.7
Release:	1
# Same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6e12d6fb90cde55279d57ac81116e7cd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Object-MultiType >= 0.03
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module has an easy way to access/create XML data. It's based on
the HASH tree that is made of the XML data, and enable a dynamic
access to it with the Perl syntax for Hash and Array, without needing
to care if you have a Hash or an Array in the tree. In other words,
each point in the tree work as a Hash and an Array at the same time!

You also have extra resources, like a search for nodes by attribute,
selection of an attribute value in each multiple node, change the
returned format, etc...

#%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:echo n | %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Smart.pm
%{perl_vendorlib}/XML/Smart
%{_mandir}/man3/*
