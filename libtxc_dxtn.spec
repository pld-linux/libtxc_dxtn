Summary:	S3TC/DXTN texture compression/decompression library
Summary(pl.UTF-8):	Biblioteka kompresji/dekompresji tekstur S3TC/DXTN
Name:		libtxc_dxtn
Version:	1.0.1
Release:	2
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	http://people.freedesktop.org/~cbrill/libtxc_dxtn/%{name}-%{version}.tar.bz2
# Source0-md5:	7105107f07ac49753f4b61ba9d0c79c5
URL:		http://people.freedesktop.org/~cbrill/libtxc_dxtn/
BuildRequires:	OpenGL-devel
#Requires:	Mesa >= 6.3 (or other Mesa-based GL)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3TC/DXTN texture compression/decompression library. It can be
dlopened by Mesa to perform online compression or software
decompression of textures.

%description -l pl.UTF-8
Biblioteka kompresji/dekompresji tekstur S3TC/DXTN. Może być
wczytywana dynamicznie (poprzez dlopen), przez bibliotekę Mesa w celu
programowej kompresji lub dekompresji tekstur.

%package devel
Summary:	Header file for txc_dxtn library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki txc_dxtn
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file describing txc_dxtn library API.

%description devel -l pl.UTF-8
Plik nagłówkowy opisujący API biblioteki txc_dxtn.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtxc_dxtn.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtxc_dxtn.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/txc_dxtn.h
