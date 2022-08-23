#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0FDE7BE0E88F5E48 (contact@emersion.fr)
#
Name     : libdrm
Version  : 2.4.112
Release  : 89
URL      : https://dri.freedesktop.org/libdrm/libdrm-2.4.112.tar.xz
Source0  : https://dri.freedesktop.org/libdrm/libdrm-2.4.112.tar.xz
Source1  : https://dri.freedesktop.org/libdrm/libdrm-2.4.112.tar.xz.sig
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

%description
What are these headers ?
------------------------
This is the canonical source of drm headers that user space should use for
communicating with the kernel DRM subsystem.

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
%setup -q -n libdrm-2.4.112
cd %{_builddir}/libdrm-2.4.112
pushd ..
cp -a libdrm-2.4.112 build32
popd
pushd ..
cp -a libdrm-2.4.112 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657150120
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dudev=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dudev=true  builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dudev=true -Dcairo-tests=false \
-Dvalgrind=false builddir
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
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
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
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_amdgpu.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_intel.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_nouveau.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_radeon.so
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
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm.so.2.4.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_amdgpu.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_amdgpu.so.1.0.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_intel.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_intel.so.1.0.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_nouveau.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_nouveau.so.2.0.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_radeon.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libdrm_radeon.so.1.0.1
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
