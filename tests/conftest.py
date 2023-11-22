import gzip
import os
from typing import IO, BinaryIO, Iterator

import pytest


def absolute_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), filename)


def open_file(name: str, mode: str = "rb") -> Iterator[IO]:
    with open(absolute_path(name), mode) as f:
        yield f


def open_file_gz(name: str, mode: str = "rb") -> Iterator[IO]:
    with gzip.GzipFile(absolute_path(name), mode) as f:
        yield f


@pytest.fixture
def qnx6_le() -> Iterator[BinaryIO]:
    yield from open_file("data/qnx6-le.bin")


@pytest.fixture
def qnx6_be() -> Iterator[BinaryIO]:
    yield from open_file("data/qnx6-be.bin")


@pytest.fixture
def qnx4() -> Iterator[BinaryIO]:
    yield from open_file("data/qnx4.bin")
