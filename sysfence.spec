Summary:	System resource guard
Summary(pl.UTF-8):   Strażnik zasobów systemowych
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
and makes action if specified thresholds have been exceeded. It can be
used for alerting admins, dumping system stats in critical moments, or
just killing dangerous processes.

%description -l pl.UTF-8
Sysfence to narzędzie monitorujące zasoby systemowe Linuksa. Sprawdza
stan zasobów (load average, pamięć, swap, ilość miejsca w systemie
plików, itp.) i podejmuje akcję gdy zostaną przekroczone ustalone
wartości. Może być użyty do alarmowania administratorów, zapisywania
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

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}{,-%{version}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
