%global oname  pyinotify

Summary:       Monitor filesystem events with Python under Linux
Name:          python-inotify
Version:       0.9.6
Release:       13%{?dist}
License:       MIT
Group:         Development/Libraries
URL:           https://github.com/seb-m/pyinotify
Source0:       http://seb.dbzteam.org/pub/pyinotify/releases/pyinotify-%{version}.tar.gz
Patch01:       pyinotify-0.9.6-epoint.patch
BuildRequires: gmp-devel
BuildRequires: python3-devel
BuildArch:     noarch

%description
This is a Python module for watching filesystems changes. pyinotify
can be used for various kind of fs monitoring. pyinotify relies on a
recent Linux Kernel feature (merged in kernel 2.6.13) called
inotify. inotify is an event-driven notifier, its notifications are
exported from kernel space to user space.

%package -n    python3-inotify
Summary:       Monitor filesystem events with Python under Linux
Group:         Development/Languages
%{?python_provide:%python_provide python3-inotify}

%description -n python3-inotify
This is a Python 3 module for watching filesystems changes. pyinotify
can be used for various kind of fs monitoring. pyinotify relies on a
recent Linux Kernel feature (merged in kernel 2.6.13) called
inotify. inotify is an event-driven notifier, its notifications are
exported from kernel space to user space.

%prep
%setup -q -n %{oname}-%{version}
%patch01 -p1
rm -rf %{py3dir}
cp -a . %{py3dir}

%build
pushd %{py3dir}
%py3_build
popd

%install
pushd %{py3dir}
%py3_install
popd

%files -n python3-inotify
%license COPYING
%doc ACKS README.md
%{_bindir}/%{oname}
%{python3_sitelib}/%{oname}*
%{python3_sitelib}/__pycache__/%{oname}*

%changelog
* Thu Nov 15 2018 Matej Marusak <mmarusak@redhat.com> - 0.9.6-13
- Only ship one executable (#1646714)

* Mon Apr 09 2018 Miroslav Suchy <msuchy@redhat.com> - 0.9.6-12
- remove python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.6-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.9.6-7
- rebuilt

* Tue Sep 20 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-6
- Add entry point script

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 6 2015 Jakub Filak <jfilak@redhat.com> - 0.9.6-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-1
- 0.9.6

* Mon Apr 13 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-1
- 0.9.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Jakub Filak <jfilak@redhat.com> - 0.9.4-3
- make with_python3 be conditional on fedora

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-1
- 0.9.4

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.3-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.9.3-1
- 0.9.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 02 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.9.2-1
- 0.9.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.9.1-1
- 0.9.1

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9.0-3
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 19 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.0-1
- 0.9.0
- Add python 3 subpackage
- License changed to MIT

* Sun Dec 06 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.8-1
- 0.8.8

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-2.git20090518
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.6-1.git20090518
- Update to latest git, fixing bz #500934.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2.git20090208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-1.git20090208
- 0.8.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8.0-4.r
- Rebuild for Python 2.6

* Sun Jun 22 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.8.0-3.r
- rebuild 

* Tue Jun 17 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.8.0-2.r
- 0.8.0r
- add wrapper in /usr/bin

* Mon Jun 16 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.8.0-1.q
- 0.8.0q
- Update url, license and source url

* Sat Feb  9 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.7.1-2
- Rebuild

* Wed Aug 08 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.7.1-1
- New upstream release: 0.7.1
- Fix license tag

* Mon Jun 25 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.7.0-3
- Remove autopath from example package (bz #237464)

* Tue Mar 27 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.7.0-2
- Fix email address

* Tue Mar  6 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.7.0-1
- Initial build

