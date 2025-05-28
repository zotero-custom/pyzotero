from pathlib import Path

import pytest

from pyzotero.zotero import Zotero

# ruff: noqa: PLR2004
# ruff: noqa: S101


def test_client_with_default_endpoint():
    client = Zotero(library_id=1, library_type="user")
    assert client.endpoint == "https://api.zotero.org"


def test_client_with_custom_endpoint():
    endpoint = "http://localhost:8080"
    client = Zotero(library_id=1, library_type="user", endpoint=endpoint)
    assert client.endpoint == endpoint


def test_client_with_null_endpoint():
    client = Zotero(library_id=1, library_type="user", local=True)
    assert client.endpoint == "http://localhost:23119/api"
