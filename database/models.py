"""
This example demonstrates most basic operations with single model. Copied from github.com/tortoise
"""

from tortoise import fields
from tortoise.models import Model


class People(Model):
    """VK id """

    id: int = fields.IntField(pk=True)
    vk_id: int = fields.IntField(description="VK id")

    class Meta:
        table = "event"

    def __str__(self):
        return self.name
