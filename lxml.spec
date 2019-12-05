#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x44A7D230CCC5497B (consulting@behnel.de)
#
Name     : lxml
Version  : 4.4.2
Release  : 59
URL      : https://lxml.de/files/lxml-4.4.2.tgz
Source0  : https://lxml.de/files/lxml-4.4.2.tgz
Source1 : https://lxml.de/files/lxml-4.4.2.tgz.asc
Summary  : Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 ZPL-2.0
Requires: lxml-license = %{version}-%{release}
Requires: lxml-python = %{version}-%{release}
Requires: lxml-python3 = %{version}-%{release}
Requires: Cython
Requires: cssselect
Requires: html5lib
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : cssselect
BuildRequires : html5lib
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : zlib-dev

%description
What is lxml?
=============
lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
It's also very fast and memory friendly, just so you know.

%package license
Summary: license components for the lxml package.
Group: Default

%description license
license components for the lxml package.


%package python
Summary: python components for the lxml package.
Group: Default
Requires: lxml-python3 = %{version}-%{release}

%description python
python components for the lxml package.


%package python3
Summary: python3 components for the lxml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the lxml package.


%prep
%setup -q -n lxml-4.4.2
cd %{_builddir}/lxml-4.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574717798
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxml
cp %{_builddir}/lxml-4.4.2/LICENSES.txt %{buildroot}/usr/share/package-licenses/lxml/495ceccaff92184d795e03cfc863c015dc3dced9
cp %{_builddir}/lxml-4.4.2/doc/licenses/GPL.txt %{buildroot}/usr/share/package-licenses/lxml/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/lxml-4.4.2/doc/licenses/ZopePublicLicense.txt %{buildroot}/usr/share/package-licenses/lxml/f5da410083f6879cf7e02e0676ee164642b33524
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxml/495ceccaff92184d795e03cfc863c015dc3dced9
/usr/share/package-licenses/lxml/dfac199a7539a404407098a2541b9482279f690d
/usr/share/package-licenses/lxml/f5da410083f6879cf7e02e0676ee164642b33524

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
