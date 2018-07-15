import os
from conans import ConanFile, CMake

class libxmldiffConan(ConanFile):
    name = "libxmldiff"
    version = "0.2.8"
    branch = "master"
    generators = "cmake"
    settings =  "os", "compiler", "arch", "build_type"
    options = {"shared": [False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    url = "http://github.com/kwallner/libxmldiff"
    scm = { "type": "git", "url": "auto", "revision": "auto" }
    
    def config_options(self):
        del self.settings.compiler.libcxx

    def requirements(self):
        self.requires("libxml2/2.9.8@%s/%s" % ("kwallner", "testing"))
        
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        # cmake.test() # FIXME
        #cmake.install()

    def package_info(self):
        self.env_info.libxmldiff_DIR = self.package_folder
