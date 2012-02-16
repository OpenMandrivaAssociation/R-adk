%define modulename adk
%define realver 1.0
%define r_library %{_libdir}/R/library

Summary:	Anderson-Darling k-sample test and combinations of such tests for R
Name:		R-cran-%{modulename}
Version:	%realver
Release:	%mkrel 6
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Anderson-Darling K-sample test can be used to test whether 
several independent random samples of various sizes come from the 
same but unspecified continuous distribution.It is a rank test and 
consistent against all alternatives.A low to moderate number of tied
observations can be tolerated.The combination of such tests can be 
used to test whether M groups of samples (with K allowed to vary from
group to group) come from respective common distributions, which may 
vary from group to group.This is useful in testing for treatment 
effects in randomized (incomplete) block designs or in examining 
whether several laboratories perform equally well when asked to 
measure a sufficient number of test speciments from different batches 
or materials.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
