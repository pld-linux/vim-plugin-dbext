%define	_v1	3
%define	_v2	50
Summary:	Vim editor database access plugin
Summary(pl):	Wtyczka dostêpu do baz danych dla edytora Vim
Name:		vim-plugin-dbext
Version:	%{_v1}.%{_v2}
Release:	0.1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	dbext_%{_v1}%{_v2}.zip
# Source0-md5:	25b93ab92cc8ca3bad9cb5fa3ddbfbb1
Requires:	vim >= 4:6.3.058-3
Requires:	vim-plugin-genutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Plugin contains functions/mappings/commands to enable Vim to access
several databases. Currently MySQL, PostgreSQL, Ingres, Oracle, Sybase
Adaptive Server Anywhere, Sybase Adaptive Server Enterprise, SQLite,
Microsoft SQL Server, DB2 and Interbase are supported.

%description -l pl
Ta wtyczka zawiera funkcje/mapowania/polecenia pozwalaj±ce na dostêp
do ró¿nych baz danych z poziomu Vima. Aktualnie obs³ugiwane s± MySQL,
PostgreSQL, Ingres, Oracle, Sybase Adaptive Server Anywhere, Sybase
Adaptive Server Enterprise, SQLite, Microsoft SQL Server, DB2 i
Interbase.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%postun
if [ "$1" = 0 ]; then
	umask 022
	echo ':helptags %{_vimdatadir}/doc' | vim -e -s
fi

%files
%defattr(644,root,root,755)
%{_vimdatadir}/doc/*
%{_vimdatadir}/plugin/*
