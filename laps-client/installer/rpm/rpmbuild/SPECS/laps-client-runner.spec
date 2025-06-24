Name:           laps-client-runner
Version:        1.0.0
Release:        1%{?dist}
Summary:        laps-client - auto-rotate the root password for AD bound (samba net, pbis, adcli) linux servers
BuildArch:      noarch

License:        MIT
URL:            https://github.com/kraloveckey/mini-python
Source0:        %{name}-%{version}.tar.gz

Requires:       python3 python3-pip python3-gssapi python3-cryptography python3-dns python3-devel krb5-workstation krb5-devel gcc

%description
This RPM contains the script and personalized config to run the laps-client python script


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
cp usr/sbin/laps-runner $RPM_BUILD_ROOT/%{_sbindir}/laps-runner
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}
cp etc/laps-runner.json $RPM_BUILD_ROOT/%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/cron.hourly/
cp etc/cron.hourly/laps-runner $RPM_BUILD_ROOT/%{_sysconfdir}/cron.hourly/

%post
sudo -H pip3 install ldap3 dpapi-ng[kerberos]


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_sbindir}/laps-runner
%{_sysconfdir}/laps-runner.json
%{_sysconfdir}/cron.hourly/laps-runner


%changelog
* Sat Mar 23 2024 kraloveckey
- Initial build
