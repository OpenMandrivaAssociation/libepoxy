# libepoxy is used by gtk-3.0, gtk-3.0 is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%global major 0
%define libname %mklibname epoxy %major
%define develname %mklibname -d epoxy
%define lib32name %mklib32name epoxy %major
%define devel32name %mklib32name -d epoxy

%global optflags %{optflags} -O3

Summary:	Direct Rendering Manager runtime library
Name:		libepoxy
Group:		System/Libraries
Version:	1.5.10
Release:	7
License:	MIT
URL:		https://github.com/anholt/libepoxy
Source0:	https://github.com/anholt/libepoxy/releases/download/%{version}/libepoxy-%{version}.tar.xz
# Mirror: https://download.gnome.org/sources/libepoxy/

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	x11-util-macros
BuildRequires:	meson
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libGL)
BuildRequires:	devel(libEGL)
BuildRequires:	devel(libGLESv2)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary: Direct Rendering Manager runtime library (32-bit)
Group: System/Libraries

%description -n %{lib32name}
A library for handling OpenGL function pointer management.

%package -n %{devel32name}
Summary:	Development files for libepoxy
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{devel32name}
This package contains libraries and header files for
developing applications that use %{name}.
%endif

%prep
%autosetup -p1
%if %{with compat32}
%meson32
%endif
%meson

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%meson_install

%files -n %{libname}
%{_libdir}/libepoxy.so.%{major}*

%files -n %{develname}
%doc README.md
%dir %{_includedir}/epoxy
%{_includedir}/epoxy/*
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libepoxy.so.%{major}*

%files -n %{devel32name}
%{_prefix}/lib/libepoxy.so
%{_prefix}/lib/pkgconfig/epoxy.pc
%endif
