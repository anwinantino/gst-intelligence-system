from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Date,
    DECIMAL,
    ForeignKey,
    Text,
    TIMESTAMP,
)
from sqlalchemy.sql import func

from app.db.base import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(BigInteger, primary_key=True)
    invoice_number = Column(String(50), unique=True, nullable=False)

    supplier_name = Column(String(255), nullable=False)
    supplier_gstin = Column(String(15), nullable=False)

    buyer_name = Column(String(255), nullable=False)
    buyer_gstin = Column(String(15))

    invoice_date = Column(Date, nullable=False)
    place_of_supply = Column(String(50), nullable=False)

    total_amount = Column(DECIMAL(12, 2), nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(BigInteger, primary_key=True)
    invoice_id = Column(
        BigInteger,
        ForeignKey("invoices.id"),
        nullable=False,
    )

    description = Column(Text, nullable=False)
    hsn_code = Column(String(10), nullable=False)

    quantity = Column(DECIMAL(10, 2), nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    taxable_value = Column(DECIMAL(12, 2), nullable=False)