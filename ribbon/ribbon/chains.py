#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By: Paolo@Paradigm
# Created Date: 08/04/2022
# version ='0.1.0'
# ---------------------------------------------------------------------------
""" Module to store Chain class """
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from ribbon.meta import BaseEnum


# ---------------------------------------------------------------------------
# Supported Chains
# ---------------------------------------------------------------------------
class Chains(BaseEnum):
    ETHEREUM = 1
    KOVAN = 42
    AVALANCHE = 43114
    FUJI = 43113
