#
# Conditional build:
%bcond_with	oci	# Oracle module (BR: proprietary libs)
%bcond_with	tests	# run test suite `make check' (uses network, won't pass on vserver)
#
Summary:	Common Lisp (ANSI CL) implementation
Summary(pl.UTF-8):	Implementacja Common Lisp (ANSI CL)
Summary(pt_BR.UTF-8):	Implementação do Common Lisp (ANSI CL)
Name:		clisp
Version:	2.50
Release:	3
License:	GPL v2
Group:		Development/Languages
#Source0Download: https://gitlab.com/gnu-clisp/clisp/-/tags  (2.50 is a not a tag, but branch with no release yet???)
Source0:	https://gitlab.com/gnu-clisp/clisp/-/archive/clisp-%{version}/clisp-clisp-%{version}.tar.bz2
# Source0-md5:	e1813423a98973c2a43b3690c563c024
Patch0:		%{name}-shell.patch
Patch1:		x32.patch
URL:		http://clisp.cons.org/
BuildRequires:	db-devel
BuildRequires:	dbus-devel
BuildRequires:	fcgi-devel
BuildRequires:	ffcall-devel
BuildRequires:	gettext-tools
BuildRequires:	gdbm-devel
BuildRequires:	groff
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libsigsegv-devel >= 2.4
BuildRequires:	libsvm-devel >= 3.0
BuildRequires:	libunistring-devel
BuildRequires:	ncurses-devel
%{?with_oci:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	pari-devel
# share/parigp/pari.desc
BuildRequires:	parigp
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	zlib-devel
Requires:	ffcall-devel
Requires:	libsigsegv-devel >= 2.4
Requires:	libunistring-devel
Requires:	ncurses-devel
Requires:	readline-devel
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

%package module-berkeley-db
Summary:	Berkeley DB module for CLISP
Summary(pl.UTF-8):	Moduł Berkeley DB dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-berkeley-db
Berkeley DB database module for CLISP.

%description module-berkeley-db -l pl.UTF-8
Moduł baz danych Berkeley DB dla CLISP-a.

%package module-clx
Summary:	CLX module for CLISP
Summary(pl.UTF-8):	Moduł CLX dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-clx
CLX (Common Lisp X interface) graphics module for CLISP.

%description module-clx -l pl.UTF-8
Moduł grafiki CTX (interfejs Common List do X) dla CLISP-a.

%package module-dbus
Summary:	DBus module for CLISP
Summary(pl.UTF-8):	Moduł DBus dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-dbus
DBus communication module for CLISP.

%description module-dbus -l pl.UTF-8
Moduł komunikacji DBus dla CLISP-a.

%package module-fastcgi
Summary:	FastCGI module for CLISP
Summary(pl.UTF-8):	Moduł FastCGI dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-fastcgi
FastCGI communication module for CLISP.

%description module-fastcgi -l pl.UTF-8
Moduł komunikacji FastCGI dla CLISP-a.

%package module-gdbm
Summary:	GDBM module for CLISP
Summary(pl.UTF-8):	Moduł GDBM dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-gdbm
GDBM database module for CLISP.

%description module-gdbm -l pl.UTF-8
Moduł baz danych GDBM dla CLISP-a.

%package module-gtk2
Summary:	GTK2 module for CLISP
Summary(pl.UTF-8):	Moduł GTK2 dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-gtk2
GTK2 graphics module for CLISP.

%description module-gtk2 -l pl.UTF-8
Moduł grafiki GTK2 dla CLISP-a.

%package module-libsvm
Summary:	LibSVM module for CLISP
Summary(pl.UTF-8):	Moduł LibSVM dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-libsvm
LibSVM (Support Vector Machine) math module for CLISP.

%description module-libsvm -l pl.UTF-8
Moduł matematyczny LibSVM (Support Vector Machine) dla CLISP-a.

%package module-oracle
Summary:	Oracle module for CLISP
Summary(pl.UTF-8):	Moduł Oracle dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-oracle
Oracle database module for CLISP.

%description module-oracle -l pl.UTF-8
Moduł baz danych Oracle dla CLISP-a.

%package module-pari
Summary:	PARI module for CLISP
Summary(pl.UTF-8):	Moduł PARI dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-pari
PARI math module for CLISP.

%description module-pari -l pl.UTF-8
Moduł matematyczny PARI dla CLISP-a.

%package module-pcre
Summary:	PCRE module for CLISP
Summary(pl.UTF-8):	Moduł PCRE dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-pcre
PCRE matching module for CLISP.

%description module-pcre -l pl.UTF-8
Moduł dopasowań PCRE dla CLISP-a.

%package module-postgresql
Summary:	PostgreSQL module for CLISP
Summary(pl.UTF-8):	Moduł PostgreSQL dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-postgresql
PostgreSQL database module for CLISP.

%description module-postgresql -l pl.UTF-8
Moduł baz danych PostgreSQL dla CLISP-a.

%package module-zlib
Summary:	Zlib module for CLISP
Summary(pl.UTF-8):	Moduł Zlib dla CLISP-a
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description module-zlib
Zlib compression module for CLISP.

%description module-zlib -l pl.UTF-8
Moduł kompresji Zlib dla CLISP-a.

%package -n emacs-clisp-mode
Summary:	CLISP mode for Emacs
Summary(pl.UTF-8):	Tryb edycji CLISP dla Emacsa
Group:		Applications/Editors
Requires:	emacs-common

%description -n emacs-clisp-mode
CLISP mode for Emacs.

%description -n emacs-clisp-mode -l pl.UTF-8
Tryb edycji CLISP dla Emacsa.

%package -n vim-syntax-lisp
Summary:	LISP syntax highlighting for Vim
Summary(pl.UTF-8):	Podświetlanie składni LISP-a w Vimie
Group:		Applications/Editors
Requires:	vim-rt

%description -n vim-syntax-lisp
LISP syntax highlighting for Vim.

%description -n vim-syntax-lisp -l pl.UTF-8
Podświetlanie składni LISP-a w Vimie.

%prep
%setup -q -n clisp-clisp-%{version}
%patch0 -p1
%patch1 -p1

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
%ifarch %{ix86} x32
CFLAGS="%{rpmcflags} -falign-functions=4" \
%else
CFLAGS="%{rpmcflags}" \
%endif
%endif
CPPFLAGS="%{rpmcppflags} -I/usr/include/fastcgi" \
./configure \
%ifarch x32
	--host=%{_target_platform} \
%endif
	--prefix=%{_prefix} \
	--with-pari-datadir=%{_datadir}/parigp \

cd src
./makemake \
	--prefix=%{_prefix} \
	--fsstnd=redhat \
	--with-dynamic-ffi \
	--with-gettext \
	--with-readline \
	--with-module=asdf \
	--with-module=berkeley-db \
	--with-module=bindings/glibc \
	--with-module=clx/new-clx \
	--with-module=dbus \
	--with-module=editor \
	--with-module=fastcgi \
	--with-module=gdbm \
	--with-module=gtk2 \
	--with-module=libsvm \
	%{?with_oci:--with-module=oracle} \
	--with-module=pari \
	--with-module=pcre \
	--with-module=postgresql \
	--with-module=rawsock \
	--with-module=zlib \
	>Makefile
%{__make} -j1 config.lisp \
	TOPDIR=clisp
%{__make} -j1 \
	libdir=%{_libdir} \
	%{?with_oci:ORA_INCLUDES="-I/usr/include/oracle/client"} \
	TOPDIR=clisp

%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	docdir=%{_docdir}/%{name}-%{version} \
	mandir=%{_mandir} \
	TOPDIR=clisp

# already packaged as man/html/pdf
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc/clisp*.{1,ps}

# clisp and clisplow domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clisp
%attr(755,root,root) %{_bindir}/clisp-link
%doc %{_docdir}/%{name}-%{version} 
%dir %{_libdir}/clisp
%dir %{_libdir}/clisp/base
%{_libdir}/clisp/base/*.[aho]
%{_libdir}/clisp/base/lispinit.mem
%attr(755,root,root) %{_libdir}/clisp/base/lisp.run
%{_libdir}/clisp/base/makevars
%{_libdir}/clisp/bindings
%{_libdir}/clisp/build-aux
%{_libdir}/clisp/data
%dir %{_libdir}/clisp/dynmod
%{_libdir}/clisp/dynmod/linux.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-linux.so
%{_libdir}/clisp/linkkit
%{_aclocaldir}/clisp.m4
%{_mandir}/man1/clisp.1*
%{_mandir}/man1/clisp-link.1*

# addtional modules with no external dependencies

%{_libdir}/clisp/asdf
%{_libdir}/clisp/dynmod/asdf.lisp

%{_libdir}/clisp/editor
%{_libdir}/clisp/dynmod/editor.lisp

%{_libdir}/clisp/rawsock
%{_libdir}/clisp/dynmod/rawsock.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-rawsock.so

%files module-berkeley-db
%defattr(644,root,root,755)
%{_libdir}/clisp/berkeley-db
%{_libdir}/clisp/dynmod/bdb.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-bdb.so

%files module-clx
%defattr(644,root,root,755)
%{_libdir}/clisp/clx
%{_libdir}/clisp/dynmod/clx.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-clx.so

%files module-dbus
%defattr(644,root,root,755)
%{_libdir}/clisp/dbus
%{_libdir}/clisp/dynmod/dbus.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-dbus.so

%files module-fastcgi
%defattr(644,root,root,755)
%{_libdir}/clisp/fastcgi
%{_libdir}/clisp/dynmod/fastcgi.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-fastcgi.so

%files module-gdbm
%defattr(644,root,root,755)
%{_libdir}/clisp/gdbm
%{_libdir}/clisp/dynmod/gdbm.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-gdbm.so

%files module-gtk2
%defattr(644,root,root,755)
%{_libdir}/clisp/gtk2
%{_libdir}/clisp/dynmod/gtk.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-gtk.so

%files module-libsvm
%defattr(644,root,root,755)
%{_libdir}/clisp/libsvm
%{_libdir}/clisp/dynmod/libsvm.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-libsvm.so

%if %{with oci}
%files module-oracle
%defattr(644,root,root,755)
%{_libdir}/clisp/oracle
%{_libdir}/clisp/dynmod/oracle.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-oracle.so
%endif

%files module-pari
%defattr(644,root,root,755)
%{_libdir}/clisp/pari
%{_libdir}/clisp/dynmod/pari.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-pari.so

%files module-pcre
%defattr(644,root,root,755)
%{_libdir}/clisp/pcre
%{_libdir}/clisp/dynmod/pcre.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-pcre.so

%files module-postgresql
%defattr(644,root,root,755)
%{_libdir}/clisp/postgresql
%{_libdir}/clisp/dynmod/postgresql.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-postgresql.so

%files module-zlib
%defattr(644,root,root,755)
%{_libdir}/clisp/zlib
%{_libdir}/clisp/dynmod/zlib.lisp
%attr(755,root,root) %{_libdir}/clisp/dynmod/lib-zlib.so

%files -n emacs-clisp-mode
%defattr(644,root,root,755)
%{_lispdir}/clhs.el
%{_lispdir}/clisp-coding.el
%{_lispdir}/clisp-ffi.el
%{_lispdir}/clisp-indent.el
%{_lispdir}/clisp-indent.lisp

%files -n vim-syntax-lisp
%defattr(644,root,root,755)
%{_datadir}/vim/vimfiles/after/syntax/lisp.vim
