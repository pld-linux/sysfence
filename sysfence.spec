Summary:	System resource guard
Summary(pl):	Stra¿nik zasobów systemowych
Name:		sysfence
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://osdn.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	203a7ed38e7ad17c125a4e166c98121c
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
# 0.2 has a bug in Makefile
install -d $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr
mv -f $RPM_BUILD_ROOT%{_datadir}/doc/%{name} $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/%{name}-%{version}/README
%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
