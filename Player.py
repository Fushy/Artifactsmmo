from time import sleep

from ArtifactsAPI import API, get_amount_recipe_to_craft, get_inventory, get_inventory_sum, get_max_amount_to_craft, wait_cooldown_from_result, get_current_craftable_items
from swagger_client.rest import ApiException
from Threads import run
from swagger_client import CharacterSchema
from constant import *


# noinspection PyUnboundLocalVariable
class Player:
    def __init__(self, name: str, working_position: tuple[int, int], max_inventory_quantity=None, depose_items: list[str] = None,
                 data=None):
        self.name: str = name
        self.working_position: tuple[int, int] = working_position
        self.depose_items: list[str] = depose_items
        if data is None:
            self.data: CharacterSchema = API.get_character(name)
        self.max_inventory_quantity: int = max_inventory_quantity
        if max_inventory_quantity is None:
            # noinspection PyTypeChecker
            self.max_inventory_quantity = self.data.inventory_max_items
        self.inventory: dict[str, int] = get_inventory(self.data.inventory)
        self.type, self.code = API.get_map(working_position).content.values()
        if self.type == "resource":
            f = API.get_resource
        elif self.type == "monster":
            f = API.get_monster
        map_element = f(self.code)
        self.drops, self.level = map_element.drops, map_element.level
        try:
            self.action = map_element.skill
            if self.action == "fishing":
                self.skill = "cooking"
            else:
                self.skill = self.action
            self.skill_level = getattr(self.data, self.skill + "_level")
        except:
            self.action = self.skill = self.skill_level = None
        # for drop in drops:
        #     code = drop["code"]
        #     item = API.get_item(code)
        self.lock = False

    def wait_if_cooldown(self):
        return wait_cooldown_from_result(self.data)

    def get_inventory(self):
        # self.inventory = get_inventory(V["characters"][self.name]["data"].inventory)
        self.inventory = get_inventory(self.data.inventory)
        return self.inventory

    def get_inventory_available_slots(self) -> int:
        # noinspection PyTypeChecker
        return self.max_inventory_quantity - get_inventory_sum(self.inventory)

    def is_max_inventory_quantity(self) -> bool:
        return self.get_inventory_available_slots() <= 0

    def deposit_all_items(self, except_items=None):
        self.move_to_bank_if_not_pos()
        self.update_data(API.bank_deposit_all_items(self.name, self.inventory, except_items=except_items))

    def get_position(self):
        return self.data.x, self.data.y

    def is_at_position(self, pos):
        return self.get_position() == pos

    def is_working_position(self):
        return self.is_at_position(self.working_position)

    def is_new_task_position(self):
        return self.is_at_position((1, 2))

    def move_to_if_not_pos(self, pos):
        if not self.is_at_position(pos):
            self.update_data(API.move(self.name, *pos))

    def move_to_working_if_not_pos(self):
        self.move_to_if_not_pos(self.working_position)

    def move_to_newtask_if_not_pos(self):
        self.move_to_if_not_pos((1, 2))

    def move_to_bank_if_not_pos(self):
        self.move_to_if_not_pos((4, 1))

    def move_to_craft_weapon_if_not_pos(self):
        self.move_to_if_not_pos((2, 1))

    def move_to_craft_gear_if_not_pos(self):
        self.move_to_if_not_pos((3, 1))

    def move_to_craft_jewel_if_not_pos(self):
        self.move_to_if_not_pos((1, 3))

    def move_to_craft_cook_if_not_pos(self):
        self.move_to_if_not_pos((1, 1))

    def move_to_craft_mine_if_not_pos(self):
        self.move_to_if_not_pos((1, 5))

    def move_to_craft_wood_if_not_pos(self):
        self.move_to_if_not_pos((-2, -3))

    def move_to_correct_craft_if_not_pos(self, code, skill=None):
        if skill is None:
            skill = API.get_item(code).item["craft"]["skill"]
        if skill == Item.CraftSkill.MINING:
            self.move_to_craft_mine_if_not_pos()
        if skill == Item.CraftSkill.WOODCUTTING:
            self.move_to_craft_wood_if_not_pos()
        if skill == Item.CraftSkill.COOKING:
            self.move_to_craft_cook_if_not_pos()
        if skill == Item.CraftSkill.GEARCRAFTING:
            self.move_to_craft_gear_if_not_pos()
        if skill == Item.CraftSkill.WEAPONCRAFTING:
            self.move_to_craft_weapon_if_not_pos()
        if skill == Item.CraftSkill.JEWELRYCRAFTING:
            self.move_to_craft_jewel_if_not_pos()

    def craft(self, code, quantity, skill=None):
        self.move_to_correct_craft_if_not_pos(code, skill)
        self.update_data(API.craft(self.name, code, quantity))

    def gather(self):
        self.move_to_working_if_not_pos()
        self.update_data(API.gather_resource(self.name))

    def fight(self):
        self.move_to_working_if_not_pos()
        self.update_data(API.fight(self.name))

    def update_data(self, data: CharacterSchema):
        self.data = data
        if self.data is None:
            self.data = API.get_character(self.name)
            return False
        self.inventory = get_inventory(self.data.inventory)
        self.wait_if_cooldown()

    def work(self):
        if self.lock:
            return
        self.lock = True
        self.wait_if_cooldown()
        if self.is_max_inventory_quantity():
            # if True:
            if self.skill_level:
                for code, item_info in get_current_craftable_items(skill=self.skill, max_level=self.skill_level).items():
                    self.craft_item(code, max_=True)
            self.deposit_all_items()
        if self.name == "Fushy":
            self.fight()
        else:
            self.gather()
        self.lock = False

    def get_new_task(self):
        return self.update_data(API.get_new_task(self.name))

    def get_from_bank(self, code, quantity, bank=None):
        if not API.is_in_bank(code, quantity, bank=bank):
            return False
        self.move_to_bank_if_not_pos()
        # Il se peut qu'à ce moment les items aient été pris
        try:
            result = API.get_from_bank(self.name, code, quantity)
        except ApiException:
            return False
        self.update_data(result)

    def craft_item(self, code, quantity=1, inventory=None, bank=None, max_=False):
        craftable_items = get_current_craftable_items()
        if code not in craftable_items:
            return False
        if inventory is None:
            inventory = self.get_inventory()
        if bank is None:
            bank = API.get_bank_items()
        bank = dict(bank)
        to_get_in_inventory = {}
        skill = craftable_items[code]["skill"]
        max_doable = craftable_items[code]["quantity"]
        recheck = False
        if max_:
            max_doable_inventory = get_max_amount_to_craft(self.name, code, self.max_inventory_quantity)
            # amount_recipe = get_amount_recipe_to_craft(code)
            if max_doable_inventory < max_doable:
                recheck = True
        for recipe_info in craftable_items[code]["recipes"]:
            recipe_item, amount_recipe, doable_quantity = (recipe_info["code"], recipe_info["quantity"],
                                                           recipe_info["doable_quantity"])
            if max_:
                quantity = min(max_doable_inventory, doable_quantity)
            in_bank = 0 if recipe_item not in bank else bank[recipe_item]
            in_inventory = 0 if recipe_item not in inventory else inventory[recipe_item]
            if in_inventory + in_bank >= amount_recipe * quantity:
                amount_to_pick, amount_to_craft = max(0, amount_recipe * quantity - in_inventory), 0
            else:
                amount_to_pick, amount_to_craft = in_bank, amount_recipe * quantity - in_bank - in_inventory
            if amount_to_pick > self.get_inventory_available_slots():
                self.deposit_all_items(except_items=[recipe["code"] for recipe in craftable_items[code]["recipes"]])
            quantity = (in_inventory + amount_to_pick) // amount_recipe
            if recipe_item in bank:
                bank[recipe_item] -= amount_to_pick
            to_get_in_inventory[recipe_item] = amount_to_pick, amount_to_craft
        for recipe_item, (amount_to_pick, _) in to_get_in_inventory.items():
            if amount_to_pick:
                if not self.get_from_bank(recipe_item, amount_to_pick):
                    return False
        for recipe_item, (_, amount_to_craft) in to_get_in_inventory.items():
            if amount_to_craft > 0:
                bank = API.get_bank_items()  # todo use V
                if recipe_item != code:
                    self.craft_item(recipe_item, amount_to_craft, inventory, bank)
            if self.craft(code, quantity, skill) == 478:
                return False
        if recheck:
            self.craft_item(code, amount_to_craft, inventory, bank, max_)
        return True

    # def deposit_items(self):
    #     return API.bank_deposit_all_items(self.name, self.inventory)

    # def gather(self):


if __name__ == '__main__':
    workers = [
        Player("Fushy", (0, 1)),
        # Player("Fushy", (1, -1)),
        Player("Yshuf", (2, 6)),
        Player("Shufy", (7, 12)),
        Player("Hysfu", (1, 7)),
        Player("Uyshf", (1, 7)),
    ]
    while True:
        for player in workers:
            if not player.lock:
                # player.work()
                run(player.work)
            sleep(0.1)

    # fushy = Player("Fushy", (0, 1))
    yshuf = Player("Yshuf", (-1, 0))
    # fushy.get_from_bank("ash_wood", 10)
    # fushy.deposit_all_items()
    # fushy.craft_item("copper_dagger")
    # fushy.craft_item("copper_dagger")
    # yshuf.craft_item('copper')
    yshuf.craft_item('ash_plank', max_=True)
