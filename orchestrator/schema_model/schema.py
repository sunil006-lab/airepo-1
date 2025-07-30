# orchestrator/schema_model/schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -------------------
# NODE SCHEMA
# -------------------

class NodeBase(BaseModel):
    name: str
    status: str
    ip_address: str
    capacity_cpu: int
    capacity_memory: int  # in MB

class NodeCreate(NodeBase):
    pass

class NodeRead(NodeBase):
    id: int

    class Config:
        orm_mode = True

# -------------------
# WORKLOAD SCHEMA
# -------------------

class WorkloadBase(BaseModel):
    id: Optional[int] = None
    name: str
    type: str
    status: str
    description: str
    created_at: Optional[datetime] = None

class WorkloadCreate(WorkloadBase):
    pass

class WorkloadRead(WorkloadBase):
    id: int

    class Config:
        orm_mode = True

# -------------------
# EVENT SCHEMA
# -------------------

class EventBase(BaseModel):
    id: Optional[int] = None
    workload_id: int
    mpod_id: int
    type: str
    message: str
    timestamp: Optional[datetime] = None

class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: int

    class Config:
        orm_mode = True
# --------------------------
# MPOD SCHEMA
# --------------------------

class MPodBase(BaseModel):
    id: Optional[int] = None
    name: str
    workload_id: int
    node_id: int
    status: str
    image: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Pydantic v2

# ----------------------------
# Scheduling SCHEMA
# ----------------------------

