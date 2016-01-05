Name:		fedora-minimal
Version:	0.4
Release:	1%{?dist}
Summary:	Keeping my work notebook clean

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/isimluk/fedora-minimal
BuildArch:	noarch
Requires:	%{name}-compat-systemd
Requires:	%{name}-conflicts-abrt
Requires:	%{name}-conflicts-auth
Requires:	%{name}-conflicts-anaconda
Requires:	%{name}-conflicts-btrfs
Requires:	%{name}-conflicts-client-tools
Requires:	%{name}-conflicts-cluster
Requires:	%{name}-conflicts-cockpit
Requires:	%{name}-conflicts-docker
Requires:	%{name}-conflicts-efi
Requires:	%{name}-conflicts-kdegames
Requires:	%{name}-conflicts-languages
Requires:	%{name}-conflicts-libreport
Requires:	%{name}-conflicts-managed-client
Requires:	%{name}-conflicts-openlmi
Requires:	%{name}-conflicts-packagekit
Requires:	%{name}-conflicts-python2
Requires:	%{name}-conflicts-setroubleshoot
Requires:	%{name}-conflicts-vmguest
Requires:	%{name}-conflicts-misc
Obsoletes:	%{name}-conflicts-dnf
#TODO genisoimage

%description
The set of fedora-minimal* packages help me to keep my work
notebook clean. The package provides *-compat-s and conflicts
so I can enjoy my desktop without some unnecessary stuff

%package	compat-systemd
Summary:	systemd tweaks
%description	compat-systemd
Disables systemd-coredump.

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

%package	conflicts-auth
Summary:	Keeps extra packages related to authentization off
Conflicts:	realmd
Conflicts:	authconfig
Conflicts:	python-sssdconfig
%description	conflicts-auth
Conflicts with extra packages related to user authentization.

%package	conflicts-anaconda
Summary:	Keeps the installer off
Conflicts:	anaconda-core anaconda-widgets
# brought in by anaconda
Conflicts:	tigervnc-server-minimal
Conflicts:	libtimezonemap
Conflicts:	python-blivet
Conflicts:	python-cryptsetup
Conflicts:	python-pyblock
Conflicts:	python-pwquality
Conflicts:	pyparted
Conflicts:	device-mapper-multipath
Conflicts:	libhbaapi
Conflicts:	lldpad
Conflicts:	fcoe-utils
Conflicts:	anaconda-user-help
%description	conflicts-anaconda
Conflicts with Anaconda installer and its dependencies.

%package	conflicts-btrfs
Summary:	Keeps extra packages related to btrfs off
Conflicts:	btrfs-progs
%description	conflicts-btrfs
Conflicts with extra packages related to btrfs.

%package	conflicts-client-tools
Summary:	Keeps various client tools out
Conflicts:	freeipa-python
Conflicts:	freeipa-client
%description	conflicts-client-tools
Conflicts with various client packages.

%package	conflicts-cluster
Summary:	Keeps various cluster related tools out
Conflicts:	device-mapper-multipath-libs
%description	conflicts-cluster
Conflicts with various cluster related tools.

%package	conflicts-cockpit
Summary:	Keeps cockpit off
Conflicts:	cockpit
Conflicts:	storaged
%description	conflicts-cockpit
Conflicts with cockpit packages. Cockpit is another useful tool
that I don't really need.

%package	conflicts-docker
summary:	keeps docker off
# this one pretty much does it
conflicts:	docker-io
%description	conflicts-docker
Conflicts with Docker and libcontainer.

%package	conflicts-efi
summary:	keeps efi tools off
Conflicts:	efivar-libs
%description	conflicts-efi
Conflicts with efi tools.

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

%package	conflicts-managed-client
Summary:	Keeps various client packages off
Conflicts:	python-pbr
Conflicts:	python-keystoneclient
Conflicts:	python-novaclient
%description	conflicts-managed-client
Conflicts with client packages related to some management stacks.

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

%package	conflicts-python2
Summary:	Conflicts with some python2 libraries
Conflicts:	python-coverage
%description	conflicts-python2
Conflicts with some python2 libraries that I no longer find useful.

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
Conflicts:	systemd-python
Conflicts:	systemd-python3
Conflicts:	tigervnc-license
Conflicts:	samba-common-libs
%description	conflicts-extra
Conflicts with the packages that I yet have to find useful.
These were installed by various repogroups or anaconda.

%prep

%build

%install
# disable systemd-coredump, this cleans /proc/sys/kernel/core_pattern
mkdir -p $RPM_BUILD_ROOT/etc/sysctl.d/
echo "kernel.core_pattern=" > $RPM_BUILD_ROOT/etc/sysctl.d/50-coredump.conf

%post compat-systemd
/lib/systemd/systemd-sysctl

%postun compat-systemd
/lib/systemd/systemd-sysctl

%files
%files		compat-systemd
/etc/sysctl.d/50-coredump.conf
%files		conflicts-auth
%files		conflicts-abrt
%files		conflicts-anaconda
%files		conflicts-btrfs
%files		conflicts-client-tools
%files		conflicts-cluster
%files		conflicts-cockpit
%files		conflicts-docker
%files		conflicts-efi
%files		conflicts-gnome
%files		conflicts-kdegames
%files		conflicts-languages
%files		conflicts-libreport
%files		conflicts-managed-client
%files		conflicts-openlmi
%files		conflicts-packagekit
%files		conflicts-python2
%files		conflicts-setroubleshoot
%files		conflicts-vmguest
%files		conflicts-misc
%files		conflicts-extra

%changelog
* Mon Oct 05 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4-1
- new upstream release

* Fri Sep 11 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3-1
- new upstream release

* Sat Feb 07 2015 slukasik - 0.2-1
- new upstream release

