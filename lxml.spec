#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x44A7D230CCC5497B (consulting@behnel.de)
#
Name     : lxml
Version  : 4.3.3
Release  : 53
URL      : https://lxml.de/files/lxml-4.3.3.tgz
Source0  : https://lxml.de/files/lxml-4.3.3.tgz
Source99 : https://lxml.de/files/lxml-4.3.3.tgz.asc
Summary  : Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: lxml-license = %{version}-%{release}
Requires: lxml-python = %{version}-%{release}
Requires: lxml-python3 = %{version}-%{release}
Requires: Cython
Requires: cssselect
Requires: html5lib
BuildRequires : buildreq-distutils3
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

%description python3
python3 components for the lxml package.


%prep
%setup -q -n lxml-4.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553634163
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxml
cp LICENSES.txt %{buildroot}/usr/share/package-licenses/lxml/LICENSES.txt
cp doc/licenses/GPL.txt %{buildroot}/usr/share/package-licenses/lxml/doc_licenses_GPL.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxml/LICENSES.txt
/usr/share/package-licenses/lxml/doc_licenses_GPL.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
