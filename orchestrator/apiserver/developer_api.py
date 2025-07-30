from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
#from orchestrator.schema_model.models import Node, Workload, Event, HealthCheck, GPU, ResourceMetric, SecurityToken, Log, Registry, User, SchedulingQueue, MPod
#from orchestrator.db.databse_query import get_async_session
from orchestrator.models.core_models import Node, Workload, Event
from orchestrator.db.database_query import get_async_session
from orchestrator.schema_model.schema import NodeCreate, WorkloadCreate, EventCreate

app = FastAPI(title="OptiFlow Developer API")

# ----- NODE OPERATIONS -----
@app.post("/nodes/")
async def create_node(node: NodeCreate, session: AsyncSession = Depends(get_async_session)):
    new_node = Node(**node.dict())
    session.add(new_node)
    await session.commit()
    await session.refresh(new_node)
    return new_node

@app.get("/nodes/")
async def get_nodes(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Node))
    return result.scalars().all()

# ----- WORKLOAD OPERATIONS -----
@app.post("/workloads/")
async def create_workload(workload: WorkloadCreate, session: AsyncSession = Depends(get_async_session)):
    new_workload = Workload(**workload.dict())
    session.add(new_workload)
    await session.commit()
    await session.refresh(new_workload)
    return new_workload

@app.get("/workloads/")
async def get_workloads(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Workload))
    return result.scalars().all()

# ----- EVENT OPERATIONS -----
@app.post("/events/")
async def create_event(event: EventCreate, session: AsyncSession = Depends(get_async_session)):
    new_event = Event(**event.dict())
    session.add(new_event)
    await session.commit()
    await session.refresh(new_event)
    return new_event

@app.get("/events/")
async def get_events(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Event))
    return result.scalars().all()

# Extend similarly for: HealthCheck, GPU, ResourceMetric, SecurityToken, Log, Registry, User, SchedulingQueue, MPod

# You can add GET/POST routes for each one like above.

# Placeholder: Health checks root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to OptiFlow Developer API"}

