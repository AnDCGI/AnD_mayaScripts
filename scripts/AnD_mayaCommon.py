"""Shared helpers for the AnD Maya scripts.

The tools in this repository are intentionally small shelf scripts. This file
keeps cross-cutting path and configuration behavior in one place so individual
tools can stay simple.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path


def _looks_like_repo(path: Path) -> bool:
    return (path / "prefs" / "shelf" / "shelf_AnDCGI.mel").is_file() and (
        path / "scripts"
    ).is_dir()


def _candidate_roots() -> list[Path]:
    candidates = []

    env_root = os.environ.get("AND_MAYA_REPO_ROOT")
    if env_root:
        candidates.append(Path(env_root).expanduser())

    current_file = Path(__file__).resolve()
    candidates.extend(current_file.parents)

    documents = Path.home() / "Documents"
    candidates.extend(
        [
            documents / "GitHub" / "AnD_mayaScripts",
            documents / "AnD_mayaScripts",
        ]
    )

    try:
        candidates.extend(Path.cwd().resolve().parents)
        candidates.append(Path.cwd().resolve())
    except OSError:
        pass

    return candidates


def repo_root() -> Path:
    for candidate in _candidate_roots():
        if _looks_like_repo(candidate):
            return candidate
    return Path(__file__).resolve().parent.parent


REPO_ROOT = repo_root()
SCRIPTS_ROOT = REPO_ROOT / "scripts"
PY_SCRIPTS_ROOT = SCRIPTS_ROOT / "py-scripts"
PREFS_ROOT = REPO_ROOT / "prefs"
ICONS_ROOT = REPO_ROOT / "icons"
SHELF_FILE = PREFS_ROOT / "shelf" / "shelf_AnDCGI.mel"


def maya_user_dir() -> Path:
    """Return a writable user data directory for tool state/config."""
    root = os.environ.get("AND_MAYA_SCRIPTS_HOME")
    if root:
        path = Path(root).expanduser()
    else:
        path = Path.home() / "Documents" / "AnD_mayaScripts"
    path.mkdir(parents=True, exist_ok=True)
    return path


def config_path() -> Path:
    return maya_user_dir() / "config.json"


def load_config() -> dict:
    path = config_path()
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, ValueError):
        return {}


def config_value(key: str, default=None):
    env_key = "AND_MAYA_" + key.upper()
    if env_key in os.environ:
        return os.environ[env_key]
    return load_config().get(key, default)


def ensure_directory(path) -> Path:
    directory = Path(path).expanduser()
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def temp_state_file(name: str) -> Path:
    return Path(tempfile.gettempdir()) / name


def add_py_script_paths() -> None:
    """Expose every py-scripts subfolder for legacy shelf imports."""
    paths = [SCRIPTS_ROOT, PY_SCRIPTS_ROOT]
    if PY_SCRIPTS_ROOT.exists():
        paths.extend(path for path in PY_SCRIPTS_ROOT.iterdir() if path.is_dir())
    for path in paths:
        value = str(path)
        if value not in sys.path:
            sys.path.insert(0, value)


def add_icon_path() -> None:
    """Expose repository icons to Maya's icon lookup path."""
    value = str(ICONS_ROOT)
    existing = os.environ.get("XBMLANGPATH", "")
    paths = [part for part in existing.split(os.pathsep) if part]
    if value not in paths:
        paths.insert(0, value)
        os.environ["XBMLANGPATH"] = os.pathsep.join(paths)
