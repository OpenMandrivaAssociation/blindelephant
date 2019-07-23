%define snapshot 5

Name:		blindelephant
Version:	7
Release:	1
Summary:	Web Application Finger Printer
License:	LGPL
Group:		Networking/Other
URL:		http://blindelephant.sourceforge.net/
# svn checkout svn://svn.code.sf.net/p/blindelephant/code/trunk blindelephant-code
Source:     %{name}-%{snapshot}.tar.bz2
BuildArch:	noarch

%description
The BlindElephant Web Application Fingerprinter attempts to discover the
version of a (known) web application by comparing static files at known
locations against precomputed hashes for versions of those files in all all
available releases. The technique is fast, low-bandwidth, non-invasive,
generic, and highly automatable.

%prep
%setup -q -n %{name}

%build
cd src
python setup.py build

%install
pushd src
python setup.py install --root=%{buildroot}
popd

install -d -m 755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/blindelephant <<EOF
#!/bin/sh
python %{py_sitedir}/blindelephant/BlindElephant.py
EOF
chmod +x %{buildroot}%{_bindir}/blindelephant

install -d -m 755 %{buildroot}%{_datadir}/%{name}/shell-scripts
install -m 755 tools/shell-scripts/* \
    %{buildroot}%{_datadir}/%{name}/shell-scripts/

%files
%doc README doc/*
%{_bindir}/blindelephant
%{py_sitedir}/blindelephant
%{py_sitedir}/BlindElephant-1.0-py%{py_ver}.egg-info
%{_datadir}/%{name}



