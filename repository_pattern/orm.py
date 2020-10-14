from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, ForeignKey

import repository_pattern.model as model


# Usage of SQLAlchemy `Classical Mapping`
metadata = MetaData()

order_lines = Table("order_lines", metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("sku", String(255)),
                    Column("qty", Integer, nullable=True),
                    Column("order_id", String(255)))

batches = Table("batches", metadata,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("reference", String(255)),
                Column("sku", String(255)),
                Column("_purchased_quantity", Integer, nullable=True),
                Column("eta", Date, nullable=True))

allocations = Table("allocations", metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("orderline_id", ForeignKey("order_lines.id")),
                    Column("batch_id", ForeignKey("batches.id")))


def start_mappers():
    order_lines_mapper = mapper(model.OrderLine, order_lines)
    mapper(model.Batch,
           batches,
           properties={"_allocations": relationship(order_lines_mapper,
                                                    secondary=allocations,
                                                    collection_class=set)})