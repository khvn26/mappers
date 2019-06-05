from typing import Any, Callable, Dict, List


class Evaluated(object):
    name: str

    def __init__(self, name: str = None) -> None:
      ...


class Mapper(object):
    # TODO: type entity, data_source, and config, their types are not clear

    # TODO: *args cannot be typed at the moment
    def __init__(self, *args) -> None:
        ...

    def reader(self, f: Callable) -> 'Reader':
        ...


# TODO: type is not clear
# TODO: type is dependent, not sure if proper typing is possible
def decompose(args) -> tuple:
    ...


# TODO: this mutates `mapper` instance. Should return different type.
def configure(mapper: Mapper) -> None:
    ...


class Reader(object):
    # TODO: type f, values_list_iterable_class
    values_list_arguments: List[str]
    # TODO: use Union[Optional[T], List[T], ...]
    converter: Callable[[Callable, Mapper], Any]

    # TODO: this will contain type errors, since `Mapper` does not have
    # properties that are specified:
    # - values_list_arguments
    # - values_list_iterable_class
    # We need to add annotations for them in `Mapper` class.
    # But for some reason they are configured in a different place.
    # Either `configure` function should return a different type / protocol,
    # or `Mapper` should always have `values_*` attributes.
    def __init__(self, f: Callable, mapper: Mapper) -> None:
        ...

    # TODO: should have the same return type as `.converter()`
    def __call__(self, *args, **kwargs) -> Any:
        ...

    # TODO: I am not sure about the type here, since there are several issues:
    # 1. `.values_list` is dynamic as hell, no one knows what it will return
    # 2. It is generic to the `f()` return value
    def raw(self, *args, **kwargs) -> Any:
        ...


# Dataclasses.

def is_dataclass(entity) -> bool:
    ...


def get_fields(entity) -> Dict[str, type]:
    ...


# Django.

def is_django_model(data_source) -> bool:
    ...


# TODO: nothing is returned, types are uncleer
def validate_fields(fields, data_source, config) -> None:
    ...


# TODO: types are unclear
def validate_field(validation_field, data_source) -> None:
    ...


# TODO: type other functions of internal API
