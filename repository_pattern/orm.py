from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData, Table, Column, Integer, String

import repository_pattern.model as model


# Usage of SQLAlchemy `Classical Mapping`
metadata = MetaData()

order_lines = Table("order_lines", metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("sku", String(255)),
                    Column("qty", Integer, nullable=True),
                    Column("order_id", String(255)))


def start_mappers():
    order_lines_mapper = mapper(model.OrderLine, order_lines)