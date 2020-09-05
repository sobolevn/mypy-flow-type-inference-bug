from typing import Callable, Generic, TypeVar, TYPE_CHECKING

if not TYPE_CHECKING:
    reveal_type = print

from example.functions import flow, identity

_ValueType = TypeVar('_ValueType', covariant=True)
_NewValueType = TypeVar('_NewValueType')


# Functor definition:

class Wrapper(Generic[_ValueType]):
    def __init__(self, inner_value: _ValueType) -> None:
        self._inner_value = inner_value

    def map(
        self,
        function: Callable[[_ValueType], _NewValueType],
    ) -> 'Wrapper[_NewValueType]':
        return Wrapper(function(self._inner_value))


T = TypeVar('T')
N = TypeVar('N')


def map_(
    function: Callable[[T], N],
) -> Callable[[Wrapper[T]], Wrapper[N]]:
    def factory(instance: Wrapper[T]) -> Wrapper[N]:
        return instance.map(function)
    return factory


# Example:

def first(arg: int) -> float:
    return float(arg)


def second(arg: float) -> str:
    return str(arg)


instance = Wrapper(1)
reveal_type(flow(instance, map_(first), map_(second)))
