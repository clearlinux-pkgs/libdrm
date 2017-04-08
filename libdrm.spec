#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCCC4F07FAC641EFF (daniel@fooishbar.org)
#
Name     : libdrm
Version  : 2.4.78
Release  : 30
URL      : http://dri.freedesktop.org/libdrm/libdrm-2.4.78.tar.gz
Source0  : http://dri.freedesktop.org/libdrm/libdrm-2.4.78.tar.gz
Source99 : http://dri.freedesktop.org/libdrm/libdrm-2.4.78.tar.gz.sig
Summary  : Userspace interface to kernel DRM services
Group    : Development/Tools
License  : MIT
Requires: libdrm-lib
Requires: libdrm-doc
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32pciaccess)
BuildRequires : pkgconfig(32pthread-stubs)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(valgrind)

%description
libdrm - userspace library for drm
This  is libdrm,  a userspace  library for  accessing the  DRM, direct
rendering  manager, on  Linux,  BSD and  other  operating systems that
support the  ioctl interface.  The library  provides wrapper functions
for the  ioctls to avoid  exposing the kernel interface  directly, and
for chipsets with drm memory manager, support for tracking relocations
and  buffers.   libdrm  is  a  low-level library,  typically  used  by
graphics drivers  such as the Mesa  DRI drivers, the  X drivers, libva
and  similar projects.  New  functionality in  the kernel  DRM drivers
typically requires  a new  libdrm, but a  new libdrm will  always work
with an older kernel.

%package dev
Summary: dev components for the libdrm package.
Group: Development
Requires: libdrm-lib
Provides: libdrm-devel

%description dev
dev components for the libdrm package.


%package dev32
Summary: dev32 components for the libdrm package.
Group: Default
Requires: libdrm-lib32
Requires: libdrm-dev

%description dev32
dev32 components for the libdrm package.


%package doc
Summary: doc components for the libdrm package.
Group: Documentation

%description doc
doc components for the libdrm package.


%package lib
Summary: lib components for the libdrm package.
Group: Libraries

%description lib
lib components for the libdrm package.


%package lib32
Summary: lib32 components for the libdrm package.
Group: Default

%description lib32
lib32 components for the libdrm package.


%prep
%setup -q -n libdrm-2.4.78
pushd ..
cp -a libdrm-2.4.78 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491678548
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%configure --disable-static --enable-udev --disable-radeon --disable-nouveau --enable-intel
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-udev --disable-radeon --disable-nouveau --enable-intel --disable-cairo-tests \
--disable-valgrind  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491678548
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libdrm/amdgpu.h
/usr/include/libdrm/amdgpu_drm.h
/usr/include/libdrm/drm.h
/usr/include/libdrm/drm_fourcc.h
/usr/include/libdrm/drm_mode.h
/usr/include/libdrm/drm_sarea.h
/usr/include/libdrm/i915_drm.h
/usr/include/libdrm/intel_aub.h
/usr/include/libdrm/intel_bufmgr.h
/usr/include/libdrm/intel_debug.h
/usr/include/libdrm/mach64_drm.h
/usr/include/libdrm/mga_drm.h
/usr/include/libdrm/nouveau_drm.h
/usr/include/libdrm/qxl_drm.h
/usr/include/libdrm/r128_drm.h
/usr/include/libdrm/radeon_drm.h
/usr/include/libdrm/savage_drm.h
/usr/include/libdrm/sis_drm.h
/usr/include/libdrm/tegra_drm.h
/usr/include/libdrm/vc4_drm.h
/usr/include/libdrm/via_drm.h
/usr/include/libdrm/virtgpu_drm.h
/usr/include/libdrm/vmwgfx_drm.h
/usr/include/libkms/libkms.h
/usr/lib64/libdrm.so
/usr/lib64/libdrm_amdgpu.so
/usr/lib64/libdrm_intel.so
/usr/lib64/libkms.so
/usr/lib64/pkgconfig/libdrm.pc
/usr/lib64/pkgconfig/libdrm_amdgpu.pc
/usr/lib64/pkgconfig/libdrm_intel.pc
/usr/lib64/pkgconfig/libkms.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libdrm.so
/usr/lib32/libdrm_amdgpu.so
/usr/lib32/libdrm_intel.so
/usr/lib32/libkms.so
/usr/lib32/pkgconfig/32libdrm.pc
/usr/lib32/pkgconfig/32libdrm_amdgpu.pc
/usr/lib32/pkgconfig/32libdrm_intel.pc
/usr/lib32/pkgconfig/32libkms.pc
/usr/lib32/pkgconfig/libdrm.pc
/usr/lib32/pkgconfig/libdrm_amdgpu.pc
/usr/lib32/pkgconfig/libdrm_intel.pc
/usr/lib32/pkgconfig/libkms.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man7/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdrm.so.2
/usr/lib64/libdrm.so.2.4.0
/usr/lib64/libdrm_amdgpu.so.1
/usr/lib64/libdrm_amdgpu.so.1.0.0
/usr/lib64/libdrm_intel.so.1
/usr/lib64/libdrm_intel.so.1.0.0
/usr/lib64/libkms.so.1
/usr/lib64/libkms.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libdrm.so.2
/usr/lib32/libdrm.so.2.4.0
/usr/lib32/libdrm_amdgpu.so.1
/usr/lib32/libdrm_amdgpu.so.1.0.0
/usr/lib32/libdrm_intel.so.1
/usr/lib32/libdrm_intel.so.1.0.0
/usr/lib32/libkms.so.1
/usr/lib32/libkms.so.1.0.0
