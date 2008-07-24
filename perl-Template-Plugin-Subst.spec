
%define realname   Template-Plugin-Subst
%define version    0.02
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    s/// functionality for Template Toolkit templates
Source:     http://www.cpan.org/modules/by-module/Template/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
Template::Plugin::Subst acts as a filter and a virtual method to carry
out regular expression substitutions with back references on text and
variables in the Template Toolkit.

That's the advantage of this approach over the built-in C<replace>
method.  C<replace> doesn't deal with backrefs, so code like this:

  [% str = 'foobar' %]
  [% str.replace('(foo)(bar)', '$2$1') %]



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



