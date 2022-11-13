Name:		texlive-lshort-spanish
Version:	35050
Release:	1
Summary:	Short introduction to LaTeX, Spanish translation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/spanish
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-spanish.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-spanish.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
