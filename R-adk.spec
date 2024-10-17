%global packname  adk
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0_2
Release:          2
Summary:          Anderson-Darling K-Sample Test and Combinations of Such Tests
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%rename R-cran-adk

%description
The Anderson-Darling K-sample test can be used to test whether several
independent random samples of various sizes come from the same but
unspecified continuous distribution. It is a rank test and consistent
against all alternatives. A low to moderate number of tied observations
can be tolerated. The combination of such tests can be used to test
whether M groups of samples (with K allowed to vary from group to group)
come from respective common distributions, which may vary from group to
group. This is useful in testing for treatment effects in randomized
(incomplete) block designs or in examining whether several laboratories
perform equally well when asked to measure a sufficient number of test
speciments from different batches or materials.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_1-1
+ Revision: 774828
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2011.0
+ Revision: 616447
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2010.0
+ Revision: 433073
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 260122
- rebuild
- rebuild

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-1mdv2008.1
+ Revision: 170023
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-adk.

