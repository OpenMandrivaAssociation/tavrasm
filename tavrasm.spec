%define name    tavrasm
%define version 1.22
%define release %mkrel 6

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
