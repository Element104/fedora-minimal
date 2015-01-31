Name:		fedora-minimal
Version:	0.1
Release:	1%{?dist}
Summary:	Keeping my work notebook clean

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/isimluk/fedora-minimal
BuildArch:	noarch

# rhbz#1187867
Conflicts:	NetworkManager-config-connectivity-fedora

%description
The set of fedora-minimal* packages help me to keep my work 
notebook clean. The package provides *-compat-s and conflicts
so I can enjoy my desktop without some unnecessary stuff

%prep

%build

%install

%files

%changelog

