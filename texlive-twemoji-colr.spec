Name:		texlive-twemoji-colr
Version:	64854
Release:	1
Summary:	Twemoji font in COLR/CPAL layered format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/twemoji-colr
License:	cc-by-sa-4 apache2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twemoji-colr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twemoji-colr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a COLR/CPAL-based color OpenType font from the Twemoji
collection of emoji images.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/twemoji-colr
%doc %{_texmfdistdir}/doc/fonts/twemoji-colr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
