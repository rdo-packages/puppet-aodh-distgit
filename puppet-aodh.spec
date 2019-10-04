%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-aodh
Version:        15.4.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Aodh
License:        ASL 2.0

URL:            https://launchpad.net/puppet-aodh

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Aodh

%prep
%setup -q -n openstack-aodh-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/aodh/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/aodh/



%files
%{_datadir}/openstack-puppet/modules/aodh/


%changelog
* Fri Oct 04 2019 RDO <dev@lists.rdoproject.org> 15.4.0-1
- Update to 15.4.0


