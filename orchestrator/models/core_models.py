from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Node(Base):
    __tablename__ = 'nodes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    ip_address = Column(String, nullable=False)
    capacity_cpu = Column(Float)
    status = Column(String)
    capacity_memory = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    mpods = relationship("MPod", back_populates="node")
    #events = relationship("Event", back_populates="node")
    logs = relationship("Log", back_populates="node")
    scheduling_queues = relationship("SchedulingQueue", back_populates="node")


class Workload(Base):
    __tablename__ = 'workloads'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    #image = Column(String)
    status = Column(String)
    #cpu = Column(Float)
    type = Column(String)
    description = Column(String)
    #memory = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    mpods = relationship("MPod", back_populates="workload")
    events = relationship("Event", back_populates="workload")
    logs = relationship("Log", back_populates="workload")


class MPod(Base):
    __tablename__ = "mpods"
    id = Column(Integer, primary_key=True)
    image = Column(String)
    name = Column(String)
    node_id = Column(Integer, ForeignKey("nodes.id"), index=True)
    workload_id = Column(Integer, ForeignKey("workloads.id"), index=True)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    node = relationship("Node", back_populates="mpods")
    workload = relationship("Workload", back_populates="mpods")
    logs = relationship("Log", back_populates="mpod")
    events = relationship("Event", back_populates="mpod")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    workload_id = Column(Integer, ForeignKey("workloads.id"), index=True)
    mpod_id = Column(Integer, ForeignKey("mpods.id"), index=True)
    type = Column(String)
    message = Column(String)
    timestamp = Column(DateTime)
    #node_id = Column(Integer, ForeignKey("nodes.id"))
    workload = relationship("Workload", back_populates="events")
    #node = relationship("Node", back_populates="events")
    mpod = relationship("MPod", back_populates="events")


class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    mpod_id = Column(Integer, ForeignKey("mpods.id"), index=True)
    node_id = Column(Integer, ForeignKey("nodes.id"), index=True)
    workload_id = Column(Integer, ForeignKey("workloads.id"), index=True)  # ✅ Added
    log_level = Column(String)
    message = Column(String)
    timestamp = Column(DateTime)

    mpod = relationship("MPod", back_populates="logs")
    node = relationship("Node", back_populates="logs")
    workload = relationship("Workload", back_populates="logs")


class SchedulingQueue(Base):
    __tablename__ = "scheduling_queues"
    id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey("nodes.id"))
    workload_id = Column(Integer, ForeignKey("workloads.id"))
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    node = relationship("Node", back_populates="scheduling_queues")

