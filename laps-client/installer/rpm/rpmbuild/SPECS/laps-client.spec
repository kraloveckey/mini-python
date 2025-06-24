Name:           laps-client
Version:        1.0.0
Release:        1%{?dist}
Summary:        laps-client - auto-rotate the root password for AD bound (samba net, pbis, adcli) linux servers
BuildArch:      noarch

License:        MIT
URL:            https://github.com/kraloveckey/mini-python/laps-client
Source0:        %{name}-%{version}.tar.gz

Requires:       python3 python3-pip python3-gssapi python3-qt5 python3-dns python3-devel krb5-devel gcc

%description
This RPM contains the script and personalized config to run the lap4linux python script


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp usr/bin/laps-gui $RPM_BUILD_ROOT/%{_bindir}/laps-gui
cp usr/bin/laps-cli $RPM_BUILD_ROOT/%{_bindir}/laps-cli
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cp usr/share/applications/LAPS4LINUX.desktop $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
cp usr/share/pixmaps/laps.png $RPM_BUILD_ROOT/usr/share/pixmaps


%post
sudo -H pip3 install ldap3 dpapi-ng[kerberos]
if command -v update-desktop-database; then
	update-desktop-database
fi


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/laps-gui
%{_bindir}/laps-cli
/usr/share/applications/laps-client.desktop
/usr/share/pixmaps/laps.png


%changelog
* Sat Mar 23 2024 kraloveckey
- Initial build
