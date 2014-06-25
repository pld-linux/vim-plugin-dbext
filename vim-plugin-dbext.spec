%define	_v1	4
%define	_v2	03
Summary:	Vim editor database access plugin
Summary(pl.UTF-8):	Wtyczka dostępu do baz danych dla edytora Vim
Name:		vim-plugin-dbext
Version:	%{_v1}.%{_v2}
Release:	1
License:	GPL
Group:		Applications/Editors/Vim
#Source0:	dbext_%{_v1}%{_v2}.zip
Source0:	dbext_%{_v1}00.zip
# Source0-md5:	b843ef4383cb6af21479a01a431270f4
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=356
BuildRequires:	unzip
Requires:	vim >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Plugin contains functions/mappings/commands to enable Vim to access
several databases. Currently MySQL, PostgreSQL, Ingres, Oracle, Sybase
Adaptive Server Anywhere, Sybase Adaptive Server Enterprise, SQLite,
Microsoft SQL Server, DB2 and Interbase are supported.

%description -l pl.UTF-8
Ta wtyczka zawiera funkcje/mapowania/polecenia pozwalające na dostęp
do różnych baz danych z poziomu Vima. Aktualnie obsługiwane są MySQL,
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
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%postun
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%files
%defattr(644,root,root,755)
%{_vimdatadir}/doc/*
%{_vimdatadir}/plugin/*
