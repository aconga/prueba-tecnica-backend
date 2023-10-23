import re
import boto3
from django.core.exceptions import ValidationError
from botocore.exceptions import NoCredentialsError


def validate_sku(value):
    # Regular expression pattern for SKU (e.g., ABC12345)
    sku_pattern = r"^[A-Z]{3}\d{1,5}$"

    # Check if the SKU matches the pattern
    if not re.match(sku_pattern, value):
        raise ValidationError(
            "Invalid SKU format. It should be in the format ABC12345."
        )


def send_email(subject, message, from_email, recipient_email):
    ses = boto3.client("ses", region_name="us-east-1")

    try:
        response = ses.send_email(
            Source=from_email,  # Debe estar verificada en AWS SES
            Destination={
                "ToAddresses": recipient_email,
            },
            Message={
                "Subject": {
                    "Data": subject,
                },
                "Body": {
                    "Text": {
                        "Data": message,
                    },
                },
            },
        )
        return response
    except NoCredentialsError:
        print("Error: Credenciales de AWS no configuradas.")
        return None
