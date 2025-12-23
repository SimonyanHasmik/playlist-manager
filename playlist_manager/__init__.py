"""Playlist Manager package.

Expose the API entry point and package metadata here.
"""

__version__ = "0.1.0"

from .api.manager import PlaylistManager

__all__ = ["PlaylistManager"]
