"""Compatibility module.

Some validators require `inference.py` to exist at the repo root.
The actual FastAPI app lives in `server/app.py`.
"""

from server.app import app  # noqa: F401