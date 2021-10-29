#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lxml
Version  : 4.6.3
Release  : 77
URL      : https://files.pythonhosted.org/packages/e5/21/a2e4517e3d216f0051687eea3d3317557bde68736f038a3b105ac3809247/lxml-4.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e5/21/a2e4517e3d216f0051687eea3d3317557bde68736f038a3b105ac3809247/lxml-4.6.3.tar.gz
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
provides safe and convenient access to these libraries using the ElementTree
        API.
        
        It extends the ElementTree API significantly to offer support for XPath,
        RelaxNG, XML Schema, XSLT, C14N and much more.
        
        To contact the project, go to the `project home page

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
Provides: pypi(lxml)

%description python3
python3 components for the lxml package.


%prep
%setup -q -n lxml-4.6.3
cd %{_builddir}/lxml-4.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616510182
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxml
cp %{_builddir}/lxml-4.6.3/LICENSES.txt %{buildroot}/usr/share/package-licenses/lxml/495ceccaff92184d795e03cfc863c015dc3dced9
cp %{_builddir}/lxml-4.6.3/doc/licenses/GPL.txt %{buildroot}/usr/share/package-licenses/lxml/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/lxml-4.6.3/doc/licenses/ZopePublicLicense.txt %{buildroot}/usr/share/package-licenses/lxml/f5da410083f6879cf7e02e0676ee164642b33524
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
