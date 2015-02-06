%define name    tavrasm
%define version 1.22
%define release 8

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:       	A AVR assembler
Source0:        %{name}-%{version}.tar.bz2
License:        GPL
Group:          Development/Other
Url:         	http://www.tavrasm.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  flex, bison

%description
Toms Linux AVR Assembler :

- Compiles code written for Atmels AVR DOS assembler.
- Super-set of Atmel AVR assembler.
- Generates Intel Hex, Motorola S-record, Generic and binary output.
- Atmel object files compatible with Atmel's AVR Studio.
- More than 100 warning/error messages.
- 'C' like escape characters in char/string literals ('\n', '\t', ...).
- Macros in macros.

%prep
%setup -q -n tavrasm.122/

%build
cd src

# parallel build fail
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

cp src/%name $RPM_BUILD_ROOT%{_bindir}
cp %name.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%{_bindir}/%{name}
%{_mandir}/man1/*


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.22-7mdv2010.0
+ Revision: 434308
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.22-6mdv2009.0
+ Revision: 261428
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.22-5mdv2009.0
+ Revision: 254186
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.22-3mdv2008.1
+ Revision: 140918
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Couriousous <couriousous@mandriva.org> 1.22-3mdv2008.0
+ Revision: 54837
- rebuild
- Import tavrasm



* Fri Apr 21 2006 Couriousous <couriousous@mandriva.org> 1.22-2mdk
- Yearly rebuild

* Sun Mar 13 2005 Couriousous <couriousous@mandrake.org> 1.22-1mdk
- First Mandrakelinux release
