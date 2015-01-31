Name:		fedora-minimal
Version:	0.1
Release:	1%{?dist}
Summary:	Keeping my work notebook clean

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/isimluk/fedora-minimal
BuildArch:	noarch
Requires:	%{name}-conflicts-abrt
Requires:	%{name}-conflicts-anaconda
Requires:	%{name}-conflicts-openlmi
Requires:	%{name}-conflicts-setroubleshoot
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
Summary:	Keeps ABRT off
Conflicts:	abrt-libs
# brought in by abrt-addon-vmcore
Conflicts:	kexec-tools
%description	conflicts-abrt
Conflicts with ABRT set of packages.

%package	conflicts-anaconda
Summary:	Keeps the installer off
Conflicts:	anaconda-core anaconda-widgets
# brought in by anaconda
Conflicts:	tigervnc-server-minimal
Conflicts:	libtimezonemap
%description	conflicts-anaconda
Conflicts with Anaconda installer and its dependencies.

%package	conflicts-gnome
Summary:	Keeps some unneeded Gnome packages off
# brought in by anaconda
Conflicts:	libgnomekbd
Conflicts:	libxklavier
Conflicts:	keybinder3
Conflicts:	zenity
%description	conflicts-gnome
Conflicts with Gnome packages that are not really needed.

%package	conflicts-openlmi
Summary:	Keeps OpenLMI off
Conflicts:	cim-schema
Conflicts:	openlmi
# brought in by openlmi-storage
Conflicts:	sg3_utils
# Then the cim-server and its libs
Conflicts:	tog-pegasus-libs
# Then libs for cim over http
Conflicts:	pywbem
%description	conflicts-openlmi
Conflicts with OpenLMI set of packages

%package	conflicts-setroubleshoot
Summary:	Keeps setroubleshoot off
Conflicts:	setroubleshoot-server
%description	conflicts-setroubleshoot
Conflicts with setroubleshoot packages.

%prep

%build

%install

%files
%files		conflicts-misc
%files		conflicts-abrt
%files		conflicts-anaconda
%files		conflicts-gnome
%files		conflicts-openlmi
%files		conflicts-setroubleshoot

%changelog

