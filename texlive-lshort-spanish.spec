Name:		texlive-lshort-spanish
Version:	0.5
Release:	1
Summary:	Short introduction to LaTeX, Spanish translation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/spanish
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-spanish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-spanish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A Spanish translation of the Short Introduction to LaTeX2e,
version 20.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-spanish

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
