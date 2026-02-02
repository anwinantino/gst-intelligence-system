from app.utils.gst_calculator import (
    GSTCalculationInput,
    calculate_gst,
)


def test_intra_state_gst():
    data = GSTCalculationInput(
        taxable_value=100000,
        gst_rate=18,
        supplier_state="Karnataka",
        recipient_state="Karnataka",
    )

    result = calculate_gst(data)

    assert result.tax_type == "CGST_SGST"
    assert result.cgst_amount == 9000
    assert result.sgst_amount == 9000
    assert result.total_tax == 18000
    assert result.total_amount == 118000


def test_inter_state_gst():
    data = GSTCalculationInput(
        taxable_value=50000,
        gst_rate=12,
        supplier_state="Karnataka",
        recipient_state="Tamil Nadu",
    )

    result = calculate_gst(data)

    assert result.tax_type == "IGST"
    assert result.igst_amount == 6000
    assert result.total_tax == 6000
    assert result.total_amount == 56000
