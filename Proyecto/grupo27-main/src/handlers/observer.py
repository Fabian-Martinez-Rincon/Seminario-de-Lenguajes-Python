from typing import Any, Callable


_subscribers: dict[str, list[Callable[..., None]]] = dict()


def _subscribe(event_type: str, response_fn: Callable[..., None]) -> None:
    if event_type not in _subscribers:
        _subscribers[event_type] = []

    _subscribers[event_type].append(response_fn)


def _unsubscribe(event_type: str, response_fn: Callable[..., None]) -> None:
    if event_type not in _subscribers:
        return

    _subscribers[event_type].remove(response_fn)


def _post_event(event_type: str, data: Any = None) -> None:
    if event_type not in _subscribers:
        return

    for response_fn in _subscribers[event_type]:
        if data is None:
            response_fn()
        else:
            response_fn(data)


def _remove_event(event_type: str) -> None:
    if event_type not in _subscribers:
        return

    _subscribers.pop(event_type)


subscribe = _subscribe
unsubscribe = _unsubscribe
post_event = _post_event
remove_event = _remove_event


def _subscribe_logger(event_type: str, response_fn: Callable[..., None]) -> None:
    print(f'EL: subscribe | {event_type} | {response_fn.__qualname__} ')
    if event_type not in _subscribers:
        _subscribers[event_type] = []

    _subscribers[event_type].append(response_fn)


def _unsubscribe_logger(event_type: str, response_fn: Callable[..., None]) -> None:
    print(f'EL: unsubscribe | {event_type} | {response_fn.__qualname__}')
    if event_type not in _subscribers:
        return

    _subscribers[event_type].remove(response_fn)


def _post_event_logger(event_type: str, data: Any = None) -> None:
    print(
        f'EL: post | {event_type} | {data} | {[fn.__qualname__ for fn in _subscribers[event_type]]}'
    )
    if event_type not in _subscribers:
        return

    for response_fn in _subscribers[event_type]:
        if data is None:
            response_fn()
        else:
            response_fn(data)


def _remove_event_logger(event_type: str) -> None:
    print(
        f'EL: remove | {event_type} | {[fn.__qualname__ for fn in _subscribers[event_type]]}'
    )
    if event_type not in _subscribers:
        return

    _subscribers.pop(event_type)


def enable_logging(state: bool) -> None:
    global subscribe, unsubscribe, post_event, remove_event
    if state:
        print('Event Logger: enabled')
        subscribe = _subscribe_logger
        unsubscribe = _unsubscribe_logger
        post_event = _post_event_logger
        remove_event = _remove_event_logger
    else:
        print('Event Logger: disabled')
        subscribe = _subscribe
        unsubscribe = _unsubscribe
        post_event = _post_event
        remove_event = _remove_event
