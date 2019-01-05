#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lxml
Version  : 4.3.0
Release  : 49
URL      : https://files.pythonhosted.org/packages/16/4a/b085a04d6dad79aa5c00c65c9b2bbcb2c6c22e5ac341e7968e0ad2c57e2f/lxml-4.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/4a/b085a04d6dad79aa5c00c65c9b2bbcb2c6c22e5ac341e7968e0ad2c57e2f/lxml-4.3.0.tar.gz
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
%setup -q -n lxml-4.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546659829
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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
