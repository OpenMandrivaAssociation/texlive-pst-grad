Name:		texlive-pst-grad
Version:	15878
Release:	2
Summary:	Filling with colour gradients, using PStricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-grad
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-grad.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-grad.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-grad is a PSTricks based package for filling with colour
gradients. Supported are colours in the RGB, CMYK or HSB
models. Other colour gradient mechanisms are to be found in
package pst-slpe.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-grad/pst-grad.pro
%{_texmfdistdir}/tex/generic/pst-grad/pst-grad.tex
%{_texmfdistdir}/tex/latex/pst-grad/pst-grad.sty
%doc %{_texmfdistdir}/doc/generic/pst-grad/Changes
%doc %{_texmfdistdir}/doc/generic/pst-grad/pst-grad-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-grad/pst-grad-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-grad/pst-grad-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
