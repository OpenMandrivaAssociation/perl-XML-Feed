%define module  XML-Feed
%define name    perl-%{module}
%define release %mkrel 5
%define version 0.12

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Perl Module for Syndication feed parsing and auto-discovery 
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:      perl(Class::ErrorHandler)
BuildRequires:      perl(Feed::Find)
BuildRequires:      perl(URI::Fetch)
BuildRequires:      perl(DateTime)
BuildRequires:      perl(DateTime::Format::Mail)
BuildRequires:      perl(DateTime::Format::W3CDTF)
BuildRequires:      perl(List::Util)
BuildRequires:      perl(LWP)
BuildRequires:      perl(HTML::TokeParser)
BuildRequires:      perl(XML::RSS) >= 1.01
BuildRequires:      perl(XML::Atom) >= 0.08 
BuildRoot:          %{_tmppath}/%{name}-%{version}
BuildArch:          noarch

%description
XML::Feed is a syndication feed parser for both RSS and Atom feeds. It also
implements feed auto-discovery for finding feeds, given a URI.

XML::Feed supports the following syndication feed formats:

* RSS 0.91
* RSS 1.0
* RSS 2.0
* Atom

The goal of XML::Feed is to provide a unified API for parsing and using the
various syndication formats.

%prep
%setup -q -n %{module}-%{version}

%build
SKIP_SAX_INSTALL=1 CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/*/*


