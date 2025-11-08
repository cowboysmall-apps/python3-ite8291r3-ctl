%global commit d2c490a1485f4d0476649bc198e8bb9bf07b476e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global reponame ite8291r3-ctl
%global modname  ite8291r3_ctl

%global debug_package %{nil}



Name:           python3-%{reponame}
Version:        0.3
Release:        1%{?dist}
Summary:        Userspace driver for the ITE 8291 (rev 0.03) RGB keyboard backlight controller
License:        GPLv2
URL:            https://github.com/pobrn/%{reponame}
Source0:        %{URL}/archive/%{commit}/%{reponame}-%{shortcommit}.tar.gz
Source1:        99-ite8291r3-ctl.rules

BuildArch:      noarch

BuildRequires:  python3-devel
# BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-pyusb

Requires:       python3-pyusb
Requires:       python3-pillow
Requires:       python3-xlib

%?python_enable_dependency_generator



%description
%{summary}.



%prep
%autosetup -n %{reponame}-%{commit}


%build
%py3_build


%install
%{__install} -d %{buildroot}%{_sysconfdir}/udev/rules.d/
%{__install} %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/
%py3_install



%check
%{python3} -m unittest
# %{__python3} setup.py test
# %pytest
# %tox


%files -n python3-%{reponame}
%license LICENSE
%doc     README.md
%{_bindir}/%{reponame}
%{python3_sitelib}/%{modname}*
%{_sysconfdir}/udev/rules.d/99-ite8291r3-ctl.rules


%changelog
* Sat Sep 03 2022 Jerry Kiely <jerry@cowboysmall.com> - 0.3-1
- Added missing changelog entry - fixed version and release numbers

* Tue Aug 30 2022 Jerry Kiely <jerry@cowboysmall.com> - 0.0-2
- Fixed version and release numbers

* Tue Aug 30 2022 Jerry Kiely <jerry@cowboysmall.com> - 0.1-1
- First version of userspace driver - python3-ite8291r3-ctl

