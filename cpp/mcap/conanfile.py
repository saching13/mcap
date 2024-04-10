from conan import ConanFile, tools


class McapConan(ConanFile):
    name = "mcap"
    version = "1.3.0"
    url = "https://github.com/foxglove/mcap"
    homepage = "https://github.com/foxglove/mcap"
    description = "A C++ implementation of the MCAP file format"
    license = "MIT"
    topics = ("mcap", "serialization", "deserialization", "recording")

    settings = ("os", "compiler", "build_type", "arch")
    requires = ("lz4/1.9.4", "zstd/1.5.2")
    generators = "CMakeDeps", "CMakeToolchain"  # Generates conan_toolchain.cmake

    def validate(self):
        tools.build.check_min_cppstd(self, "17")

    def configure(self):
        pass

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses")
        self.copy("include/*")

    def package_id(self):
        self.info.clear()
