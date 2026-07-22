# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install eos
#
# You can edit this file again by typing:
#
#     spack edit eos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

class Eos(CMakePackage):
    """EOS is a software solution that aims to provide fast and reliable multi-PB disk-only storage technology for both LHC and non-LHC use-cases at CERN.
       The core of the implementation is the XRootD framework which provides feature-rich remote access protocol.
       The storage system is running on commodity hardware with disks in JBOD configuration.
       It is written mostly in C/C++, with some of the extra modules in Python.
       Files can be accessed via native XRootD protocol, a POSIX-like FUSE client or HTTP(S) & WebDav protocol.
    """

    # Add a proper url for your package's homepage here.
    homepage = "https://eos-web.web.cern.ch/eos-web/"
    urls = [
        "https://github.com/cern-eos/eos/archive/refs/tags/5.5.0.tar.gz"
    ]
    git = "https://github.com/cern-eos/eos"

    supplier = "CERN"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("fuhlig1")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("GPL-3.0-or-later", checked_by="fuhlig1")

    # FIXME: Add proper versions here.
    #version("main", branch="main")
    version("5.5.0", tag="5.5.0", get_full_repo=True, submodules=True)
    #version("5.5.0", sha256="011e3f3035145396215bde082c6371ea21f2f19ea5d1532bbf41a123abf86de0", submodules=True)

    variant(
        "cxxstd",
        default="20",
        values=("20", "23"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    # FIXME: Add dependencies if required.
    depends_on('cmake', type='build')

    depends_on("c", type="build") 
    depends_on("cxx", type="build") 

    depends_on("xrootd")
    depends_on("abseil-cpp")
    depends_on("jemalloc")
    depends_on("xrootd")
    depends_on("libzmq")
    depends_on("curl")
    depends_on("libfuse")
    depends_on("zlib")
    depends_on("readline")
    depends_on("util-linux-uuid")
    depends_on("openssl")
    depends_on("ncurses")
    depends_on("krb5")
    depends_on("sparsehash")
    depends_on("jsoncpp")
    depends_on("libevent")
    depends_on("fmt")
    depends_on("bzip2")
    depends_on("rocksdb")
    depends_on("grpc +shared")
    depends_on("protobuf")
    depends_on("glibc")
    depends_on("xfs")
    depends_on("procps")
    depends_on("scitokens-cpp")
    depends_on("davix")
    depends_on("zstd")
    depends_on("snappy")
    depends_on("xxhash")
    depends_on("libnfs")
    depends_on("binutils")
    depends_on("py-sphinx")
    depends_on("help2man")

    patch("eos_find_davix.patch", when="@5.5.0")
    patch("eos_fix_fusex_install.patch", when="@5.5.0")
    patch("eos_fix_etc_install.patch", when="@5.5.0")
    patch("eos_fix_var_install.patch", when="@5.5.0")

    def cmake_args(self):
        spec = self.spec
        define = self.define
        define_from_variant = self.define_from_variant
        options = []

        options += [
            define("CLIENT", True),
            define("VERSION", "5.5.0"),
        ]
        
        options.append("-DROCKSDB_ROOT=%s" % spec["rocksdb"].prefix)
        options.append("-DGRPC_ROOT=%s" % spec["grpc"].prefix)
        options.append("-DABSL_ROOT=%s" % spec["abseil-cpp"].prefix)
        options.append("-DPROTOBUF_ROOT=%s" % spec["protobuf"].prefix)
        options.append("-DSCITOKENS_ROOT=%s" % spec["scitokens-cpp"].prefix)
        options.append("-DDAVIX_ROOT=%s" % spec["davix"].prefix)
        options.append("-DXFS_ROOT=%s" % spec["xfs"].prefix)

        options.append(define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        return options
