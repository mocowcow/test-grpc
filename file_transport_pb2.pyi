from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UploadRequest(_message.Message):
    __slots__ = ["filename", "body"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    filename: str
    body: bytes
    def __init__(self, filename: _Optional[str] = ..., body: _Optional[bytes] = ...) -> None: ...

class UploadResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class DownloadRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DownloadResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
