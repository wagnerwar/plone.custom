# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plone.custom


class PloneCustomLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.custom)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.custom:default')


PLONE_CUSTOM_FIXTURE = PloneCustomLayer()


PLONE_CUSTOM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_CUSTOM_FIXTURE,),
    name='PloneCustomLayer:IntegrationTesting'
)


PLONE_CUSTOM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_CUSTOM_FIXTURE,),
    name='PloneCustomLayer:FunctionalTesting'
)


PLONE_CUSTOM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_CUSTOM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneCustomLayer:AcceptanceTesting'
)
