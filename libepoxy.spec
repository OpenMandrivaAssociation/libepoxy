%global major 0
%define libname %mklibname epoxy %major
%define develname %mklibname -d epoxy

Summary:	Direct Rendering Manager runtime library
Name:		libepoxy
Group:		System/Libraries
Version:	1.5.3
Release:	1
License:	MIT
URL:		http://github.com/anholt/libepoxy
Source0:	https://github.com/anholt/libepoxy/releases/download/%{version}/libepoxy-%{version}.tar.xz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(egl)
BuildRequires:	x11-util-macros
BuildRequires:	meson

%description
A library for handling OpenGL function pointer management.

%package -n %{libname}
Summary: Direct Rendering Manager runtime library
Group: System/Libraries

%description -n %{libname}
A library for handling OpenGL function pointer management.

%package -n %{develname}
Summary:	Development files for libepoxy
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

#check
#make check

%install
%meson_install
find %{buildroot} -type f -name '*.la' -delete -print

%files -n %{libname}
%{_libdir}/libepoxy.so.%{major}*

%files -n %{develname}
%doc README.md
%dir %{_includedir}/epoxy
%{_includedir}/epoxy/*
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc
