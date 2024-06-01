# ICU is used by harfbuzz, which is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major %(echo %{version} |cut -d. -f1)
%define libicudata %mklibname icudata %{major}
%define libicui18n %mklibname icui18n %{major}
%define libicuio %mklibname icuio %{major}
%define libicutest %mklibname icutest %{major}
%define libicutu %mklibname icutu %{major}
%define libicuuc %mklibname icuuc %{major}
%define devname %mklibname icu -d
%define lib32icudata %mklib32name icudata %{major}
%define lib32icui18n %mklib32name icui18n %{major}
%define lib32icuio %mklib32name icuio %{major}
%define lib32icutest %mklib32name icutest %{major}
%define lib32icutu %mklib32name icutu %{major}
%define lib32icuuc %mklib32name icuuc %{major}
%define dev32name %mklib32name icu -d
#define beta rc
%ifarch %arm
%define _disable_lto %nil
%endif
%define arch %([ "%{_arch}" = "x86_64" ] && echo -n x86-64 || echo -n %{_arch})
%if "%_lib" == "lib64"
%define archmarker ()(64bit)
%else
%define archmarker %nil
%endif
# Previous versions that are ABI compatible enough for a symlink to (mostly) work
%define compatible 60 61 62 63 64 65 66 67 68 69 70 71 72 73

%define tarballver %(echo %{version}|sed -e 's|\\.|_|g')%{?beta:%{beta}}
%define dashedver %(echo %{version}|sed -e 's|\\.|-|g')%{?beta:-%{beta}}
%if %{defined beta}
%define fsversion %{version}.1
%else
%define fsversion %{version}
%endif

Summary:	International Components for Unicode
Name:		icu74
Version:	74.2
Release:	%{?beta:0.%{beta}.}1
License:	MIT
Group:		System/Libraries
Url:		https://icu.unicode.org/
Source0:	https://github.com/unicode-org/icu/releases/download/release-%{dashedver}/icu4c-%{tarballver}-src.tgz
Source1:	https://github.com/unicode-org/icu/releases/download/release-%{dashedver}/icu4c-%{tarballver}-docs.zip
Source2:	https://raw.githubusercontent.com/unicode-org/icu/main/LICENSE
Patch0:		icu-61.1-DESTDIR.patch
BuildRequires:	doxygen

%description
The International Components for Unicode (ICU) libraries provide robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and they provide support
for supplementary Unicode characters (needed for GB 18030 repertoire support).

As computing environments become more heterogeneous, software portability
becomes more important. ICU lets you produce the same results across all the
various platforms you support, without sacrificing performance. It offers
great flexibility to extend and customize the supplied services, which 
include:

  * Text: Unicode text handling, full character properties and character set
    conversions (500+ codepages)
  * Analysis: Unicode regular expressions; full Unicode sets; character, word
    and line boundaries
  * Comparison: Language sensitive collation and searching
  * Transformations: normalization, upper/lowercase, script transliterations 
    (50+ pairs)
  * Locales: Comprehensive locale data (230+) and resource bundle architecture
  * Complex Text Layout: Arabic, Hebrew, Indic and Thai
  * Time: Multi-calendar and time zone
  * Formatting and Parsing: dates, times, numbers, currencies, messages and   
    rule based

%package doc
Summary:	Documentation for the International Components for Unicode
Group:		System/Libraries
Requires:	%{name} >= %{EVRD}

%description doc
Documentation for the International Components for Unicode.

%package data
Summary:	Data files needed for ICU
Group:		System/Libraries

%description data
Data files needed for ICU.

%package -n %{libicudata}
Summary:	Library for the International Components for Unicode - icudata
Group:		System/Libraries
Obsoletes:	%{mklibname icu 44} <= 4.4.2
Requires(meta):	%{name}-data = %{EVRD}
%if %{defined compatible}
%(for i in %compatible; do echo Provides: %{_lib}icudata$i = %{EVRD}; echo Obsoletes: %{_lib}icudata$i "<" %{EVRD}; echo Provides: "libicudata.so.$i%{archmarker}"; echo Provides: "%{_lib}icudata$i(%{arch})" = %{EVRD}; done)
%endif

%description -n %{libicudata}
Library for the International Components for Unicode - icudata.

%package -n %{libicui18n}
Summary:	Library for the International Components for Unicode - icui18n
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: %{_lib}icui18n$i = %{EVRD}; echo Obsoletes: %{_lib}icui18n$i "<" %{EVRD}; echo Provides: "libicui18n.so.$i%{archmarker}"; echo Provides: "%{_lib}icui18n$i(%{arch})" = %{EVRD}; done)
%endif

%description -n %{libicui18n}
Library for the International Components for Unicode - icui18n.

%package -n %{libicuio}
Summary:	Library for the International Components for Unicode - icuio
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: %{_lib}icuio$i = %{EVRD}; echo Obsoletes: %{_lib}icuio$i "<" %{EVRD}; echo Provides: "libicuio.so.$i%{archmarker}"; echo Provides: "%{_lib}icuio$i(%{arch}) = %{EVRD}"; done)
%endif

%description -n %{libicuio}
Library for the International Components for Unicode - icuio.

%package -n %{libicutest}
Summary:	Library for the International Components for Unicode - icutest
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: %{_lib}icutest$i = %{EVRD}; echo Obsoletes: %{_lib}icutest$i "<" %{EVRD}; echo Provides: "libicutest.so.$i%{archmarker}"; echo Provides: "%{_lib}icutest$i(%{arch}) = %{EVRD}"; done)
%endif

%description -n %{libicutest}
Library for the International Components for Unicode - icutest.

%package -n %{libicutu}
Summary:	Library for the International Components for Unicode - icutu
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: %{_lib}icutu$i = %{EVRD}; echo Obsoletes: %{_lib}icutu$i "<" %{EVRD}; echo Provides: "libicutu.so.$i%{archmarker}"; echo Provides: "%{_lib}icutu$i(%{arch}) = %{EVRD}"; done)
%endif

%description -n %{libicutu}
Library for the International Components for Unicode - icutu.

%package -n %{libicuuc}
Summary:	Library for the International Components for Unicode - icuuc
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: %{_lib}icuuc$i = %{EVRD}; echo Obsoletes: %{_lib}icuuc$i "<" %{EVRD}; echo Provides: "libicuuc.so.$i%{archmarker}"; echo Provides: "%{_lib}icuuc$i(%{arch}) = %{EVRD}"; done)
%endif

%description -n %{libicuuc}
Library for the International Components for Unicode - icuuc.

%package -n %{devname}
Summary:	Development files for the International Components for Unicode
Group:		Development/Other
Requires:	%{libicudata} >= %{EVRD}
Requires:	%{libicui18n} >= %{EVRD}
Requires:	%{libicuio} >= %{EVRD}
Requires:	%{libicutest} >= %{EVRD}
Requires:	%{libicutu} >= %{EVRD}
Requires:	%{libicuuc} >= %{EVRD}
Provides:	%{name}%{major}-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
#define _requires_exceptions statically\\|linked

%description -n	%{devname}
Development files and headers for the International Components for Unicode.

%if %{with compat32}
%package -n %{lib32icudata}
Summary:	Library for the International Components for Unicode - icudata (32-bit)
Group:		System/Libraries
Requires(meta):	%{name}-data = %{EVRD}
BuildRequires:	libc6
%if %{defined compatible}
%(for i in %compatible; do echo Provides: libicudata$i = %{EVRD}; echo Obsoletes: libicudata$i "<" %{EVRD}; echo Provides: "libicudata.so.$i"; done)
%endif

%description -n %{lib32icudata}
Library for the International Components for Unicode - icudata.

%package -n %{lib32icui18n}
Summary:	Library for the International Components for Unicode - icui18n (32-bit)
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: libicui18n$i = %{EVRD}; echo Obsoletes: libicui18n$i "<" %{EVRD}; echo Provides: "libicui18n.so.$i"; done)
%endif

%description -n %{lib32icui18n}
Library for the International Components for Unicode - icui18n.

%package -n %{lib32icuio}
Summary:	Library for the International Components for Unicode - icuio (32-bit)
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: libicuio$i = %{EVRD}; echo Obsoletes: libicuio$i "<" %{EVRD}; echo Provides: "libicuio.so.$i"; done)
%endif

%description -n %{lib32icuio}
Library for the International Components for Unicode - icuio.

%package -n %{lib32icutest}
Summary:	Library for the International Components for Unicode - icutest (32-bit)
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: libicutest$i = %{EVRD}; echo Obsoletes: libicutest$i "<" %{EVRD}; echo Provides: "libicutest.so.$i"; done)
%endif

%description -n %{lib32icutest}
Library for the International Components for Unicode - icutest.

%package -n %{lib32icutu}
Summary:	Library for the International Components for Unicode - icutu (32-bit)
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: libicutu$i = %{EVRD}; echo Obsoletes: libicutu$i "<" %{EVRD}; echo Provides: "libicutu.so.$i"; done)
%endif

%description -n %{lib32icutu}
Library for the International Components for Unicode - icutu.

%package -n %{lib32icuuc}
Summary:	Library for the International Components for Unicode - icuuc (32-bit)
Group:		System/Libraries
%if %{defined compatible}
%(for i in %compatible; do echo Provides: libicuuc$i = %{EVRD}; echo Obsoletes: libicuuc$i "<" %{EVRD}; echo Provides: "libicuuc.so.$i"; done)
%endif

%description -n %{lib32icuuc}
Library for the International Components for Unicode - icuuc.

%package -n %{dev32name}
Summary:	Development files for the International Components for Unicode (32-bit)
Group:		Development/Other
Requires:	%{devname} >= %{EVRD}
Requires:	%{lib32icudata} >= %{EVRD}
Requires:	%{lib32icui18n} >= %{EVRD}
Requires:	%{lib32icuio} >= %{EVRD}
Requires:	%{lib32icutest} >= %{EVRD}
Requires:	%{lib32icutu} >= %{EVRD}
Requires:	%{lib32icuuc} >= %{EVRD}

%description -n	%{dev32name}
Development files and headers for the International Components for Unicode.
%endif

%prep
%autosetup -p1 -n icu

# LICENSE is a dangling symlink, but is being installed
rm LICENSE
cp %{S:2} .

mkdir -p docs
cd docs
unzip -q %{SOURCE1}
cd -

%if %{with compat32}
cp -a source source32
%endif

%if %{cross_compiling}
cp -a source source-native
%endif

%build
%if %{cross_compiling}
cd source-native
./configure \
	--prefix=%{_prefix} \
	--disable-samples \
	--disable-renaming \
	--with-library-bits=64else32 \
	--with-data-packaging=library
%make_build
cd ..
%endif

cd source
%configure \
	--disable-renaming \
%if !%{cross_compiling}
	--with-library-bits=64else32 \
%endif
	--with-data-packaging=archive \
%if %{cross_compiling}
	--with-cross-build=$(realpath $(pwd)/../source-native/) \
%endif
	--disable-samples

#rhbz#225896
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
#rhbz#681941
# As of ICU 52.1 the -nostdlib in tools/toolutil/Makefile results in undefined reference to `__dso_handle'
sed -i 's|^LIBS =.*|LIBS = -L../../lib -licui18n -licuuc -lpthread|' tools/toolutil/Makefile
#rhbz#813484
sed -i 's| \$(docfilesdir)/installdox||' Makefile
# There is no source/doc/html/search/ directory
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
# rhbz#856594 The configure --disable-renaming and possibly other options
# result in icu/source/uconfig.h.prepend being created, include that content in
# icu/source/common/unicode/uconfig.h to propagate to consumer packages.
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h

mkdir -p data/out/tmp
touch -d "10 years ago" data/out/tmp/icudata.lst

%make_build
%make_build doc
cd -

%if %{with compat32}
cd source32
%configure32 --disable-samples \
	--disable-renaming \
	--with-library-bits=64else32 \
	--with-cross-build=$(pwd)/../source \
	--with-data-packaging=archive
#rhbz#225896
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
#rhbz#681941
# As of ICU 52.1 the -nostdlib in tools/toolutil/Makefile results in undefined reference to `__dso_handle'
sed -i 's|^LIBS =.*|LIBS = -L../../lib -licui18n -licuuc -lpthread|' tools/toolutil/Makefile
#rhbz#813484
sed -i 's| \$(docfilesdir)/installdox||' Makefile
# There is no source/doc/html/search/ directory
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
# rhbz#856594 The configure --disable-renaming and possibly other options
# result in icu/source/uconfig.h.prepend being created, include that content in
# icu/source/common/unicode/uconfig.h to propagate to consumer packages.
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h

mkdir -p data/out/tmp
touch -d "10 years ago" data/out/tmp/icudata.lst
%make_build
cd ..
%endif


#% check
#pushd source
#make check
#popd

%install
%if %{with compat32}
%make_install -C source32
%endif
%make_install -C source

%if %{defined compatible}
cd %{buildroot}%{_libdir}
for c in %compatible; do
	for i in *.so.%{major}; do
		ln -s $i ${i/%{major}/$c}
	done
done

%if %{with compat32}
cd %{buildroot}%{_prefix}/lib
for c in %compatible; do
	for i in *.so.%{major}; do
		ln -s $i ${i/%{major}/$c}
	done
done
%endif
%endif

# "current" bits belong to the non-compat package
rm -rf %{buildroot}%{_libdir}/icu/current \
	%{buildroot}%{_libdir}/icu/*.inc

# As do -devel bits
rm -rf	%{buildroot}%{_bindir}/icu-config \
	%{buildroot}%{_libdir}/*.so \
	%{buildroot}%{_libdir}/icu/*.inc \
	%{buildroot}%{_libdir}/icu/%{fsversion}/*.inc \
	%{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_includedir} \
	%{buildroot}%{_datadir}/icu/%{fsversion}/LICENSE \
	%{buildroot}%{_datadir}/icu/%{fsversion}/config \
	%{buildroot}%{_datadir}/icu/%{fsversion}/install-sh \
	%{buildroot}%{_datadir}/icu/%{fsversion}/mkinstalldirs \
	%{buildroot}%{_prefix}/lib/*.so \
	%{buildroot}%{_prefix}/lib/pkgconfig \
	%{buildroot}%{_prefix}/lib/icu/current \
	%{buildroot}%{_prefix}/lib/icu/*.inc \
	%{buildroot}%{_prefix}/lib/icu/%{fsversion}/*.inc

%files
%{_bindir}/*

%files doc
%doc readme.html docs/*
%{_mandir}/man1/*
%{_mandir}/man8/*

%files data
%dir %{_datadir}/icu
%dir %{_datadir}/icu/%{fsversion}
%{_datadir}/icu/%{fsversion}/icudt%{major}l.dat

%files -n %{libicudata}
%{_libdir}/libicudata.so.*

%files -n %{libicui18n}
%{_libdir}/libicui18n.so.*

%files -n %{libicuio}
%{_libdir}/libicuio.so.*

%files -n %{libicutest}
%{_libdir}/libicutest.so.*

%files -n %{libicutu}
%{_libdir}/libicutu.so.*

%files -n %{libicuuc}
%{_libdir}/libicuuc.so.*

%if %{with compat32}
%files -n %{lib32icudata}
%{_prefix}/lib/libicudata.so.*

%files -n %{lib32icui18n}
%{_prefix}/lib/libicui18n.so.*

%files -n %{lib32icuio}
%{_prefix}/lib/libicuio.so.*

%files -n %{lib32icutest}
%{_prefix}/lib/libicutest.so.*

%files -n %{lib32icutu}
%{_prefix}/lib/libicutu.so.*

%files -n %{lib32icuuc}
%{_prefix}/lib/libicuuc.so.*
%endif

# Make sure the compat symlinks don't get removed when
# we replace older packages
%if %{defined compatible}
%(for i in %{compatible}; do
	for l in data i18n io test tu uc; do
		cat <<EOF
%%triggerpostun -- %{_lib}icu$l$i < %{EVRD}
[ -e %{_libdir}/libicu$l.so.$i ] || ln -sf libicu$l.so.%{major} %{_libdir}/libicu$l.so.$i
EOF

%if %{with compat32}
		cat <<EOF
%%triggerpostun -- libicu$l$i < %{EVRD}
[ -e %{_prefix}/lib/libicu$l.so.$i ] || ln -sf libicu$l.so.%{major} %{_prefix}/lib/libicu$l.so.$i
EOF
%endif
	done
done)
%endif
