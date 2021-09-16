%global debug_package %{nil}

Name: python-platformdirs
Epoch: 100
Version: 2.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python module for determining appropriate platform-specific dirs
License: MIT
URL: https://github.com/platformdirs/platformdirs/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-platformdirs
Summary: Python module for determining appropriate platform-specific dirs
Requires: python3
Provides: python3-platformdirs = %{epoch}:%{version}-%{release}
Provides: python3dist(platformdirs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-platformdirs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(platformdirs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-platformdirs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(platformdirs) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-platformdirs
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%files -n python%{python3_version_nodots}-platformdirs
%license LICENSE.txt
%{python3_sitelib}/platformdirs*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-platformdirs
Summary: Python module for determining appropriate platform-specific dirs
Requires: python3
Provides: python3-platformdirs = %{epoch}:%{version}-%{release}
Provides: python3dist(platformdirs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-platformdirs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(platformdirs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-platformdirs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(platformdirs) = %{epoch}:%{version}-%{release}

%description -n python3-platformdirs
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%files -n python3-platformdirs
%license LICENSE.txt
%{python3_sitelib}/platformdirs*
%endif

%changelog
