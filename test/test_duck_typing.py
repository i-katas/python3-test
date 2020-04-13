from typing import runtime_checkable, Protocol, TypeVar, abstractmethod, Generic

T = TypeVar('T')


@runtime_checkable
class Consumer(Protocol[T]):
    __slots__ = ()

    @abstractmethod
    def __accept__(self, value: T):
        pass


def test_duck_type_checking():
    class MessageReceiver(Generic[T]):
        def __accept__(self, value: T):
            pass

    assert isinstance(MessageReceiver(), Consumer)
