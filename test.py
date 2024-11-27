"""
Copyright 2024 Vlad Emelianov
"""

from aioboto3.session import Session

session = Session("aws_access_key_id")
session = Session(None)
session = Session(123)
