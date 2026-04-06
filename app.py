from __future__ import annotations

from typing import Any, Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

state: Dict[str, Any] = {"step": 0}


class Action(BaseModel):
    action: Any = None


def _reset_state() -> Dict[str, Any]:
    global state
    state = {"step": 0}
    return {"state": state}


def _observation() -> Dict[str, Any]:
    return {"state": state}


@app.post("/reset")
def reset() -> Dict[str, Any]:
    _reset_state()
    return {"observation": _observation(), "info": {}, "state": state}


@app.post("/openenv/reset")
def openenv_reset() -> Dict[str, Any]:
    return reset()


@app.post("/step")
def step(action: Action) -> Dict[str, Any]:
    global state
    state["step"] = int(state.get("step", 0)) + 1
    reward = 1.0
    terminated = False
    truncated = False
    done = terminated or truncated
    return {
        "observation": _observation(),
        "reward": reward,
        "terminated": terminated,
        "truncated": truncated,
        "info": {},
        # Back-compat
        "state": state,
        "done": done,
    }


@app.post("/openenv/step")
def openenv_step(action: Action) -> Dict[str, Any]:
    return step(action)


@app.get("/state")
def get_state() -> Dict[str, Any]:
    return {"state": state}


@app.get("/openenv/state")
def openenv_state() -> Dict[str, Any]:
    return get_state()


@app.get("/openenv/validate")
def openenv_validate_get() -> Dict[str, Any]:
    return {"ok": True}


@app.post("/openenv/validate")
def openenv_validate_post() -> Dict[str, Any]:
    return {"ok": True}


def main() -> None:
    """Console entrypoint used by validators.

    Runs the FastAPI app via uvicorn.
    """

    import uvicorn

    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
