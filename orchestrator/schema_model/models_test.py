# orchestrator/models_test.py

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class NodeTestModel(BaseModel):
    name: str
    ip_address: str
    cpu_cores: int = Field(..., ge=1)
    memory_gb: float = Field(..., gt=0)
    status: str
    created_at: Optional[datetime] = datetime.utcnow()


class WorkloadTestModel(BaseModel):
    name: str
    cpu_required: int = Field(..., ge=1)
    memory_required: float = Field(..., gt=0)
    status: str
    assigned_node_id: Optional[int] = None
    created_at: Optional[datetime] = datetime.utcnow()


class EventTestModel(BaseModel):
    type: str
    message: str
    related_workload_id: Optional[int] = None
    timestamp: Optional[datetime] = datetime.utcnow()


# ✅ Example usage for quick testing
if __name__ == "__main__":
    try:
        # Try a valid test object
        node = NodeTestModel(name="node-A", ip_address="192.168.1.10", cpu_cores=4, memory_gb=16.0, status="Healthy")
        print("✅ Node validated:", node)

        # Trigger validation error
        bad_node = NodeTestModel(name="bad-node", ip_address="x.x.x.x", cpu_cores=0, memory_gb=-1, status="Down")
    except ValidationError as e:
        print("❌ Validation Error:", e)

