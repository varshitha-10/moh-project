# Data Masking for PII
import re

def mask_email(email: str) -> str:
    return re.sub(r'(^.).*(@.*$)', r'\1***\2', email)

def mask_phone(phone: str) -> str:
    return re.sub(r'(\d{2})\d{5,}(\d{2})', r'\1*****\2', phone)

def mask_row(row: dict, pii_fields=('email', 'phone')) -> dict:
    masked = row.copy()
    for field in pii_fields:
        if field in masked:
            if field == 'email':
                masked[field] = mask_email(masked[field])
            elif field == 'phone':
                masked[field] = mask_phone(masked[field])
    return masked
