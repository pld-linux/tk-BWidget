%define		package	bwidget
Summary:	High-level Widget Set for Tcl/Tk
Summary(pl.UTF-8):	Wysokopoziomowy zestaw widgetów dla Tcl/Tk
Name:		tk-BWidget
Version:	1.9.0
Release:	1
License:	TCL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/tcllib/BWidget-%{version}.tar.gz
# Source0-md5:	d4d31f0279c87b024aa3f900a8cbf549
URL:		http://sourceforge.net/projects/tcllib/
BuildRequires:	rpmbuild(macros) >= 1.517
BuildRequires:	sed >= 4.0
BuildRequires:	tcl >= 8.4
Requires:	tcl >= %{tcl_version}
Requires:	tk >= 8.3.3
Obsoletes:	tcl-bwidget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BWidget Toolkit is a high-level Widget Set for Tcl/Tk built using
native Tcl/Tk 8.x namespaces.

The BWidgets have a professional look&feel as in other well known
Toolkits (Tix or Incr Widgets), but the concept is radically different
because everything is pure Tcl/Tk. No platform dependencies, and no
compiling required. The code is 100% Pure Tcl/Tk.

%description -l pl.UTF-8
BWidget Toolkit to wysokopoziomowy zestaw widgetów dla Tcl/Tk
zbudowany przy użyciu natywnych przestrzeni nazw Tcl/Tk 8.x.

BWidgets mają profesjonalny wygląd jak w innych dobrze znanych
toolkitach (Tix lub Incr Widgets), ale koncepcyjnie są całkowicie
inne, ponieważ wszystko jest czystym Tcl/Tk. Nie ma zależności od
platformy, nie wymagają kompilacji. Kod jest w 100% czystym Tcl/Tk.

%prep
%setup -q -n BWidget-%{version}
%{__sed} -i 's/\r//' LICENSE.txt

%install
rm -rf $RPM_BUILD_ROOT
# Don't bother with the included configure script and Makefile.  They
# are missing a lot of pieces and won't work at all.  Installation is
# pretty simple, so we can just do it here manually.
install -d $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}/{lang,images}
cp -a *.tcl $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}
cp -a lang/*.rc $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}/lang
cp -a images/*.gif images/*.xbm $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}/images

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt ChangeLog LICENSE.txt README.txt BWman/*.html
%dir %{tcl_sitelib}/%{package}%{version}
%{tcl_sitelib}/%{package}%{version}/*.tcl
%{tcl_sitelib}/%{package}%{version}/images
%dir %{tcl_sitelib}/%{package}%{version}/lang
%{tcl_sitelib}/%{package}%{version}/lang/en.rc
%lang(da) %{tcl_sitelib}/%{package}%{version}/lang/da.rc
%lang(de) %{tcl_sitelib}/%{package}%{version}/lang/de.rc
%lang(es) %{tcl_sitelib}/%{package}%{version}/lang/es.rc
%lang(fr) %{tcl_sitelib}/%{package}%{version}/lang/fr.rc
%lang(hu) %{tcl_sitelib}/%{package}%{version}/lang/hu.rc
%lang(nl) %{tcl_sitelib}/%{package}%{version}/lang/nl.rc
%lang(no) %{tcl_sitelib}/%{package}%{version}/lang/no.rc
%{_examplesdir}/%{name}-%{version}
