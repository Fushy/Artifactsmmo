from collections import OrderedDict, defaultdict
from copy import deepcopy
from datetime import datetime
from functools import wraps
import inspect
import os
from sys import stderr
from time import sleep
from typing import Callable

from dotenv import load_dotenv

from Colors import printc
from Introspection import frameinfo
from Times import now
from Util import chronometer
from conf import V
from constant import *
from swagger_client import ApiClient, CharacterSchema, CharactersApi, DataPageResourceSchema_, ItemsApi, MapsApi, MapSchema, MonstersApi, MonsterSchema, MyAccountApi, MyCharactersApi, ResourcesApi, DefaultApi, ResourceSchema, SingleItemSchema
from swagger_client.rest import ApiException


def task(func):
    # async def wrapper(*args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parameters = list(inspect.signature(func).parameters.keys())
        parameters = {parameters[i]: arg for (i, arg) in enumerate(args) if parameters[i] != "self"}
        name = parameters["name"]
        printc(f"{func.__name__} {parameters}", color="green")
        try:
            result: CharacterSchema = func(*args, **kwargs)
        except ApiException as e:
            print(frameinfo(1)["line"], frameinfo(2)["line"], frameinfo(3)["line"], frameinfo(4)["line"], frameinfo(5)["line"],
                  name, e.status, "sleep 1 sec", e.body, e.headers, file=stderr)
            # if e.status == 478:
            #     # Missing item or insufficient quantity.
            #     return 478
            # if e.status == 497:
            #     print(e.status, e.body["error"], file=stderr)
            #     return
            # await asyncio.sleep(1)
            sleep(2)
            result = wrapper(*args, **kwargs)
        # data: SkillDataSchema = result.data
        # result: CharacterSchema = CharacterSchema(**data.character)
        V["characters"][name]["data"].__dict__ = result.__dict__
        V['characters'][name]['last_action'] = func.__name__
        wait_cooldown_from_result(result)
        # sleep_time = get_cooldown_from_result(V["characters"][name]["data"])
        # chronometer(sleep_time, extra=f"{parameters} {V['characters'][name]['last_action']}"
        #                               f"{API.get_inventory(name, result.inventory)}")
        # sleep(sleep_time)
        # else:
        # await asyncio.sleep(sleep_time)
        return result

    return wrapper


class ArtifactsAPI:

    def __init__(self):
        load_dotenv()
        self.token = os.environ.get("API_TOKEN")
        self.server = os.environ.get("SERVER")
        self.api_client = ApiClient(header_name="Authorization", header_value=f'Bearer {self.token}')
        self.api_client.configuration.host = self.server
        self.api_character = CharactersApi(self.api_client)
        self.api_mycharacter = MyCharactersApi(self.api_client)
        self.api_item = ItemsApi(self.api_client)
        self.api_monster = MonstersApi(self.api_client)
        self.api_resource = ResourcesApi(self.api_client)
        self.api_map = MapsApi(self.api_client)
        self.api_myaccount = MyAccountApi(self.api_client)
        self.api_default = DefaultApi(self.api_client)
        self.offset_time = V["server_offset_time"] = now() - self.get_server_time()

    def get_server_time(self):
        return datetime.fromisoformat(self.api_default.get_status_get().data.server_time[:-1])

    @task
    def move(self, name: str, x: int, y: int) -> CharacterSchema:
        data = {"x": x, "y": y}
        return CharacterSchema(**self.api_mycharacter.action_move_my_name_action_move_post(body=data, name=name).data.character)

    @task
    def fight(self, name: str) -> CharacterSchema:
        return CharacterSchema(**self.api_mycharacter.action_fight_my_name_action_fight_post(name=name).data.character)

    @task
    def gather_resource(self, name: str) -> CharacterSchema:
        return CharacterSchema(**self.api_mycharacter.action_gathering_my_name_action_gathering_post(name=name).data.character)

    @task
    def craft(self, name: str, code: str, quantity: int = 1) -> CharacterSchema:
        return CharacterSchema(
            **self.api_mycharacter.action_crafting_my_name_action_crafting_post(
                name=name, body={"code": code, "quantity": quantity}).data.character)

    @task
    def get_new_task(self, name: str) -> CharacterSchema:
        return CharacterSchema(
            **self.api_mycharacter.action_accept_new_task_my_name_action_task_new_post(name=name).data.character)

    @task
    def bank_deposit_item(self, name: str, code: str, quantity: int) -> CharacterSchema:
        data = {"code": code, "quantity": quantity}
        return CharacterSchema(
            **self.api_mycharacter.action_deposit_bank_my_name_action_bank_deposit_post(name=name, body=data).data.character)

    @task
    def get_from_bank(self, name, code, quantity):
        data = {"code": code, "quantity": quantity}
        return CharacterSchema(
            **self.api_mycharacter.action_withdraw_bank_my_name_action_bank_withdraw_post(body=data, name=name).data.character)

    @task
    def bank_deposit_gold(self, name: str, quantity: int) -> CharacterSchema:
        data = {"quantity": quantity}
        return CharacterSchema(**self.api_mycharacter.action_deposit_bank_gold_my_name_action_bank_deposit_gold_post(
            name=name, body=data).data.character)

    def bank_deposit_items(self, name: str, codes_quantities: dict[str, int]):
        for code, quantity in codes_quantities.items():
            self.bank_deposit_item(name, code, quantity)

    def bank_deposit_all_items(self, name: str, inventory: dict[str, int], except_items=None):
        return self.bank_deposit_items(name, {item: qtt for (item, qtt) in inventory.items()
                                              if not except_items or item not in except_items})


    def get_characters_logs(self, name: str):
        return OrderedDict(sorted((get_all_record_from_pages(
            self.api_mycharacter.get_all_characters_logs_my_logs_get, ["character", "created_at", "type"], stack=True).items())))

    def get_character(self, name: str):
        return self.api_character.get_character_characters_name_get(name=name).data

    def get_my_characters(self) -> list[dict]:
        return self.api_mycharacter.get_my_characters_my_characters_get().data

    # @task
    # def unequip(self, name: str, slot=Slots.WEAPON):
    #     data = {"slot": slot.value}
    #     return self._post(Url.unequip(name), data=data)

    def get_server_characters(self):
        return self.api_character.get_all_characters_characters_get()

    def get_inventory(self, name: str, choose_key=None):
        return get_inventory(name, choose_key)

    def get_item(self, code: str) -> SingleItemSchema:
        """{
      "name": "Cooked Gudgeon",
      "code": "cooked_gudgeon",
      "level": 1,
      "type": "consumable",
      "subtype": "food",
      "description": "Restores 8HP at the start of the turn if the player has lost more than 50% of his health points.",
      "effects": [
        {
          "name": "restore",
          "value": 8
        }
      ],
      "craft": {
        "skill": "cooking",
        "level": 1,
        "items": [
          {
            "code": "gudgeon",
            "quantity": 1
          }
        ],
        "quantity": 1
      }
    }"""
        return self.api_item.get_item_items_code_get(code).data

    def get_items(self, min_level=None, max_level=None, name=None, type_=None, craft_skill=None, craft_material=None,
                  page=None, size=100) -> list[dict]:
        dictionnary = {k: v for (k, v) in {"min_level": min_level, "max_level": max_level, "name": name, "type": type_,
                                           "craft_skill": craft_skill, "craft_material": craft_material, "page": page,
                                           "size": size}.items() if v is not None}
        return sorted(self.api_item.get_all_items_items_get(**dictionnary).data, key=lambda x: list(x.items())[0])

    def get_all_items(self) -> dict[str, dict]:
        return OrderedDict(sorted((get_all_record_from_pages(self.api_item.get_all_items_items_get, "code").items())))

    def get_monster(self, code: str) -> MonsterSchema:
        """{
      "name": "Chicken",
      "code": "chicken",
      "level": 1,
      "hp": 60,
      "attack_fire": 0,
      "attack_earth": 0,
      "attack_water": 4,
      "attack_air": 0,
      "res_fire": 0,
      "res_earth": 0,
      "res_water": 0,
      "res_air": 0,
      "min_gold": 0,
      "max_gold": 1,
      "drops": [
        {
          "code": "raw_chicken",
          "rate": 10,
          "min_quantity": 1,
          "max_quantity": 1
        },
        {
          "code": "egg",
          "rate": 20,
          "min_quantity": 1,
          "max_quantity": 1
        },
        {
          "code": "golden_egg",
          "rate": 5000,
          "min_quantity": 1,
          "max_quantity": 1
        },
        {
          "code": "feather",
          "rate": 10,
          "min_quantity": 1,
          "max_quantity": 1
        }
      ]
    }"""
        return self.api_monster.get_monster_monsters_code_get(code).data

    def get_monsters(self, async_req=None, min_level=None, max_level=None, drop=None, page=None, size=100):
        dictionnary = {k: v for (k, v) in {"async_req": async_req, "min_level": min_level, "max_level": max_level, "drop": drop,
                                           "page": page, "size": size}.items() if v is not None}
        return sorted(self.api_monster.get_all_monsters_monsters_get(**dictionnary).data, key=lambda x: list(x.items())[0])

    def get_all_monster(self) -> dict[str, dict]:
        return OrderedDict(
            sorted((get_all_record_from_pages(self.api_monster.get_all_monsters_monsters_get, "code").items())))

    def get_resource(self, code: str) -> ResourceSchema:
        """{
      "name": "Ash Tree",
      "code": "ash_tree",
      "skill": "woodcutting",
      "level": 1,
      "drops": [
        {
          "code": "ash_wood",
          "rate": 1,
          "min_quantity": 1,
          "max_quantity": 1
        }
      ]
    }"""
        return self.api_resource.get_resource_resources_code_get(code).data

    def get_resources(self, async_req=None, min_level=None, max_level=None, skill=None, drop=None, page=None,
                      size=100, level=None) -> DataPageResourceSchema_:
        min_level = 1 if min_level <= 1 else min_level
        max_level = 1 if max_level <= 1 else max_level
        if level:
            min_level = max_level = level
        dictionnary = {k: v for (k, v) in {"async_req": async_req, "min_level": min_level, "max_level": max_level, "skill": skill,
                                           "drop": drop, "page": page, "size": size}.items() if v is not None}
        return self.api_resource.get_all_resources_resources_get(**dictionnary)

    def get_all_resources(self) -> dict[str, dict]:
        resources = get_all_record_from_pages(self.api_resource.get_all_resources_resources_get, "code")
        return OrderedDict(sorted((resources.items())))

    def get_map(self, pos) -> MapSchema:
        """{
      "name": "Forest",
      "skin": "forest_ogre1",
      "x": -5,
      "y": -5,
      "content": {
        "type": "monster",
        "code": "ogre"
      }
    }"""
        return self.api_map.get_map_maps_xy_get(pos[0], pos[1]).data

    def get_maps(self, async_req=None, content_type=None, content_code=None, page=None,
                 size=100) -> dict[tuple[int, int], dict]:
        dictionnary = {k: v for (k, v) in {"async_req": async_req, "content_type": content_type, "content_code": content_code,
                                           "page": page, "size": size}.items() if v is not None}
        dictionnaries = self.api_map.get_all_maps_maps_get(**dictionnary).data
        return OrderedDict(sorted(({(d["x"], d["y"]): d for d in dictionnaries}).items(), key=lambda x: (x[0][1], x[0][0])))

    def get_all_maps(self) -> dict[tuple[int, int], dict]:
        return OrderedDict(sorted((get_all_record_from_pages(self.api_map.get_all_maps_maps_get, ["x", "y"])).items()))

    def get_bank_golds(self):
        return OrderedDict(sorted((get_all_record_from_pages(self.api_myaccount.get_bank_golds_my_bank_gold_get,
                                                             keys_in_data="code")).items()))

    def get_bank_items(self) -> dict[str, int]:
        bank_items = OrderedDict(
            sorted((get_all_record_from_pages(self.api_myaccount.get_bank_items_my_bank_items_get, keys_in_data="code")).items()))
        return {v["code"]: v["quantity"] for (_, v) in bank_items.items()}

    def is_in_bank(self, code, quantity, bank=None):
        if bank is None:
            bank = self.get_bank_items()
        return code in bank and bank[code] >= quantity



# return self.api_myaccount.get_bank_items_my_bank_items_get()


def wait_cooldown_from_result(result: CharacterSchema) -> bool:
    if not result:
        return False
    cooldown_end = datetime.fromisoformat(result.cooldown_expiration[:-1])
    # sleep_time = (cooldown_end - now(offset_h=-2)).total_seconds()
    sleep_time = (V["server_offset_time"] - (now() - cooldown_end)).total_seconds()
    if sleep_time > 0:
        name = result.name
        chronometer(sleep_time, extra=f"{name} {V['characters'][name]['last_action']} {get_inventory(result.name)}")
    return True


def get_cooldown_from_result(result: CharacterSchema) -> float:
    if not result:
        return False
    cooldown_end = datetime.fromisoformat(result.cooldown_expiration[:-1])
    sleep_time = (cooldown_end - now(offset_h=-2)).total_seconds()
    return max(0, sleep_time)


def get_all_record_from_pages(fun: Callable, keys_in_data: list | object, size=100, stack=False):
    records = {}
    total, page, size = 0, 0, size
    while True:
        page += 1
        results = fun(size=size, page=page)
        if not stack:
            if type(keys_in_data) is list:
                records.update({tuple(data_dict[key] for key in keys_in_data): data_dict for data_dict in results.data})
            else:
                records.update({data_dict[keys_in_data]: data_dict for data_dict in results.data})
        else:
            key_name, key_stack = keys_in_data[0], keys_in_data[1:]
            for result_dict in results.data:
                key = result_dict[key_name]
                if key not in records:
                    records[key] = {}
                if type(key_stack) is list:
                    records[key].update({tuple(result_dict[key] for key in key_stack): result_dict})
                else:
                    records[key].update({result_dict[key_stack]: result_dict})
        total += size
        if total > results.total:
            return records


def get_map_from_resource(async_req=None, min_level=None, max_level=None, level=None, skill=None, drop=None,
                          content_code=None):
    min_level = 1 if min_level <= 1 else min_level
    max_level = 1 if max_level <= 1 else max_level
    if level:
        min_level = max_level = level
    dictionnary = {k: v for (k, v) in {"async_req": async_req, "min_level": min_level, "max_level": max_level,
                                       "skill": skill, "drop": drop, "content_code": content_code}.items() if v is not None}
    resources = API.get_resources(**dictionnary).data
    results = []
    for resource in resources:
        positions = API.get_maps(content_code=resource["code"])
        for position in positions:
            positions[position]["level"] = resource["level"]
            positions[position]["skill"] = resource["skill"]
        results.append(positions)
    return results


def get_inventory(name, choose_key=None):
    inventory = V["characters"][name]["data"].inventory
    if choose_key:
        return [(item[choose_key] if choose_key else item) for item in inventory if item["quantity"] > 0]
    return {inventory["code"]: inventory["quantity"] for inventory in inventory if inventory["quantity"] > 0}


def get_inventory_sum(inventory):
    return sum(inventory.values())


def get_max_amount_to_craft(name, code, max_inventory_quantity=None, inventory=None):
    if inventory is None or max_inventory_quantity is None:
        data = API.get_character(name)
        # inventory = get_inventory(data.inventory)
        max_inventory_quantity = data.inventory_max_items
    recipes = API.get_item(code).item["craft"]["items"]
    amount_to_craft = 0
    while max_inventory_quantity > 0:
        for recipe in recipes:
            max_inventory_quantity -= recipe["quantity"]
        amount_to_craft += 1
    return amount_to_craft - 1


def get_amount_recipe_to_craft(code):
    recipes = API.get_item(code).item["craft"]["items"]
    return sum(recipe["quantity"] for recipe in recipes)


API = ArtifactsAPI()


def able_to_craft(bank_items: dict[str, int], recipe_items: dict[str, list[dict[str, int]]]):
    bank_items = defaultdict(int, deepcopy(bank_items))
    for recipe_item in recipe_items["items"]:
        recipe_code, recipe_quantity = recipe_item["code"], recipe_item["quantity"]
        if recipe_code in bank_items:
            recipe_item["doable_quantity"] = bank_items[recipe_code] // recipe_quantity
        else:
            # return 0, bank_items
            return 0
    doable_quantity = min(recipe_item["doable_quantity"] for recipe_item in recipe_items["items"])
    # bank_items[recipe_items["code"]] += doable_quantity
    # for recipe_item in recipe_items["items"]:
    # bank_items[recipe_item["code"]] -= doable_quantity * recipe_item["quantity"]
    # return doable_quantity, bank_items
    return doable_quantity


def get_current_craftable_items(max_level=None, level=None, effect=None, skill=None,
                                filter_fun: Callable = lambda x: x) -> dict[str, dict]:
    bank_items = defaultdict(int, API.get_bank_items())
    craft_table = get_craft_table()
    craftable = {}
    while True:
        i = 0
        for code, craft_item in craft_table.items():
            craft_item["code"] = code
            doable_quantity = able_to_craft(bank_items, craft_item)
            if doable_quantity and code not in craftable:
                bank_items[code] = doable_quantity
                craftable[code] = {"quantity": doable_quantity, "level": craft_item["level"],
                                   "recipes": craft_item["items"], "skill": craft_item["skill"], "effects": craft_item["effects"]}
                break
            i += 1
        if i == len(craft_table):
            break
    craftable = OrderedDict(sorted(craftable.items(), key=lambda x: x[1]["level"], reverse=True))
    return craft_table_filter(craftable, effect, filter_fun, level, max_level, skill)


def craft_table_filter(craftable, effect, filter_fun, level, max_level, skill):
    craftable = filter_fun(craftable)
    if level:
        craftable = {code: item for code, item in craftable.items() if item['level'] == level}
    elif max_level:
        craftable = {code: item for code, item in craftable.items() if item['level'] <= max_level}
    if effect:
        craftable = {code: item for code, item in craftable.items()
                     if any(effect.lower() in effect_['name'] for effect_ in item['effects'])}
    if skill:
        craftable = {code: item for code, item in craftable.items() if item['skill'] == skill}
    return craftable


def get_craft_table(max_level=None, level=None, effect=None, skill=None,
                    filter_fun: Callable = lambda x: x):
    craft_table = {}
    for craft_item, d in API.get_all_items().items():
        if "craft" in d and d["craft"]:
            craft_table[craft_item] = d["craft"]
            craft_table[craft_item]["effects"] = d["effects"]
    return craft_table_filter(craft_table, effect, filter_fun, level, max_level, skill)


if __name__ == '__main__':
    # API.get_character("Hysfu")
    # API.move("Hysfu", 1, 1)
    # characters = API.get_my_characters()
    # inventory = API.get_inventory("Fushy")
    # inventories = API.get_inventory("Fushy", choose_key="code")
    # resources = API.get_all_resources()
    # items = API.get_all_items()
    # items_ = API.get_items(type_=Item.Type.RESOURCE)
    # monsters = API.get_all_monster()
    # maps = API.get_all_maps()
    # craft_table = get_craft_table()
    # craftable = get_current_craftable_items()
    # craftable_effect = get_craft_table(effect="attack")
    # craftable_level = get_current_craftable_items(max_level=1)
    # craftable_skill = get_current_craftable_items(type_=Item.CraftSkill.WOODCUTTING)

    # r = API.get_character("Fushy")
    # r = API.get_characters_logs("Fushy")
    find_map = get_map_from_resource(min_level=1, max_level=1, level=20)

    # r = get_max_amount_to_craft("Yshuf", "copper")
    1
