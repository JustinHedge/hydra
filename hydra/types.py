# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable

from omegaconf import MISSING

TaskFunction = Callable[[Any], Any]


@dataclass
class TargetConf:
    # class, class method or function name
    _target_: str = MISSING


class RunMode(Enum):
    RUN = 1
    MULTIRUN = 2
