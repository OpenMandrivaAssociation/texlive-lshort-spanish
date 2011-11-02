Name:		texlive-lshort-spanish
Version:	0.4
Release:	1
Summary:	Short introduction to LaTeX, Spanish translation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/spanish
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-spanish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-spanish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A Spanish translation of the Short Introduction to LaTeX2e,
version 20.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/CAMBIOS
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/LEAME.latin1
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/LEAME.utf8
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/MANIFEST
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/Makefile
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/fixdate.pl
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/biblio.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/contrib.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/custom.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/fancyhea.sty
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/graphic.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-a4.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-a5.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-base.ltx
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-letter.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort.sty
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lssym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/math.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/overview.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/spec.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/things.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/title.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/typeset.tex
%doc %{_texmfdistdir}/doc/latex/lshort-spanish/lshort-a4.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
