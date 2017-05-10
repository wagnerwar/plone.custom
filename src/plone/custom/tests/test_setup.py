# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.custom.testing import PLONE_CUSTOM_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone.custom is properly installed."""

    layer = PLONE_CUSTOM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.custom is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.custom'))

    def test_browserlayer(self):
        """Test that IPloneCustomLayer is registered."""
        from plone.custom.interfaces import (
            IPloneCustomLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneCustomLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_CUSTOM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plone.custom'])

    def test_product_uninstalled(self):
        """Test if plone.custom is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.custom'))

    def test_browserlayer_removed(self):
        """Test that IPloneCustomLayer is removed."""
        from plone.custom.interfaces import \
            IPloneCustomLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneCustomLayer, utils.registered_layers())
