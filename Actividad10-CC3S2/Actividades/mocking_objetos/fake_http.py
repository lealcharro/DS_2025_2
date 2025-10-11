import time
from typing import Dict, Any

class FakeHttpClient:
    """No network. Serves preloaded fixtures; can simulate errors/timeouts."""
    def __init__(self, fixtures: Dict[str, Any], delay_ms: int = 0, fail_mode: str | None = None):
        self._fx = fixtures
        self._delay = delay_ms / 1000.0
        self._fail_mode = fail_mode

    def get_json(self, url: str, headers=None, timeout=2.0):
        if self._delay:
            time.sleep(min(self._delay, timeout + 0.05))
        if self._fail_mode == "timeout":
            # Simulate exceeding timeout
            time.sleep(timeout + 0.1)
            raise TimeoutError("request timed out")
        if self._fail_mode == "500":
            raise RuntimeError("HTTP 500 simulated")
        if "malformed" in url:
            return self._fx["malformed_payload"]
        if "Ratings" in url:
            return self._fx["ratings_ok"]
        return self._fx["search_titles_ok"]
