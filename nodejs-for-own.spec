%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name for-own

Summary:       return an object with properties that evaluate to true from the callback
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.1.3
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/for-own
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Iterate over the own enumerable properties of an object, and return 
an object with properties that evaluate to true from the callback. 
Exit early by returning false.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.3-3
- rebuilt

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-2
- Enable scl macros, fix license macro for el6

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 0.1.3-1
- Initial package