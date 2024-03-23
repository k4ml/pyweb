from typing import List, Set, Tuple, Type

class MaxSizeExceeded(Exception): ...
class NoSSLError(Exception): ...
class FatalSSLAlert(Exception): ...

def plat_specific_errors(*errnames: str) -> List[int]: ...

socket_error_eintr: List[int]
socket_errors_to_ignore: List[int]
socket_errors_nonblocking: List[int]
acceptable_sock_shutdown_error_codes: Set[int]
acceptable_sock_shutdown_exceptions: Tuple[Type[Exception], ...]
