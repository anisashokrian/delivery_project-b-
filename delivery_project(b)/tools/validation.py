import re

def product_validator(product):
    if re.match(r"^[a-zA-Z\d\s_-]{3,30}$", product):
        return product
    else:
        raise ValueError("Invalid product")

def oder_datetime_validator(oder_datetime):
    if re.match(r"^\d{4}-\d{1,2}-\d{1,2}$", oder_datetime):
        return oder_datetime
    else:
        raise ValueError("Invalid oder_datetime")

def deliver_datetime_validator(deliver_datetime):
    if re.match(r"^\d{4}-\d{1,2}-\d{1,2}$", deliver_datetime):
        return deliver_datetime
    else:
        raise ValueError("Invalid deliver_datetime")



