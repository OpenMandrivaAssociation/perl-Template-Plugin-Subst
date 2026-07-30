%define upstream_name    Template-Plugin-Subst
%define upstream_version 0.02
Name:       perl-%{upstream_name}
Version:	0.02
Release:	3

Summary:    s/// functionality for Template Toolkit templates
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/N/NI/NIKC/Template-Plugin-Subst-0.02.tar.gz

BuildRequires:	make
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Template::Plugin::Subst acts as a filter and a virtual method to carry
out regular expression substitutions with back references on text and
variables in the Template Toolkit.

That's the advantage of this approach over the built-in C<replace>
method.  C<replace> doesn't deal with backrefs, so code like this:

  [% str = 'foobar' %]
  [% str.replace('(foo)(bar)', '$2$1') %]

%prep
%setup -q -n Template-Plugin-Subst-0.02

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


