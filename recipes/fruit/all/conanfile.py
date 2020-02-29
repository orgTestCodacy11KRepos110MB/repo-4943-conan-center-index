from conans import ConanFile, tools, CMake
from conans.errors import ConanInvalidConfiguration
from conans.tools import Version
import os


class FruitConan(ConanFile):
    name = "fruit"
    description = "C++ dependency injection framework"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/google/fruit"
    license = "Apache"
    topics = ("conan", "fruit", "injection")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "use_boost": [True, False],
               "fPIC": [True, False]}
    default_options = {"shared": False, "use_boost": True, "fPIC": True}
    generators = "cmake", "cmake_find_package"
    exports_sources = ["CMakeLists.txt", "patches/*"]
    _cmake = None

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def requirements(self):
        if self.options.use_boost:
            self.requires("boost/1.72.0")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        compiler = str(self.settings.compiler)
        compiler_version = Version(self.settings.compiler.version.value)

        minimal_version = {
            "gcc": "5",
            "clang": "3.5",
            "apple-clang": "7.3",
            "Visual Studio": "14"
        }

        if compiler in minimal_version and \
           compiler_version < minimal_version[compiler]:
            raise ConanInvalidConfiguration("%s requires a compiler that supports"
                                            " at least C++11. %s %s is not"
                                            " supported." % (self.name, compiler, compiler_version))

        tools.check_min_cppstd(self, "11")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        if not self._cmake:
            self._cmake = CMake(self)
            # fruit doesn't support multi-configuration.
            self._cmake.definitions["CMAKE_BUILD_TYPE"] = self.settings.build_type
            self._cmake.definitions["FRUIT_USES_BOOST"] = self.options.use_boost
            self._cmake.definitions["FRUIT_ENABLE_COVERAGE"] = False
            if self.options.use_boost:
                self._cmake.definitions["BOOST_DIR"] = os.path.join(
                    self.deps_cpp_info["boost"].rootpath, "include")

            self._cmake.configure(build_folder=self._build_subfolder)
        return self._cmake

    def _patch_files(self):
        if self.version in self.conan_data["patches"]:
            for patch in self.conan_data["patches"][self.version]:
                tools.patch(**patch)

    def build(self):
        self._patch_files()

        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("COPYING", dst="licenses", src=self._source_subfolder)

        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
