Summary:	High-level Widget Set for Tcl/Tk
Summary(pl):	Wysokopoziomowy zestaw widgetów dla Tcl/Tk
Name:		tk-BWidget
Version:	1.4.1
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://prdownloads.sourceforge.net/tcllib/BWidget-%{version}.tar.gz
URL:		http://sourceforge.net/projects/tcllib/
Requires:	tk >= 8.3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BWidget Toolkit is a high-level Widget Set for Tcl/Tk built using
native Tcl/Tk 8.x namespaces.

The BWidgets have a professional look&feel as in other well known
Toolkits (Tix or Incr Widgets), but the concept is radically different
because everything is pure Tcl/Tk.  No platform dependencies, and no
compiling required.  The code is 100% Pure Tcl/Tk.

%prep
%setup -qn BWidget-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}%{version}/{lang,images}

install *.tcl $RPM_BUILD_ROOT%{_libdir}/%{name}%{version}
install lang/*  $RPM_BUILD_ROOT%{_libdir}/%{name}%{version}/lang
install images/*  $RPM_BUILD_ROOT%{_libdir}/%{name}%{version}/images
install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt ChangeLog LICENSE.txt README.txt BWman
%{_libdir}/%{name}%{version}
%{_examplesdir}/%{name}
