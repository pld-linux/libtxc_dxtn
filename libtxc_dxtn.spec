Summary:	S3TC/DXTN texture compression/decompression library
Summary(pl):	Biblioteka kompresji/dekompresji tekstur S3TC/DXTN
Name:		libtxc_dxtn
Version:	040623
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://homepage.hispeed.ch/rscheidegger/dri_experimental/%{name}%{version}.tar.gz
# Source0-md5:	88fbcac3f7c06390a0c927ab8688e9ce
Patch0:		%{name}-make.patch
URL:		http://homepage.hispeed.ch/rscheidegger/dri_experimental/s3tc_index.html
BuildRequires:	OpenGL-devel
#Requires:	Mesa >= 6.3 (or other Mesa-based GL)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3TC/DXTN texture compression/decompression library. It can be
dlopened by Mesa to perform online compression or software
decompression of textures.

%description -l pl
Biblioteka kompresji/dekompresji tekstur S3TC/DXTN. Mo¿e byæ
wczytywana dynamicznie (przez dlopen) przez bibliotekê Mesa w celu
kompresji lub programowej dekompresji tekstur.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -pedantic"

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
