%global srcname procszoo
%global debug_package %{nil}
%global version %(tr -d '\n' < VERSION)
%global release 1
%global sum Python module to operate Linux namespaces
%global desc Procszoo aims to provide you a simple but complete tool and you can use it \
as a DSL or an embeded programming language which let you operate Linux namespaces by Python. \
Procszoo gives a smart init program. I get it from baseimage-docker. \
Thanks a lot, you guys. \
Procszoo does not require new version Python (but we support python3, too) and Linux kernel.

Summary: %{sum}
Name: python-%{srcname}
Version: %{version}
Release: %{release}%{?dist}
Source: %{srcname}-%{version}.tar.gz
License: GPL2+
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{srcname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: xning <anzhou94@gmail.com>
Packager: Rayson Zhu <vfreex+procszoo@gmail.com>
Url: https://github.com/xning/procszoo
BuildRequires: autoconf make gcc
BuildRequires: python-devel python-setuptools python-rpm-macros python-srpm-macros python2-rpm-macros

%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%endif

# Macros from https://fedoraproject.org/wiki/Packaging:Python_Old
%{!?py_setup: %global py_setup setup.py}
%{!?py_shbang_opts: %global py_shbang_opts -s}
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

# Macros from python2-rpm-macros on Fedora 24: /usr/lib/rpm/macros.d/macros.python2
%{!?py2_build: %global py2_build %{expand:\
CFLAGS="%{optflags}" %{__python2} %{py_setup} %{?py_setup_args} build --executable="%{__python2} %{py2_shbang_opts}" %{?1}\
}}
%{!?py2_install: %global py2_install %{expand:\
CFLAGS="%{optflags}" %{__python2} %{py_setup} %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?1}\
}}

%if 0%{?with_python3}
BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}-setuptools python3-rpm-macros
%endif

%description
Procszoo aims to provide you a simple but complete tool and you can use it as a DSL or an embeded programming language which let you operate Linux namespaces by Python. Procszoo gives a smart init program. I get it from baseimage-docker. Thanks a lot, you guys. Procszoo does not require new version Python (but we support python3, too) and Linux kernel.

%package -n python2-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
%description -n python2-%{srcname}
%{desc}

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}
%{desc}
%endif

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python2-%{srcname}
#%license LICENSE.txt
%doc README.first
%doc README.md
%{python2_sitearch}/*
%{_bindir}/*

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
#%license LICENSE.txt
%doc README.first
%doc README.md
%{python3_sitearch}/*
%{_bindir}/*
%endif

