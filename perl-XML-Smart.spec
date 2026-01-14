#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	Smart
Summary:	XML::Smart - a smart, easy and powerful way to access/create XML files/data
Summary(pl.UTF-8):	XML::Smart - zgrabny, łatwy i potężny sposób dostępu i tworzenia plików/danych XML
Name:		perl-XML-Smart
Version:	1.6.9
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	648309c0d613ddaca6f6b16e9f13c81d
URL:		http://search.cpan.org/dist/XML-Smart/
BuildRequires:	perl-Object-MultiType >= 0.03
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Ten moduł ma łatwy sposób na dostęp i tworzenie danych XML. Jest
oparty na drzewie haszy tworzonym z danych XML i umożliwia dynamiczny
dostęp do nich z użyciem perlowej składni dla haszy i tablic, bez
potrzeby pilnowania, czy w danym drzewie znajdują się hasze czy
tablice. Innymi słowy, każdy węzeł w drzewie funkcjonuje jako hasz i
tablica jednocześnie!

Moduł udostępnia także dodatki takie jak poszukiwanie węzłów według
atrybutów, wybór wartości atrybutu w każdym węźle wielokrotnym, zmiana
formatu zwracanych danych itp.

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

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/XML/Smart/*.{pod,epod}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Smart.pm
%{perl_vendorlib}/XML/Smart
%{_mandir}/man3/*
