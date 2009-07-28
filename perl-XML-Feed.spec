%define upstream_name    XML-Feed
%define upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      2

Summary:    Perl Module for Syndication feed parsing and auto-discovery 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::ErrorHandler)
BuildRequires: perl(Feed::Find)
BuildRequires: perl(URI::Fetch)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(List::Util)
BuildRequires: perl(LWP)
BuildRequires: perl(HTML::TokeParser)
BuildRequires: perl(XML::RSS) >= 1.01
BuildRequires: perl(XML::Atom) >= 0.08 
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
# (misc) not found by find-provides, as it can be changed at runtime with a 
# variable $PREFERED_PARSER
Requires:           perl(XML::RSS)

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
