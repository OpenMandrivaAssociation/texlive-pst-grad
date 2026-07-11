%global tl_name pst-grad
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.06
Release:	%{tl_revision}.1
Summary:	Filling with colour gradients, using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-grad
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-grad.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-grad.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package fills with colour gradients, using PSTricks. The RGB, CMYK
and HSB models are supported. Other colour gradient mechanisms are to be
found in package pst-slpe.

