%bcond_with tests

%define srcname cryptography

Name:           python-%{srcname}
Version:        3.3.2
Release:        0
Summary:        PyCA's cryptography library

License:        ASL 2.0 or BSD
URL:            https://github.com/sailfishos/python-cryptography
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  openssl-devel
#BuildRequires:  gcc
BuildRequires:  gnupg2

BuildRequires:  python3-cffi >= 1.7
BuildRequires:  python3-devel
BuildRequires:  python3-idna >= 2.1
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.4.1

%if %{with tests}
BuildRequires:  python3-cryptography-vectors = %{version}
BuildRequires:  python3-hypothesis >= 1.11.4
BuildRequires:  python3-iso8601
BuildRequires:  python3-pretend
BuildRequires:  python3-pytest >= 3.2.1
BuildRequires:  python3-pytz
%endif

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%package -n  python3-%{srcname}
Summary:        PyCA's cryptography library

%description -n python3-%{srcname}
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%py3_build

%install
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete
rm -rf doc

%py3_install

%check
%if %{with tests}

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest -k "not (test_buffer_protocol_alternate_modes or test_dh_parameters_supported or test_load_ecdsa_no_named_curve)"
%endif


%files -n python3-%{srcname}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-*-py*.egg-info
