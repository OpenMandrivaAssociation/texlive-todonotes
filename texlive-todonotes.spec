%global tl_name todonotes
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.7
Release:	%{tl_revision}.1
Summary:	Marking things to do in a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/todonotes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/todonotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/todonotes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/todonotes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pgf)
Requires:	texlive(tools)
Requires:	texlive(xcolor)
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package lets the user mark things to do later, in a simple and
visually appealing way. The package takes several options to enable
customization/finetuning of the visual appearance.

