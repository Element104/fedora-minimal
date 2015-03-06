Name:		fedora-minimal
Version:	0.2
Release:	1%{?dist}
Summary:	Keeping my work notebook clean

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/isimluk/fedora-minimal
BuildArch:	noarch
Requires:	%{name}-conflicts-abrt
Requires:	%{name}-conflicts-anaconda
Requires:	%{name}-conflicts-cockpit
Requires:	%{name}-conflicts-client-tools
Requires:	%{name}-conflicts-dnf
Requires:	%{name}-conflicts-docker
Requires:	%{name}-conflicts-kdegames
Requires:	%{name}-conflicts-languages
Requires:	%{name}-conflicts-libreport
Requires:	%{name}-conflicts-openlmi
Requires:	%{name}-conflicts-packagekit
Requires:	%{name}-conflicts-setroubleshoot
Requires:	%{name}-conflicts-vmguest
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
Conflicts:	python-blivet
Conflicts:	python-cryptsetup
Conflicts:	python-pyblock
Conflicts:	pyparted
Conflicts:	device-mapper-multipath
Conflicts:	libhbaapi
Conflicts:	lldpad
Conflicts:	fcoe-utils
Conflicts:	pykickstart
%description	conflicts-anaconda
Conflicts with Anaconda installer and its dependencies.

%package	conflicts-client-tools
Summary:	Keeps various client tools out
Conflicts:	freeipa-python
Conflicts:	freeipa-client
%description	conflicts-client-tools
Conflicts with various client packages.

%package	conflicts-cockpit
Summary:	Keeps cockpit off
Conflicts:	cockpit
Conflicts:	storaged
%description	conflicts-cockpit
Conflicts with cockpit packages. Cockpit is another useful tool
that I don't really need.

%package	conflicts-dnf
Summary:	Keeps DNF off
# this one pretty much does it
Conflicts:	dnf
Conflicts:	hawkey
Conflicts:	libsolv
Conflicts:	python-libcomps, python3-libcomps
Conflicts:	python-librepo, python3-librepo
%description	conflicts-dnf
Conflicts with DNF and rpm-ostree. Don't take me wrong, I think
dnf is the future, I just happen to use yum at this point.

%package	conflicts-docker
summary:	keeps docker off
# this one pretty much does it
conflicts:	docker-io
%description	conflicts-docker
Conflicts with Docker and libcontainer.

%package	conflicts-gnome
Summary:	Keeps some unneeded Gnome packages off
# brought in by anaconda
Conflicts:	libgnomekbd
Conflicts:	libxklavier
Conflicts:	keybinder3
Conflicts:	zenity
Conflicts:	accountsservice-libs
%description	conflicts-gnome
Conflicts with Gnome packages that are not really needed.

%package	conflicts-kdegames
Summary:	Keeps kdegames off
Conflicts:	openalt-soft
%description	conflicts-kdegames
Conflicts with kdegames and their dependencies.

%package	conflicts-languages
Summary:	Keeps non english language support off
Conflicts:	system-config-language
Conflicts:	libkkc, libkkc-common
%description	conflicts-languages
Conflicts with various packages related to internatialization.

%package	conflicts-libreport
Summary:	Keeps libreport off
Conflicts:	libreport
Conflicts:	python-augeas
Conflicts:	fros
Conflicts:	satyr
%description	conflicts-libreport
Conflicts with libreport and its dependencies.

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

%package	conflicts-packagekit
Summary:	Keeps PackageKit off
Conflicts:	PackageKit-glib
%description	conflicts-packagekit
Conflicts with PackageKit.

%package	conflicts-setroubleshoot
Summary:	Keeps setroubleshoot off
Conflicts:	setroubleshoot-server
%description	conflicts-setroubleshoot
Conflicts with setroubleshoot packages.

%package	conflicts-vmguest
Summary:	Keeps vm guest tools off
Conflicts:	spice-vdagent
Conflicts:	qemu-guest-agent
Conflicts:	open-vm-tools
Conflicts:	xorg-x11-drv-vmware
%description	conflicts-vmguest
Conflicts with packages related to VM guests.

%package	conflicts-extra
Summary:	Extra conflicts that you may found useful
Conflicts:	jack-audio-connection-kit-example-clients
Conflicts:	nano
Conflicts:	sos
Conflicts:	setuptool
Conflicts:	gnome-disk-utility
Conflicts:	lftp
Conflicts:	rmt
Conflicts:	rcs
Conflicts:	ssmtp
Conflicts:	stunnel
%description	conflicts-extra
Conflicts with the packages that I yet have to find useful.
These were installed by various repogroups or anaconda.

%prep

%build

%install

%files
%files		conflicts-abrt
%files		conflicts-anaconda
%files		conflicts-client-tools
%files		conflicts-cockpit
%files		conflicts-dnf
%files		conflicts-docker
%files		conflicts-gnome
%files		conflicts-kdegames
%files		conflicts-languages
%files		conflicts-libreport
%files		conflicts-openlmi
%files		conflicts-packagekit
%files		conflicts-setroubleshoot
%files		conflicts-vmguest
%files		conflicts-misc
%files		conflicts-extra

%changelog
* Sat Feb 07 2015 slukasik - 0.2-1
- new upstream release

