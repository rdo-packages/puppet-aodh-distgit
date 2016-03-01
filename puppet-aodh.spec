Name:			puppet-aodh
Epoch:			1
Version:		XXX
Release:		XXX
Summary:		Puppet module for OpenStack Aodh
License:		Apache-2.0

URL:			https://launchpad.net/puppet-aodh

Source0:		git://github.com/openstack/puppet-aodh.git

BuildArch:		noarch

Requires:		puppet-inifile
Requires:		puppet-stdlib
Requires:		puppet-openstacklib

%description
Puppet module for OpenStack Aodh

%prep
%setup -q -n %{name}-%{version}

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
cp -r %{buildroot}/%{_datadir}/openstack-puppet/modules/aodh/



%files
%{_datadir}/openstack-puppet/modules/aodh/


%changelog

