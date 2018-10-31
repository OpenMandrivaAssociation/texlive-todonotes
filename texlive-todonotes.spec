Name:		texlive-todonotes
Version:	1.0.7
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
%{_texmfdistdir}/tex/latex/todonotes
%doc %{_texmfdistdir}/doc/latex/todonotes
#- source
%doc %{_texmfdistdir}/source/latex/todonotes

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
