Summary:	System resource guard
Summary(pl):	Stra¿nik zasobów systemowych
Name:		sysfence
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/sysfence/%{name}-%{version}.tar.gz
# Source0-md5:	72027d4cea47dade2715540f19f0e077
URL:		http://sysfence.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sysfence is a Linux system resource monitoring tool. It checks
resource levels (load average, memory, swap, filesystem space, etc.)
and makes action if specified thresholds have been exceeded. It can
be used for alerting admins, dumping system stats in critical moments,
or just killing dangerous processes.

%description -l pl
Sysfence to narzêdzie monitoruj±ce zasoby systemowe Linuksa. Sprawdza
stan zasobów (load average, pamiêæ, swap, ilo¶æ miejsca w systemie
plików, itp.) i podejmuje akcjê gdy zostan± przekroczone ustalone
warto¶ci. Mo¿e byæ u¿yty do alarmowania administratorów, zapisywania
informacji o stanie systemu w krytycznych momentach lub po prostu do
zabijania niebezpiecznych procesów.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

mv -f $RPM_BUILD_ROOT%{_datadir}/doc/%{name} $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/%{name}-%{version}/README
%doc %{_datadir}/doc/%{name}-%{version}/example.conf
%attr(755,root,root) %{_bindir}/*
