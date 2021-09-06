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


class Category(Model):
    """categories of food and their description"""

    id: int = fields.IntField(pk=True, description="ID of the category")
    name: str = fields.CharField(
        max_length=64,
        description="Description of the category",
    )

    class Meta:
        table = "categories"
        table_description = "table of the categories"
