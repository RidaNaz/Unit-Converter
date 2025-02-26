from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

def dynamic_conversion(value, from_unit, to_unit):
    try:
        quantity = Q_(value, from_unit)
        converted_quantity = quantity.to(to_unit)
        return converted_quantity.magnitude, str(converted_quantity.units)
    except Exception as e:
        return None, str(e)