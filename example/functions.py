from typing import TypeVar

from functools import reduce

_InstanceType = TypeVar('_InstanceType')
_PipelineStepType = TypeVar('_PipelineStepType')
_ReturnType = TypeVar('_ReturnType')


def identity(instance: _InstanceType) -> _InstanceType:
    return instance


def flow(
    instance: _InstanceType,
    *functions: _PipelineStepType,
) -> _ReturnType:
    return reduce(_compose, functions)(instance)  # type: ignore


# ===============================
# We are not interested in these:

def _compose(f, g):
    return lambda arg: g(f(arg))
