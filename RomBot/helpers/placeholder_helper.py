import inspect
from typing import Callable


def call_bot_placeholder(placeholder: Callable[..., str], *args):
    sig = inspect.signature(placeholder)
    num_args = len(sig.parameters)
    if num_args > len(args):
        raise ValueError(f"Expected {num_args} arguments, got {len(args)}")
    return placeholder(*args[:num_args])
