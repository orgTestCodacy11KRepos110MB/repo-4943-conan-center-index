from conan import ConanFile
from conan.tools.build import cross_building
from conan.tools.cmake import CMake, cmake_layout
import os
import textwrap


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualRunEnv"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not cross_building(self):
            with open("test.ini", "w") as fn:
                fn.write(textwrap.dedent("""\
                    [protocol]
                    version = 1337
                    [user]
                    name = conan-center-index
                    email = info@conan.io
                    """))
            bin_path = os.path.join(self.cpp.build.bindirs[0], "test_package")
            self.run(bin_path, env="conanrun")
