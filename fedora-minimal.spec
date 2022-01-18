Name:		fedora-minimal
Version:	0.35
Release:	2%{?dist}
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
Requires:	%{name}-conflicts-bluetooth
Requires:	%{name}-conflicts-cards
Requires:	%{name}-conflicts-clever-desktop
Requires:	%{name}-conflicts-client-tools
Requires:	%{name}-conflicts-cloud-iaas
Requires:	%{name}-conflicts-cluster
Requires:	%{name}-conflicts-cockpit
Requires:	%{name}-conflicts-docker
Requires:	%{name}-conflicts-efi
Requires:	%{name}-conflicts-fingerprint
Requires:	%{name}-conflicts-ipsec
Requires:	%{name}-conflicts-kdegames
Requires:	%{name}-conflicts-languages
Requires:	%{name}-conflicts-libreport
Requires:	%{name}-conflicts-managed-client
Requires:	%{name}-conflicts-openlmi
Requires:	%{name}-conflicts-opencl
Requires:	%{name}-conflicts-ostree
Requires:	%{name}-conflicts-packagekit
Requires:	%{name}-conflicts-python2
Requires:	%{name}-conflicts-setroubleshoot
Requires:	%{name}-conflicts-selinux-advanced-tools
Requires:	%{name}-conflicts-sssd
Requires:	%{name}-conflicts-vmguest
Requires:	%{name}-conflicts-vmhost
Requires:	%{name}-conflicts-network-services
Requires:	%{name}-conflicts-network-tools
Requires:	%{name}-conflicts-misc
Requires:	%{name}-disable-services
Requires:	%{name}-conflicts-old-hw-support
Obsoletes:	%{name}-conflicts-dnf <= 0:0.32
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
Conflicts:	NetworkManager-team
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
Conflicts:	authselect
Conflicts:	authselect-libs
Conflicts:	python-sssdconfig
%description	conflicts-auth
Conflicts with extra packages related to user authentization.

%package	conflicts-anaconda
Summary:	Keeps the installer off
Conflicts:	anaconda-core anaconda-widgets
# brought in by anaconda
Conflicts:	tigervnc-server-minimal
Conflicts:	libtimezonemap
Conflicts:	python3-blivet
Conflicts:	python-cryptsetup
Conflicts:	python-pyblock
Conflicts:	python3-pwquality
Conflicts:	augeas-libs
Conflicts:	pyparted
Conflicts:	device-mapper-multipath
Conflicts:	kpartx
Conflicts:	libhbaapi
Conflicts:	lldpad
Conflicts:	fcoe-utils
Conflicts:	anaconda-user-help
Conflicts:	anaconda-widgets
Conflicts:	libblockdev
Conflicts:	libblockdev-kbd bcache-tools
Conflicts:	libblockdev-swap
Conflicts:	libblockdev-mdraid
Conflicts:	libblockdev-dm dmraid dmraid-events sgpio
Conflicts:	libblockdev-lvm
Conflicts:	libblockdev-loop
Conflicts:	libblockdev-crypto volume_key-libs
Conflicts:	libblockdev-utils
Conflicts:	libudisks2
Conflicts:	libbytesize
Conflicts:	langtable
%description	conflicts-anaconda
Conflicts with Anaconda installer and its dependencies.

%package	conflicts-bluetooth
Summary:	Keeps bluetooth broken
Conflicts:	bluez-libs
Conflicts:	bluez
%description	conflicts-bluetooth
Conflicts with bluebooth.

%package	conflicts-btrfs
Summary:	Keeps extra packages related to btrfs off
Conflicts:	btrfs-progs
%description	conflicts-btrfs
Conflicts with extra packages related to btrfs.

%package	conflicts-cards
Summary:	Keeps various smart card and tokens support out
Conflicts:	pcsc-lite-libs
%description	conflicts-cards
Conflicts with various smart card and token support packages.

%package	conflicts-clever-desktop
Summary:	Keeps various desktop trackers, file system indexers, metadata search
Conflicts:	exempi
Conflicts:	libcue
Conflicts:	libgexiv2
Conflicts:	libgrss
Conflicts:	libiptcdata
Conflicts:	libtracker-miner
Conflicts:	imwheel
%description	conflicts-clever-desktop
Conflicts with various desktop trackers, file system indexers, metadata search...

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

%package	conflicts-cloud-iaas
Summary:	Keeps various cloud related tools out
Conflicts:	userspace-rcu librados2 lttng-ust
%description	conflicts-cloud-iaas
Conflicts with various clould related tools.

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

%package	conflicts-fingerprint
Summary:	keeps finger print reader tools out
Conflicts:	fprintd-pam
Conflicts:	fprintd
Conflicts:	libfprint
%description	conflicts-fingerprint
Conflicts with finger print reader tools.

%package	conflicts-ipsec
Summary:	keeps ipsec tools out
Conflicts:	trousers-lib
%description	conflicts-ipsec
Conflicts with ipsec tools.

%package	conflicts-gnome
Summary:	Keeps some unneeded Gnome packages off
Conflicts:	anaconda-user-help
# brought in by anaconda
Conflicts:	libgnomekbd
Conflicts:	glade-libs
#Conflicts:	libxklavier - neede by my favourite lightdm
#Conflicts:	keybinder3 - needed by terminator
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
Conflicts:	ibus-hangul
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

%package	conflicts-opencl
Summary:	Keeps OpenCL tools off
Conflicts:	beignet
Conflicts:	pocl
Conflicts:	mesa-libOpenCL
Conflicts:	libclc
Conflicts:	opencl-filesystem
%description	conflicts-opencl
Conflicts with OpenCL set of packages

%package	conflicts-ostree
Summary:	Keeps ostree tools off
Conflicts:	ostree-libs
%description	conflicts-ostree
Conflicts with ostree set of packages

%package	conflicts-packagekit
Summary:	Keeps PackageKit off
Conflicts:	PackageKit-glib
%description	conflicts-packagekit
Conflicts with PackageKit.

%package	conflicts-python2
Summary:	Conflicts with some python2 libraries
Conflicts:	python-coverage
Conflicts:	python27
Conflicts:	python2-rpm-macros
%description	conflicts-python2
Conflicts with some python2 libraries that I no longer find useful.

%package	conflicts-setroubleshoot
Summary:	Keeps setroubleshoot off
Conflicts:	setroubleshoot-server
%description	conflicts-setroubleshoot
Conflicts with setroubleshoot packages.

%package	conflicts-selinux-advanced-tools
Summary:	Keeps advanced selinux tools offf
Conflicts:	checkpolicy
Conflicts:	policycoreutils-python-utils
Conflicts:	policycoreutils-python3
Conflicts:	libsemanage-python3
Conflicts:	setools-python3
%description	conflicts-selinux-advanced-tools
Note: This may damper your ability to install various -selinux
subpackages. See dnf search selinux | grep -- -selinux

%package	conflicts-sssd
Summary:	Keeps sssd off
Conflicts:	sssd
Conflicts:	sssd-ipa sssd-krb5 sssd-krb5-common sssd-ldap
Conflicts:	adcli
Conflicts:	lubipa_hbac
Conflicts:	python3-sssdconfig
Conflicts:	sssd-client
Conflicts:	sssd-common
Conflicts:	sssd-common-pac
Conflicts:	sssd-kcm
Conflicts:	sssd-proxy
Conflicts:	sssd-nfs-idmap
Conflicts:	libsss_certmap
Conflicts:	libsss_idmap
Conflicts:	libsss_nss_idmap
Conflicts:	libsss_sudo libsss_autofs
Conflicts:	libipa_hbac
Conflicts:	c-ares
Conflicts:	libdhash
%description	conflicts-sssd
Conflicts with setroubleshoot packages.

%package	conflicts-vmguest
Summary:	Keeps vm guest tools off
Conflicts:	spice-vdagent
Conflicts:	qemu-guest-agent
Conflicts:	open-vm-tools
Conflicts:	xorg-x11-drv-vmware
Conflicts:	virtualbox-guest-additions
Conflicts:	hyperv-daemons
Conflicts:	hyperv-daemons-license
%description	conflicts-vmguest
Conflicts with packages related to VM guests.

%package	conflicts-vmhost
Summary:	Keeps vm host tools off
Conflicts:	cyrus-sasl-gssapi
Conflicts:	libnfsidmap
Conflicts:	libosinfo
Conflicts:	osinfo-db-tools
%description	conflicts-vmhost
Conflicts with packages related to VM host.

%package	conflicts-network-services
Summary:	Keeps network services off my notebook
Conflicts:	gssproxy
Conflicts:	nfs-utils rpcbind
Conflicts:	libverto-libev
Conflicts:	samba-libs samba-client-libs samba-common
Conflicts:	cifs-utils libwbclient
Conflicts:	keyutils
%description	conflicts-network-services
Conflicts with packages related to network services.

%package	conflicts-network-tools
Summary:	Keeps network tools off my notebook
Conflicts:	bridge-utils
Conflicts:	dnsmasq
%description	conflicts-network-tools
Conflicts with packages related to network services.

%package	conflicts-old-hw-support
Summary:	Conflicts with support of dated hardware
Conflicts:	iwl100-firmware iwl105-firmware iwl135-firmware
Conflicts:	iwl1000-firmware
Conflicts:	iwl2000-firmware iwl2030-firmware
Conflicts:	iwl3160-firmware iwl3945-firmware
Conflicts:	iwl4965-firmware
Conflicts:	iwl5000-firmware iwl5150-firmware
Conflicts:	iwl6000-firmware iwl6000g2a-firmware iwl6000g2b-firmware iwl6050-firmware
%description	conflicts-old-hw-support
Conflicts with various dated firmware packages.

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
Conflicts:	rsyslog
Conflicts:	libestr libfastjson liblogging-stdlog
Conflicts:	opensc
%description	conflicts-extra
Conflicts with the packages that I yet have to find useful.
These were installed by various repogroups or anaconda.

%package	disable-services
Summary:	Please
%description	disable-services
Disables various services that are really not needed on minimal laptop.

%prep

%build

%install
# disable systemd-coredump in var, this cleans /proc/sys/kernel/core_pattern
mkdir -p $RPM_BUILD_ROOT/etc/sysctl.d/
echo "kernel.core_pattern=" > $RPM_BUILD_ROOT/etc/sysctl.d/50-coredump.conf
# disable systemd-coredump whatsoever
mkdir -p $RPM_BUILD_ROOT/etc/systemd/coredump.conf.d/
cat > $RPM_BUILD_ROOT/etc/systemd/coredump.conf.d/disable.conf <<__END__
[Coredump]
Storage=none
__END__
# disable bluetooth (A)
mkdir -p ${RPM_BUILD_ROOT}/etc/bluetooth
cat > ${RPM_BUILD_ROOT}/etc/bluetooth/main.conf <<__END__
AutoEnable=false
__END__
# disable bluetooth (B)
mkdir -p ${RPM_BUILD_ROOT}/etc/modprobe.d/
cat > ${RPM_BUILD_ROOT}/etc/modprobe.d/blacklist-btusb.conf <<__END__
blacklist btusb
__END__

%post compat-systemd
/lib/systemd/systemd-sysctl
systemctl daemon-reload

%postun compat-systemd
/lib/systemd/systemd-sysctl
systemctl daemon-reload

%post disable-services
chkconfig sshd off  # screw you systemd, I learned chkconfig when I was young
systemctl disable dnf-makecache.timer  # ok systemd you win

%post conflicts-bluetooth
# disable bluetooth (B)
modprobe -r btusb

%files
%files		compat-systemd
/etc/sysctl.d/50-coredump.conf
/etc/systemd/coredump.conf.d/disable.conf
%files		conflicts-auth
%files		conflicts-abrt
%files		conflicts-anaconda
%files		conflicts-bluetooth
/etc/modprobe.d/blacklist-btusb.conf
/etc/bluetooth/main.conf
%files		conflicts-btrfs
%files		conflicts-cards
%files		conflicts-clever-desktop
%files		conflicts-client-tools
%files		conflicts-cloud-iaas
%files		conflicts-cluster
%files		conflicts-cockpit
%files		conflicts-docker
%files		conflicts-efi
%files		conflicts-fingerprint
%files		conflicts-ipsec
%files		conflicts-gnome
%files		conflicts-kdegames
%files		conflicts-languages
%files		conflicts-libreport
%files		conflicts-managed-client
%files		conflicts-openlmi
%files		conflicts-opencl
%files		conflicts-ostree
%files		conflicts-packagekit
%files		conflicts-python2
%files		conflicts-selinux-advanced-tools
%files		conflicts-setroubleshoot
%files		conflicts-sssd
%files		conflicts-vmguest
%files		conflicts-vmhost
%files		conflicts-network-services
%files		conflicts-network-tools
%files		conflicts-misc
%files		conflicts-extra
%files		conflicts-old-hw-support
%files		disable-services

%changelog
* Sun Dec 19 2021 Šimon Lukašík <slukasik@redhat.com> - 0.35-2
- rebuilt

* Sun Dec 19 2021 Šimon Lukašík <slukasik@redhat.com> - 0.32-7
- rebuilt for f35

* Tue Jun 16 2020 Šimon Lukašík <slukasik@redhat.com> - 0.32-6
- rebuilt

* Sun May 24 2020 Šimon Lukašík <slukasik@redhat.com> - 0.32-5
- rebuilt

* Fri May 22 2020 Šimon Lukašík <slukasik@redhat.com> - 0.32-4
- rebuilt

* Tue May 19 2020 Šimon Lukašík <slukasik@redhat.com> - 0.32-3
- rebuilt

* Tue May 19 2020 Šimon Lukašík <slukasik@redhat.com> - 0.32-2
- rebuilt

* Mon May 11 2020 Šimon Lukašík <slukasik@redhat.com> - 0.32-1
- rebuilt for f32

* Sun Dec 30 2018 Šimon Lukašík <slukasik@redhat.com> - 0.29-1
- rebuilt for f29

* Sat Sep 22 2018 Šimon Lukašík <slukasik@redhat.com> - 0.6-3
- get a rid of authselect

* Fri Jul 13 2018 Šimon Lukašík <slukasik@redhat.com> - 0.6-2
- get a rid of virtualbox-guest-additions

* Mon Jul 02 2018 Šimon Lukašík <slukasik@redhat.com> - 0.6-1
- support f28

* Mon Mar 05 2018 Šimon Lukašík <slukasik@redhat.com> - 0.5-11
- rebuilt

* Thu Jan 25 2018 Šimon Lukašík <slukasik@redhat.com> - 0.5-10
- remove timedatex used only by anaconda
- grace with ntfs, kids have external disks with ntfs nowdays

* Tue Jan 16 2018 Šimon Lukašík <slukasik@redhat.com> - 0.5-9
- introduce -conflicts-opencl

* Wed Jan 10 2018 Šimon Lukašík <slukasik@redhat.com> - 0.5-8
- rebuilt

* Thu Dec 21 2017 Šimon Lukašík <slukasik@redhat.com> - 0.5-7
- rebuilt

* Wed Dec 20 2017 Šimon Lukašík <slukasik@redhat.com> - 0.5-7
- rebuilt

* Tue Dec 19 2017 Šimon Lukašík <slukasik@redhat.com> - 0.5-5
- rebuilt

* Mon Dec 18 2017 Šimon Lukašík <slukasik@redhat.com> - 0.5-4
- rebuilt

* Thu Nov 30 2017 Šimon Lukašík <slukasik@redhat.com> - 0.5-3
- rebuilt -- fix coredumpctl (disable)

* Sat Nov 25 2017 Šimon Lukašík <slukasik@redhat.com> - 0.5-2
- rebuilt

* Wed Nov 22 2017 Šimon Lukašík <slukasik@redhat.com> - 0.5-1
- amended for my today needs on F27

* Mon Oct 05 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4-1
- new upstream release

* Fri Sep 11 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3-1
- new upstream release

* Sat Feb 07 2015 slukasik - 0.2-1
- new upstream release

