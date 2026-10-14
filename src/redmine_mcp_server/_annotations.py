"""Shared MCP ToolAnnotations classes (see ~/Projects/MCP-SERVER-STANDARDS.md)."""

from mcp.types import ToolAnnotations

READ_ONLY_ANNOTATIONS = ToolAnnotations(
    read_only_hint=True,
    destructive_hint=False,
    idempotent_hint=True,
    open_world_hint=True,
)
# Creates a new resource on every call - not idempotent.
CREATE_ANNOTATIONS = ToolAnnotations(
    read_only_hint=False,
    destructive_hint=False,
    idempotent_hint=False,
    open_world_hint=True,
)
# Update/delete of an existing resource: overwrites or removes prior state,
# repeating the same call yields the same end state.
MUTATE_ANNOTATIONS = ToolAnnotations(
    read_only_hint=False,
    destructive_hint=True,
    idempotent_hint=True,
    open_world_hint=True,
)
# manage_<x>(action=...) dispatchers: may create, update and delete.
MANAGE_ANNOTATIONS = ToolAnnotations(
    read_only_hint=False,
    destructive_hint=True,
    idempotent_hint=False,
    open_world_hint=True,
)
# Local maintenance (deletes expired files on the server host only).
LOCAL_MUTATE_ANNOTATIONS = ToolAnnotations(
    read_only_hint=False,
    destructive_hint=True,
    idempotent_hint=True,
    open_world_hint=False,
)
