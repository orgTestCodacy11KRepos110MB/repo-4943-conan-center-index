from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout
import os

required_conan_version = ">=1.50.0"


class AccessPrivateConan(ConanFile):
    name = "access_private"
    description = "Access private members and statics of a C++ class"
    license = "MIT"
    topics = ("access", "private", "header-only")
    homepage = "https://github.com/martong/access_private"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    def package_id(self):
        self.info.clear()

    def validate(self):
        if self.settings.compiler.get_safe("cppstd"):
            check_min_cppstd(self, 11)

    def layout(self):
        basic_layout(self, src_folder="src")

    def source(self):
        get(self, **self.conan_data["sources"][self.version],
            destination=self.source_folder, strip_root=True)

    def build(self):
        pass

    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, "access_private.hpp",
                   src=os.path.join(self.source_folder, "include"),
                   dst=os.path.join(self.package_folder, "include", "access_private"))

    def package_info(self):
        self.cpp_info.includedirs.append(os.path.join("include", "access_private"))
        self.cpp_info.bindirs = []
        self.cpp_info.frameworkdirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
