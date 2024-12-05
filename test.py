"""
Copyright 2024 Vlad Emelianov
"""

from aioboto3.session import Session


async def main() -> None:
    session = Session("aws_access_key_id")
    session = Session(None)
    session = Session(123)

    async with session.client("s3") as client:
        client.create_bucket(Bucket="bucket")
