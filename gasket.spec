%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     gasket
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  The Coral Gasket Driver allows usage of the Coral EdgeTPU on Linux systems
License:  GPLv2
URL:      https://github.com/KyleGospo/gasket-dkms/

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
The Coral Gasket Driver allows usage of the Coral EdgeTPU on Linux systems. The driver contains two modules: Gasket: Gasket (Google ASIC Software, Kernel Extensions, and Tools) is a top level driver for lightweight communication with Google ASICs; and Apex: The EdgeTPU v1.

%prep
%setup -q -c gasket-dkms-main

%build
install -D -m 0644 gasket-dkms-main/%{name}.conf %{buildroot}%{_modulesloaddir}/%{name}.conf
install -D -m 0644 gasket-dkms-main/65-apex.rules %{buildroot}%{_udevrulesdir}/65-apex.rules

%files
%doc gasket-dkms-main/README.md
%license gasket-dkms-main/LICENSE
%{_modulesloaddir}/%{name}.conf
%{_udevrulesdir}/65-apex.rules

%changelog
{{{ git_dir_changelog }}}
