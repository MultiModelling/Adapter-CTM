from enum import Enum
from typing import Dict, Optional, Any, ClassVar, Type
from marshmallow_dataclass import dataclass
from dataclasses import field

from marshmallow import Schema, fields


class ModelState(str, Enum):
    UNKNOWN = "UNKNOWN"
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    QUEUED = "QUEUED"
    READY = "READY"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    ERROR = "ERROR"


@dataclass
class CTMConfig:
    endpoint: str
    CTM_scenario_ID: Optional[str] = None
    ETM_scenario_ID: Optional[str] = None
    CTM_session_ID: Optional[str] = None        # I actually want these not to be inputtable by users
    ETM_session_ID: Optional[str] = None        # We only want ScenarioIDs for CTM and ETM


@dataclass
class CTMAdapterConfig:
    ctm_config: CTMConfig
    base_path: str
    input_esdl_file_path: str
    output_esdl_file_path: str


@dataclass
class ModelRun:
    state: ModelState
    config: CTMAdapterConfig
    result: dict


@dataclass(order=True)
class ModelRunInfo:
    model_run_id: str
    state: ModelState = field(default=ModelState.UNKNOWN)
    result: Optional[Dict[str, Any]] = None
    reason: Optional[str] = None

    # support for Schema generation in Marshmallow
    Schema: ClassVar[Type[Schema]] = Schema
