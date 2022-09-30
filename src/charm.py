#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Test node operator.
"""

import logging

from ops.main import main

from hpctinterfaces.relation import interface_registry
from hpctops.charm.node import NodeCharm


logger = logging.getLogger(__name__)


class HpctTestNodeCharm(NodeCharm):
    """Operator for cluster test node."""

    def __init__(self, *args):
        super().__init__(*args)

        self.interfaces = {
            "test-ready": interface_registry.load(
                "relation-subordinate-ready", self, "test-ready"
            ),
        }

        self.setup_subordinate_relations_and_syncs(["test-ready"])


if __name__ == "__main__":
    main(HpctTestNodeCharm)
