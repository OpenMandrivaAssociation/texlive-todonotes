# revision 24362
# category Package
# catalog-ctan /macros/latex/contrib/todonotes
# catalog-date 2011-04-21 10:56:14 +0200
# catalog-license lppl
# catalog-version 0.9.8
Name:		texlive-todonotes
Version:	0.9.8
Release:	1
Summary:	Marking things to do in a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/todonotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todonotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todonotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todonotes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package lets the user mark things to do later, in a simple
and visually appealing way. The package takes several options
to enable customization/finetuning of the visual appearance.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/todonotes/todonotes.sty
%doc %{_texmfdistdir}/doc/latex/todonotes/README
%doc %{_texmfdistdir}/doc/latex/todonotes/todonotes.pdf
%doc %{_texmfdistdir}/doc/latex/todonotes/todonotesexample.pdf
%doc %{_texmfdistdir}/doc/latex/todonotes/todonotesexample.tex
#- source
%doc %{_texmfdistdir}/source/latex/todonotes/todonotes.dtx
%doc %{_texmfdistdir}/source/latex/todonotes/todonotes.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
