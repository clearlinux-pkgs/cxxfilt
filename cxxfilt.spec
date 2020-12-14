#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cxxfilt
Version  : 0.2.2
Release  : 22
URL      : https://files.pythonhosted.org/packages/e0/aa/c1ae3629819cdcbb21b9a9fb5185df7a042592444c031198409523b4310a/cxxfilt-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e0/aa/c1ae3629819cdcbb21b9a9fb5185df7a042592444c031198409523b4310a/cxxfilt-0.2.2.tar.gz
Summary  : Python interface to c++filt / abi::__cxa_demangle
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: cxxfilt-license = %{version}-%{release}
Requires: cxxfilt-python = %{version}-%{release}
Requires: cxxfilt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
================

%package license
Summary: license components for the cxxfilt package.
Group: Default

%description license
license components for the cxxfilt package.


%package python
Summary: python components for the cxxfilt package.
Group: Default
Requires: cxxfilt-python3 = %{version}-%{release}

%description python
python components for the cxxfilt package.


%package python3
Summary: python3 components for the cxxfilt package.
Group: Default
Requires: python3-core
Provides: pypi(cxxfilt)

%description python3
python3 components for the cxxfilt package.


%prep
%setup -q -n cxxfilt-0.2.2
cd %{_builddir}/cxxfilt-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597077164
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cxxfilt
cp %{_builddir}/cxxfilt-0.2.2/LICENSE %{buildroot}/usr/share/package-licenses/cxxfilt/bea2c25a6aca85e33e4b56e95055f22e9e4b671e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cxxfilt/bea2c25a6aca85e33e4b56e95055f22e9e4b671e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
