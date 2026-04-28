"""A pocket calculator with a tiny API surface."""

from dataclasses import dataclass


@dataclass
class Calculator:
    """A stateful calculator that accumulates a running value."""

    value: float = 0.0

    def add(self, x: float) -> "Calculator":
        """Add `x` to the running value and return self for chaining."""
        self.value += x
        return self

    def multiply(self, x: float) -> "Calculator":
        """Multiply the running value by `x`."""
        self.value *= x
        return self

    def reset(self) -> None:
        """Reset the running value to zero."""
        self.value = 0.0


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def _internal_helper(x: float) -> float:
    """Private helper — should not be documented in v0.1."""
    return x * 2
