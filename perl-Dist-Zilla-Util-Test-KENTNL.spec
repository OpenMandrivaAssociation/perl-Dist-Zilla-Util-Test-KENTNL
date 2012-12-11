%define upstream_name    Dist-Zilla-Util-Test-KENTNL
%define upstream_version 0.01000510

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	KENTNL's DZil plugin testing tool
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Dist::Zilla::Tester)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(Throwable)
BuildRequires:	perl(Role::Identifiable::HasIdent)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Role::HasMessage)
BuildRequires:	perl(MooseX::OneArgNew)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
KENTNL's DZil plugin testing tool.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

