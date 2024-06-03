#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v12
# autospec commit: fbcebd0
#
Name     : libdrm
Version  : 2.4.121
Release  : 105
URL      : https://dri.freedesktop.org/libdrm/libdrm-2.4.121.tar.xz
Source0  : https://dri.freedesktop.org/libdrm/libdrm-2.4.121.tar.xz
Summary  : Userspace interface to kernel DRM services
Group    : Development/Tools
License  : MIT
Requires: libdrm-data = %{version}-%{release}
Requires: libdrm-lib = %{version}-%{release}
Requires: libdrm-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32atomic_ops)
BuildRequires : pkgconfig(32pciaccess)
BuildRequires : pkgconfig(atomic_ops)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pypi-docutils
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is a historical description of what is now the kgsl backend
in libdrm freedreno (before the upstream drm/msm driver).  Note
that the kgsl backend requires the "kgsl-drm" shim driver, which
usually is in disrepair (QCOM does not build it for android), and
due to random differences between different downstream android
kernel branches it may or may not work.  So YMMV.

%package data
Summary: data components for the libdrm package.
Group: Data

%description data
data components for the libdrm package.


%package dev
Summary: dev components for the libdrm package.
Group: Development
Requires: libdrm-lib = %{version}-%{release}
Requires: libdrm-data = %{version}-%{release}
Provides: libdrm-devel = %{version}-%{release}
Requires: libdrm = %{version}-%{release}

%description dev
dev components for the libdrm package.


%package dev32
Summary: dev32 components for the libdrm package.
Group: Default
Requires: libdrm-lib32 = %{version}-%{release}
Requires: libdrm-data = %{version}-%{release}
Requires: libdrm-dev = %{version}-%{release}

%description dev32
dev32 components for the libdrm package.


%package lib
Summary: lib components for the libdrm package.
Group: Libraries
Requires: libdrm-data = %{version}-%{release}

%description lib
lib components for the libdrm package.


%package lib32
Summary: lib32 components for the libdrm package.
Group: Default
Requires: libdrm-data = %{version}-%{release}

%description lib32
lib32 components for the libdrm package.


%package man
Summary: man components for the libdrm package.
Group: Default

%description man
man components for the libdrm package.


%prep
%setup -q -n libdrm-2.4.121
cd %{_builddir}/libdrm-2.4.121
pushd ..
cp -a libdrm-2.4.121 build32
popd
pushd ..
cp -a libdrm-2.4.121 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717436510
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dudev=true  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dudev=true  builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dudev=true -Dcairo-tests=disabled \
-Dvalgrind=disabled builddir
ninja -v -C builddir
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../build32;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/libdrm/amdgpu.ids

%files dev
%defattr(-,root,root,-)
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
/usr/include/libdrm/msm_drm.h
/usr/include/libdrm/nouveau/nouveau.h
/usr/include/libdrm/nouveau/nvif/cl0080.h
/usr/include/libdrm/nouveau/nvif/cl9097.h
/usr/include/libdrm/nouveau/nvif/class.h
/usr/include/libdrm/nouveau/nvif/if0002.h
/usr/include/libdrm/nouveau/nvif/if0003.h
/usr/include/libdrm/nouveau/nvif/ioctl.h
/usr/include/libdrm/nouveau/nvif/unpack.h
/usr/include/libdrm/nouveau_drm.h
/usr/include/libdrm/qxl_drm.h
/usr/include/libdrm/r128_drm.h
/usr/include/libdrm/r600_pci_ids.h
/usr/include/libdrm/radeon_bo.h
/usr/include/libdrm/radeon_bo_gem.h
/usr/include/libdrm/radeon_bo_int.h
/usr/include/libdrm/radeon_cs.h
/usr/include/libdrm/radeon_cs_gem.h
/usr/include/libdrm/radeon_cs_int.h
/usr/include/libdrm/radeon_drm.h
/usr/include/libdrm/radeon_surface.h
/usr/include/libdrm/savage_drm.h
/usr/include/libdrm/sis_drm.h
/usr/include/libdrm/tegra_drm.h
/usr/include/libdrm/vc4_drm.h
/usr/include/libdrm/via_drm.h
/usr/include/libdrm/virtgpu_drm.h
/usr/include/libdrm/vmwgfx_drm.h
/usr/include/libsync.h
/usr/include/xf86drm.h
/usr/include/xf86drmMode.h
/usr/lib64/libdrm.so
/usr/lib64/libdrm_amdgpu.so
/usr/lib64/libdrm_intel.so
/usr/lib64/libdrm_nouveau.so
/usr/lib64/libdrm_radeon.so
/usr/lib64/pkgconfig/libdrm.pc
/usr/lib64/pkgconfig/libdrm_amdgpu.pc
/usr/lib64/pkgconfig/libdrm_intel.pc
/usr/lib64/pkgconfig/libdrm_nouveau.pc
/usr/lib64/pkgconfig/libdrm_radeon.pc
/usr/share/man/man3/drmAvailable.3
/usr/share/man/man3/drmHandleEvent.3
/usr/share/man/man3/drmModeGetResources.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libdrm.so
/usr/lib32/libdrm_amdgpu.so
/usr/lib32/libdrm_intel.so
/usr/lib32/libdrm_nouveau.so
/usr/lib32/libdrm_radeon.so
/usr/lib32/pkgconfig/32libdrm.pc
/usr/lib32/pkgconfig/32libdrm_amdgpu.pc
/usr/lib32/pkgconfig/32libdrm_intel.pc
/usr/lib32/pkgconfig/32libdrm_nouveau.pc
/usr/lib32/pkgconfig/32libdrm_radeon.pc
/usr/lib32/pkgconfig/libdrm.pc
/usr/lib32/pkgconfig/libdrm_amdgpu.pc
/usr/lib32/pkgconfig/libdrm_intel.pc
/usr/lib32/pkgconfig/libdrm_nouveau.pc
/usr/lib32/pkgconfig/libdrm_radeon.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libdrm.so.2.4.0
/V3/usr/lib64/libdrm_amdgpu.so.1.0.0
/V3/usr/lib64/libdrm_intel.so.1.0.0
/V3/usr/lib64/libdrm_nouveau.so.2.0.0
/V3/usr/lib64/libdrm_radeon.so.1.0.1
/usr/lib64/libdrm.so.2
/usr/lib64/libdrm.so.2.4.0
/usr/lib64/libdrm_amdgpu.so.1
/usr/lib64/libdrm_amdgpu.so.1.0.0
/usr/lib64/libdrm_intel.so.1
/usr/lib64/libdrm_intel.so.1.0.0
/usr/lib64/libdrm_nouveau.so.2
/usr/lib64/libdrm_nouveau.so.2.0.0
/usr/lib64/libdrm_radeon.so.1
/usr/lib64/libdrm_radeon.so.1.0.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libdrm.so.2
/usr/lib32/libdrm.so.2.4.0
/usr/lib32/libdrm_amdgpu.so.1
/usr/lib32/libdrm_amdgpu.so.1.0.0
/usr/lib32/libdrm_intel.so.1
/usr/lib32/libdrm_intel.so.1.0.0
/usr/lib32/libdrm_nouveau.so.2
/usr/lib32/libdrm_nouveau.so.2.0.0
/usr/lib32/libdrm_radeon.so.1
/usr/lib32/libdrm_radeon.so.1.0.1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/drm-kms.7
/usr/share/man/man7/drm-memory.7
/usr/share/man/man7/drm.7
