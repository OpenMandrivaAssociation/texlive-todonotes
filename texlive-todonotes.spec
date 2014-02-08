# revision 27159
# category Package
# catalog-ctan /macros/latex/contrib/todonotes
# catalog-date 2012-07-25 10:56:43 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-todonotes
Version:	20120725
Release:	2
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

%description
The package lets the user mark things to do later, in a simple
and visually appealing way. The package takes several options
to enable customization/finetuning of the visual appearance.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120725-1
+ Revision: 813110
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9.8-2
+ Revision: 757004
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9.8-1
+ Revision: 719776
- texlive-todonotes
- texlive-todonotes
- texlive-todonotes

