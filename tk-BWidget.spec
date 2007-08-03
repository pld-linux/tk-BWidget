Summary:	High-level Widget Set for Tcl/Tk
Summary(pl.UTF-8):	Wysokopoziomowy zestaw widgetów dla Tcl/Tk
Name:		tk-BWidget
Version:	1.8.0
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcllib/BWidget-%{version}.tar.gz
# Source0-md5:	bc590989cae539a9c78fda34e12e277e
URL:		http://sourceforge.net/projects/tcllib/
Requires:	tk >= 8.3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	/usr/lib

%description
The BWidget Toolkit is a high-level Widget Set for Tcl/Tk built using
native Tcl/Tk 8.x namespaces.

The BWidgets have a professional look&feel as in other well known
Toolkits (Tix or Incr Widgets), but the concept is radically different
because everything is pure Tcl/Tk.  No platform dependencies, and no
compiling required.  The code is 100% Pure Tcl/Tk.

%description -l pl.UTF-8
BWidget Toolkit to wysokopoziomowy zestaw widgetów dla Tcl/Tk
zbudowany przy użyciu natywnych przestrzeni nazw Tcl/Tk 8.x.

BWidgets mają profesjonalny wygląd jak w innych dobrze znanych
toolkitach (Tix lub Incr Widgets), ale koncepcyjnie są całkowicie
inne, ponieważ wszystko jest czystym Tcl/Tk. Nie ma zależności od
platformy, nie wymagają kompilacji. Kod jest w 100% czystym Tcl/Tk.

%prep
%setup -qn BWidget-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	$RPM_BUILD_ROOT%{_ulibdir}/%{name}%{version}/{lang,images}

install *.tcl $RPM_BUILD_ROOT%{_ulibdir}/%{name}%{version}
install lang/*  $RPM_BUILD_ROOT%{_ulibdir}//%{name}%{version}/lang
install images/*  $RPM_BUILD_ROOT%{_ulibdir}/%{name}%{version}/images
install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt ChangeLog LICENSE.txt README.txt BWman
%dir %{_ulibdir}/%{name}%{version}
%{_ulibdir}/%{name}%{version}/*.tcl
%{_ulibdir}/%{name}%{version}/images
%dir %{_ulibdir}/%{name}%{version}/lang
%{_ulibdir}/%{name}%{version}/lang/en.rc
%lang(de) %{_ulibdir}/%{name}%{version}/lang/de.rc
%lang(da) %{_ulibdir}/%{name}%{version}/lang/da.rc
%lang(es) %{_ulibdir}/%{name}%{version}/lang/es.rc
%lang(fr) %{_ulibdir}/%{name}%{version}/lang/fr.rc
%{_examplesdir}/%{name}
