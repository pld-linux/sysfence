Summary:	System resource guard
Summary(pl):	Stra�nik zasob�w systemowych
Name:		sysfence
Version:	0.15
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://osdn.dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9924311a4c83a99d3aa3b45db2419867
URL:		http://sysfence.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sysfence is a Linux system resource monitoring tool. It checks
resource levels (load average, memory, swap, filesystem space, etc.)
and makes action if specified thresholds have been exceeded. It can
be used for alerting admins, dumping system stats in critical moments,
or just killing dangerous processes.

%description -l pl
Sysfence to narz�dzie monitoruj�ce zasoby systemowe Linuksa. Sprawdza
stan zasob�w (load average, pami��, swap, ilo�� miejsca w systemie
plik�w, itp.) i podejmuje akcj� gdy zostan� przekroczone ustalone
warto�ci. Mo�e by� u�yty do alarmowania administrator�w, zapisywania
informacji o stanie systemu w krytycznych momentach lub po prostu do
zabijania niebezpiecznych proces�w.

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
