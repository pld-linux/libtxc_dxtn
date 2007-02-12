Summary:	S3TC/DXTN texture compression/decompression library
Summary(pl.UTF-8):   Biblioteka kompresji/dekompresji tekstur S3TC/DXTN
Name:		libtxc_dxtn
Version:	060508
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://homepage.hispeed.ch/rscheidegger/dri_experimental/%{name}%{version}.tar.gz
# Source0-md5:	2b6533617012f5aab52f7f31bd28a8b0
Patch0:		%{name}-make.patch
URL:		http://homepage.hispeed.ch/rscheidegger/dri_experimental/s3tc_index.html
BuildRequires:	OpenGL-devel
#Requires:	Mesa >= 6.3 (or other Mesa-based GL)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3TC/DXTN texture compression/decompression library. It can be
dlopened by Mesa to perform online compression or software
decompression of textures.

%description -l pl.UTF-8
Biblioteka kompresji/dekompresji tekstur S3TC/DXTN. Może być
wczytywana dynamicznie (poprzez dlopen), przez bibliotekę Mesa 
w celu programowej kompresji lub dekompresji tekstur.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT_CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtxc_dxtn.so
