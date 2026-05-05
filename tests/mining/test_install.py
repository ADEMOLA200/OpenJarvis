"""Tests for openjarvis.mining._install."""
from __future__ import annotations

import sys
import types
from unittest.mock import patch


def test_pearl_packages_available_returns_false_when_pearl_mining_missing():
    from openjarvis.mining import _install

    fake_modules = dict(sys.modules)
    fake_modules.pop("pearl_mining", None)
    fake_modules.pop("pearl_gateway", None)
    fake_modules.pop("miner_base", None)
    with patch.dict(sys.modules, fake_modules, clear=True):
        assert _install.pearl_packages_available() is False


def test_pearl_packages_available_returns_true_when_all_present():
    """When all three are importable, returns True."""
    from openjarvis.mining import _install

    fakes = {
        name: types.ModuleType(name)
        for name in ("pearl_mining", "pearl_gateway", "miner_base")
    }
    with patch.dict(sys.modules, fakes):
        assert _install.pearl_packages_available() is True


def test_install_hint_is_actionable():
    """The hint string must include the extra name and a clear next step."""
    from openjarvis.mining._install import install_hint

    h = install_hint()
    assert "mining-pearl-cpu" in h
    assert "uv sync" in h or "pip install" in h
