Summary:	System resource guard
Summary(pl):	Stra¿nik zasobów systemowych
Name:		sysfence
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4fc338c0b94c658d6d63b6f91b762b88
URL:		http://sysfence.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sysfence is a Linux system resource monitoring tool. It checks
resource levels (load average, memory, swap, etc.) and makes action if
specified thresholds have been exceeded. It can be used for alerting
admins, dumping system stats in critical moments, or just killing
dangerous processes.

%description -l pl
Sysfence to narzêdzie monitoruj±ce zasoby systemowe Linuksa. Sprawdza
stan zasobów (load average, pamiêæ, swap, itp.) i podejmuje akcjê gdy
zostan± przekroczone ustalone warto¶ci. Mo¿e byæ u¿yty do alarmowania
administratorów, zapisywania informacji o stanie systemu w krytycznych
momentach lub po prostu do zabijania niebezpiecznych procesów.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
install -m 0755 sysfence-* $RPM_BUILD_ROOT%{_bindir}
install -m 0644 README $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
