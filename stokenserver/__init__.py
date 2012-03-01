# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import logging

from mozsvc.config import get_configurator
from mozsvc.plugin import load_and_register


logger = logging.getLogger('tokenserver')


def includeme(config):
    config.include("cornice")
    config.include("mozsvc")
    config.scan("stokenserver.views")
    load_and_register("metadatadb", config)


def main(global_config, **settings):
    config = get_configurator(global_config, **settings)
    config.include(includeme)
    return config.make_wsgi_app()
