%define upstream_name    XML-Feed
%define upstream_version 0.52

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		2

Summary:	Perl Module for Syndication feed parsing and auto-discovery 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/XML-Feed-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::ErrorHandler)
BuildRequires:	perl(Feed::Find)
BuildRequires:	perl(URI::Fetch)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Mail)
BuildRequires:	perl(DateTime::Format::W3CDTF)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(LWP)
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(XML::RSS) >= 1.01
BuildRequires:	perl(XML::Atom) >= 0.08 
BuildArch:	noarch
# (misc) not found by find-provides, as it can be changed at runtime with a 
# variable $PREFERED_PARSER
Requires:	perl(XML::RSS)

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
SKIP_SAX_INSTALL=1 CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/*/*

%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 2:0.430.0-2mdv2011.0
+ Revision: 664895
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2:0.430.0-1mdv2010.0
+ Revision: 401864
- rebuild using %%perl_convert_version

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.43-1mdv2010.0
+ Revision: 373772
- update to new version 0.43

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.42-1mdv2010.0
+ Revision: 370249
- update to new version 0.42

* Thu Mar 26 2009 Michael Scherer <misc@mandriva.org> 2:0.41-2mdv2009.1
+ Revision: 361417
- add a require to perl-XML-RSS, fix bug #49123

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.41-1mdv2009.1
+ Revision: 314281
- update to new version 0.41

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.40-1mdv2009.1
+ Revision: 309314
- update to new version 0.40

* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.3-1mdv2009.1
+ Revision: 303785
- new version

* Fri Nov 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.23-1mdv2009.1
+ Revision: 303169
- add epoch to fit upstream versioning schema

* Sat Oct 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.1
+ Revision: 297139
- update to new version 0.23

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.1
+ Revision: 296679
- update to new version 0.22

* Sun Oct 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.1
+ Revision: 295242
- update to new version 0.21

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.12-5mdv2009.0
+ Revision: 258841
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.12-4mdv2009.0
+ Revision: 246730
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.12-2mdv2008.1
+ Revision: 136365
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-2mdv2007.1
+ Revision: 133683
- cleanup

* Fri Mar 02 2007 Shlomi Fish  0.12-2mdv2007.0
- Changed the architecture to "noarch".

* Fri Mar 02 2007 Shlomi Fish  0.12-1mdv2007.0
- Initial release. Adapted the XML-Feed spec for this one.


