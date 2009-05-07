import unittest

class Test_get_metadata(unittest.TestCase):

    def _callFUT(self, path, metadata_version=None):
        from pkginfo.utils import get_metadata
        if metadata_version is not None:
            return get_metadata(path, metadata_version)
        return get_metadata(path)

    def _checkMyPackage(self, dist, filename):
        self.assertEqual(dist.filename, filename)
        self.assertEqual(dist.metadata_version, '1.0')
        self.assertEqual(dist.name, 'mypackage')
        self.assertEqual(dist.version, '0.1')
        self.assertEqual(dist.keywords, None)
        self.assertEqual(list(dist.supported_platforms), [])

    def _checkClassifiers(self, dist):
        self.assertEqual(list(dist.classifiers),
                         ['Development Status :: 4 - Beta',
                          'Environment :: Console (Text Based)',
                         ])

    def test_w_gztar(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.tar.gz' % d
        dist = self._callFUT(filename)
        self._checkMyPackage(dist, filename)

    def test_w_gztar_and_metadata_version(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.tar.gz' % d
        dist = self._callFUT(filename, metadata_version='1.1')
        self._checkMyPackage(dist, filename)
        self._checkClassifiers(dist)

    def test_w_bztar(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.tar.bz2' % d
        dist = self._callFUT(filename)
        self._checkMyPackage(dist, filename)

    def test_w_bztar_and_metadata_version(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.tar.bz2' % d
        dist = self._callFUT(filename, metadata_version='1.1')
        self._checkMyPackage(dist, filename)
        self._checkClassifiers(dist)

    def test_w_zip(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.zip' % d
        dist = self._callFUT(filename)
        self._checkMyPackage(dist, filename)

    def test_w_zip_and_metadata_version(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.zip' % d
        dist = self._callFUT(filename, metadata_version='1.1')
        self._checkMyPackage(dist, filename)
        self._checkClassifiers(dist)

    def test_w_egg(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1-py2.6.egg' % d
        dist = self._callFUT(filename)
        self._checkMyPackage(dist, filename)

    def test_w_egg_and_metadata_version(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1-py2.6.egg' % d
        dist = self._callFUT(filename, metadata_version='1.1')
        self._checkMyPackage(dist, filename)
        self._checkClassifiers(dist)

    def test_w_module(self):
        import pkginfo
        from pkginfo.tests import _checkSample
        dist = self._callFUT(pkginfo)
        _checkSample(self, dist)

    def test_w_module_and_metadata_version(self):
        import pkginfo
        from pkginfo.tests import _checkSample
        from pkginfo.tests import _checkClassifiers
        dist = self._callFUT(pkginfo, metadata_version='1.1')
        _checkSample(self, dist)
        _checkClassifiers(self, dist)

    def test_w_package_name(self):
        from pkginfo.tests import _checkSample
        dist = self._callFUT('pkginfo')
        _checkSample(self, dist)

    def test_w_package_name_and_metadata_version(self):
        from pkginfo.tests import _checkSample
        from pkginfo.tests import _checkClassifiers
        dist = self._callFUT('pkginfo', metadata_version='1.1')
        _checkSample(self, dist)
        _checkClassifiers(self, dist)
