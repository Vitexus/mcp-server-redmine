"""Every tool must carry a title and complete ToolAnnotations."""

import anyio
import pytest

from redmine_mcp_server.server import mcp
from redmine_mcp_server import tools  # noqa: F401  -- registers tools


@pytest.fixture(scope="module")
def registered_tools():
    return anyio.run(mcp.list_tools)


def test_tools_registered(registered_tools):
    assert registered_tools


def test_every_tool_has_title_and_annotations(registered_tools):
    for tool in registered_tools:
        assert tool.title and tool.title != tool.name, tool.name
        a = tool.annotations
        assert a is not None, tool.name
        for hint in (
            "read_only_hint",
            "destructive_hint",
            "idempotent_hint",
            "open_world_hint",
        ):
            assert getattr(a, hint) is not None, f"{tool.name}: {hint} unset"
        assert not (a.read_only_hint and a.destructive_hint), tool.name


def test_name_consistency(registered_tools):
    for tool in registered_tools:
        a = tool.annotations
        if tool.name.startswith(("get_", "list_", "search_")):
            assert a.read_only_hint is True, tool.name
        if "delete" in tool.name:
            assert a.destructive_hint is True, tool.name
