%define	rname	activeresource

Summary:	Think Active Record for web resources
Name:		ruby-%{rname}
Version:	3.2.3
Release:	2
URL:		http://www.rubyonrails.org/
Source0:	http://rubygems.org/downloads/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 

%description
Rails way to utilize model objects as REST-based client proxies to remote
services.

%prep

%build

%install
rm -rf %{buildroot}
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec


%changelog
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.2.3-1
+ Revision: 795963
- update to 3.2.3

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.1-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 3.2.1-1
+ Revision: 769664
- New release

* Tue Mar 15 2011 Rémy Clouard <shikamaru@mandriva.org> 2.3.11-1
+ Revision: 645163
- new version 2.3.11

* Thu Dec 09 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-2mdv2011.0
+ Revision: 618309
- add provides to fix rails dependencies

* Fri Oct 15 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-1mdv2011.0
+ Revision: 585835
- bump release

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.9-1mdv2011.0
+ Revision: 579502
- new release: 2.3.9

* Sun Sep 13 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.4-1mdv2010.0
+ Revision: 438621
- Update to new version 2.3.4

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.3-1mdv2010.0
+ Revision: 404440
- Update to new version 2.3.3

* Fri Jun 12 2009 Lev Givon <lev@mandriva.org> 2.1.2-1mdv2010.0
+ Revision: 385326
- Update to 2.1.2.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-2mdv2009.0
+ Revision: 269229
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.1.0-1mdv2009.0
+ Revision: 214637
- new release 2.1.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Mon Jan 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 151599
- import ruby-activeresource


