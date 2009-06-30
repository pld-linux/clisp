# TODO:
# - review alpha patch
#
# Conditional build:
%bcond_with	tests	# run test suite `make check' (uses network, won't pass on vserver)
#
Summary:	Common Lisp (ANSI CL) implementation
Summary(pl.UTF-8):	Implementacja Common Lisp (ANSI CL)
Summary(pt_BR.UTF-8):	Implementação do Common Lisp (ANSI CL)
Name:		clisp
Version:	2.47
Release:	6
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/clisp/%{name}-%{version}.tar.bz2
# Source0-md5:	8fa89bb13e865fc7c7150b82682f35af
Patch0:		%{name}-shell.patch
Patch1:		%{name}-alpha.patch
Patch2:		%{name}-gcc4.patch
URL:		http://clisp.cons.org/
BuildRequires:	ffcall-devel
BuildRequires:	gettext-devel
BuildRequires:	libsigsegv >= 2.4
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define specflags_ppc	-DNO_GENERATIONAL_GC
%define specflags_ppc64	-DNO_GENERATIONAL_GC

%description
Common Lisp is a high-level, all-purpose programming language. CLISP
is a Common Lisp implementation by Bruno Haible of Karlsruhe
University and Michael Stoll of Munich University, both in Germany. It
mostly supports Common Lisp as described in the ANSI CL standard. It
runs on microcomputers (DOS, OS/2, Windows NT, Windows 95, Amiga
500-4000, Acorn RISC PC) as well as on Unix workstations (Linux, SVR4,
Sun4, DEC Alpha OSF, HP-UX, NeXTstep, SGI, AIX, Sun3 and others) and
needs only 2 MB of RAM.

It is free software and may be distributed under the terms of GNU GPL,
while it is possible to distribute commercial applications compiled
with CLISP.

The user interface comes in German, English, French and Spanish. CLISP
includes an interpreter, a compiler, a large subset of CLOS, a foreign
language interface and a socket interface. An X11 interface is
available through CLX and Garnet.

%description -l pl.UTF-8
Common Lisp to wysokopoziomowy język programowania ogólnego
przeznaczenia. CLISP to implementacja Common Lisp, której autorami są
Bruno Haible z Karlsruhe University oraz Michael Stoll z Munich
University (oba w Niemczech). W większości wspiera Common Lisp opisany
w standardzie ANSI CL. Działa na mikrokomputerach (DOS, OS/2, Windows
NT, Windows 95, Amiga 500-4000, Acorn RICS PC), a także stacjach
uniksowych (Linux, SVR4, Sun4, DEC Alpha OSF, HP-UX, NeXTstep, SGI,
AIX, Sun3 i inne) i wymaga tylko 2 MB RAM.

To jest oprogramowanie wolnodostępne, na licencji GNU GPL, możliwe
jest dystrybuowanie komercyjnych aplikacji skompilowanych CLISP-em.

Interfejs użytkownika dostępny jest po niemiecku, angielsku, francusku
i hiszpańsku. CLISP zawiera interpreter, kompilator, znaczny podzbiór
CLOS, interfejs do innych języków oraz interfejs do gniazdek.
Interfejs X11 jest dostępny poprzez CLX i Garnet.

%description -l pt_BR.UTF-8
Common Lisp é uma linguagem de programação de propósito geral de alto
nível. CLISP é uma implementação do Common Lisp feita por Bruno
Haible, da Universidade Karlsruhe, e Michael Stoll, da Universidade de
Munique, ambas na Alemanha. O CLISP é quase totalmente compatível com
o Common Lisp descrito pelo padrão ANSI CL. Além disso, CLISP é
software livre, distribuído sob os termos da GNU GPL.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1

# changing default -O to optflags causes memory fault on amd64
# - so something is broken... code or compiler
# -fno-strict-aliasing seems to fix crashes on amd64 but doesn't fix
# random crashes on sparc (which occur with default CFLAGS)
#%{__perl} -pi -e "s@' -O2?([^0])@' %{rpmcflags} -fno-strict-aliasing\$1@" src/makemake.in

%build

%ifarch ppc ppc64
ulimit -s unlimited
%else
ulimit -s 32768
%endif

CC="%{__cc}" \
%ifarch sparc sparcv9 sparc64
CFLAGS="%{rpmcflags} -DSAFETY=3" \
%else
CFLAGS="%{rpmcflags}" \
%endif
./configure \
	--prefix=%{_prefix}

cd src
./makemake \
	--prefix=%{_prefix} \
	--with-readline \
	--with-gettext \
	--with-dynamic-ffi \
	--fsstnd=redhat \
	--with-module=wildcard \
	--with-module=bindings/glibc \
	--with-module=clx/new-clx \
	>Makefile
%{__make} -j1 config.lisp \
	TOPDIR=clisp
%{__make} -j1 \
	libdir=%{_libdir} \
	TOPDIR=clisp

%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	lispdocdir=%{_docdir}/%{name}-%{version} \
	mandir=%{_mandir} \
	TOPDIR=clisp

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/modules
install modules/*/*.dvi $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/modules

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clisp
%doc %{_docdir}/%{name}-%{version} 
%dir %{_libdir}/clisp
%dir %{_libdir}/clisp/base
%{_libdir}/clisp/base/*.[aho]
%{_libdir}/clisp/base/lispinit.mem
%attr(755,root,root) %{_libdir}/clisp/base/lisp.run
%{_libdir}/clisp/base/makevars
%{_libdir}/clisp/clisp-link
%{_libdir}/clisp/data
%dir %{_libdir}/clisp/full
%attr(755,root,root) %{_libdir}/clisp/full/lisp.run
%{_libdir}/clisp/full/*.[aho]
%{_libdir}/clisp/full/lispinit.mem
%{_libdir}/clisp/full/makevars
%{_libdir}/clisp/linkkit
%{_mandir}/man[13]/*
