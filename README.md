# Fedora Minimal Project
[![RPM Build](https://github.com/Element104/fedora-minimal/actions/workflows/rpm_build.yaml/badge.svg)](https://github.com/Element104/fedora-minimal/actions/workflows/rpm_build.yaml)
[![RPM Lint](https://github.com/Element104/fedora-minimal/actions/workflows/rpmlint.yml/badge.svg)](https://github.com/Element104/fedora-minimal/actions/workflows/rpmlint.yml)
[![RPM Install](https://github.com/Element104/fedora-minimal/actions/workflows/e2e.yml/badge.svg)](https://github.com/Element104/fedora-minimal/actions/workflows/e2e.yml)

`fedora-minimal-\*.rpm` packages conflict with various unnecessary stuff.
By installing `fedora-minimal-\*` package, you can achieve cleaner workstation installation.

Builds are at https://copr.fedoraproject.org/coprs/isimluk/fedora-minimal

## User Manual

### Enable repository

```
dnf copr enable -y isimluk/fedora-minimal
```

### Review available options

```
dnf search fedora-minimal-conflicts- 2> /dev/null | perl -ne 's/\.noarch\s*// and print'
```

### Install some parts of Fedora Minimal (removing some unneeded packages)
Based on the output above
```
dnf install fedora-minimal-conflicts-vmguest fedora-minimal-conflicts-cloud-iaas fedora-minimal-conflicts-client-tools fedora-minimal-conflicts-languages fedora-minimal-conflicts-old-hw-support fedora-minimal-conflicts-abrt fedora-minimal-conflicts-libreport fedora-minimal-conflicts-btrfs
```

### Install all of the fedora-minimal (hard-core option)
```
dnf install fedora-minimal
```
