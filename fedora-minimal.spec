Name:		fedora-minimal
Version:	0.1
Release:	1%{?dist}
Summary:	Keeping my work notebook clean

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/isimluk/fedora-minimal
BuildArch:	noarch
Requires:	%{name}-conflicts-abrt
Requires:	%{name}-conflicts-openlmi
Requires:	%{name}-conflicts-misc

%description
The set of fedora-minimal* packages help me to keep my work
notebook clean. The package provides *-compat-s and conflicts
so I can enjoy my desktop without some unnecessary stuff

%package	conflicts-misc
Summary:	Miscellaneous conflicts
# rhbz#1187867
Conflicts:	NetworkManager-config-connectivity-fedora
%description	conflicts-misc
Conflicts with miscellaneous packages.

%package	conflicts-abrt
Summary:	Keeps ABRT out off
Conflicts:	abrt-libs
# brought in by abrt-addon-vmcore
Conflicts:	kexec-tools
%description	conflicts-abrt
Conflicts with ABRT set of packages.

%package	conflicts-openlmi
Summary:	Keeps OpenLMI off
Conflicts:	openlmi
# brought in by openlmi-storage
Conflicts:	sg3_utils
# Then the cim-server and its libs
Conflicts:	tog-pegasus-libs

%description	conflicts-openlmi
Conflicts with OpenLMI set of packages

%prep

%build

%install

%files
%files		conflicts-misc
%files		conflicts-abrt
%files		conflicts-openlmi

%changelog

