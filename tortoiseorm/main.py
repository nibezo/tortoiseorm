from tortoise import Tortoise, run_async
from database.models import People  # folder|file.py import class_name
from tortoiseorm import converter

idList = converter.convert_id('../tortoiseorm/id.txt')  # converter id from id.txt to Python list


async def id_database():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    for i in range(len(idList)):  # add the id to People table
        await People(vk_id=idList[i]).save()

    # .values_list vs .values - where's the difference?
    print(await People.all().values_list("id", flat=True))
    # >>> [1, ..., 309]
    print(await People.all().values("id", "vk_id"))
    # >>> [{'id': 1, 'vk_id': '106320748'}, {'id': 2, 'vk_id': '107964572'}...]

run_async(id_database())
