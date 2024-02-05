# Decision Making Tree

## Classic Mapping
- **Pros**
  - Full control over the configuration
  - Can map to existing tables
- **Cons**
  - More verbose
- **Example**
  ```python
  from sqlalchemy import Table, MetaData, Column, Integer, String
  metadata = MetaData()

  user = Table('user', metadata,
      Column('id', Integer, primary_key=True),
      Column('name', String),
  )
  ```

## Declarative Mapping
- **Pros**
  - Simpler and more Pythonic
  - Automatically creates the table
- **Cons**
  - Less control over the configuration
- **Example**
  ```python
  from sqlalchemy import Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class User(Base):
      __tablename__ = 'user'

      id = Column(Integer, primary_key=True)
      name = Column(String)
  ```

## Dataclasses with SQLAlchemy
- **Pros**
  - Can use Python's built-in dataclasses
  - More Pythonic
- **Cons**
  - Requires SQLAlchemy 1.4 or later
  - Less control over the configuration
- **Example**
  ```python
  from dataclasses import dataclass
  from sqlalchemy import Column, Integer, String
  from sqlalchemy.orm import registry

  mapper_registry = registry()

  @dataclass
  class User:
      __tablename__ = 'user'

      id: int = Column(Integer, primary_key=True)
      name: str = Column(String)
      
  mapper_registry.map_imperatively(User)
  ```

Please note that the dataclasses approach is still experimental in SQLAlchemy and may not support all features.