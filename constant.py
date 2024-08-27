### ITEMS ###
from itertools import chain


class Item:
    ADVENTURER_BOOTS = 'adventurer_boots'
    ADVENTURER_HELMET = 'adventurer_helmet'
    ADVENTURER_PANTS = 'adventurer_pants'
    ADVENTURER_VEST = 'adventurer_vest'
    AIR_AND_WATER_AMULET = 'air_and_water_amulet'
    AIR_RING = 'air_ring'
    ASH_PLANK = 'ash_plank'
    ASH_WOOD = 'ash_wood'
    BANDIT_ARMOR = 'bandit_armor'
    BASS = 'bass'
    BATTLESTAFF = 'battlestaff'
    BEEF_STEW = 'beef_stew'
    BIRCH_WOOD = 'birch_wood'
    BLUE_SLIMEBALL = 'blue_slimeball'
    CHEESE = 'cheese'
    COAL = 'coal'
    COOKED_BASS = 'cooked_bass'
    COOKED_BEEF = 'cooked_beef'
    COOKED_CHICKEN = 'cooked_chicken'
    COOKED_GUDGEON = 'cooked_gudgeon'
    COOKED_SHRIMP = 'cooked_shrimp'
    COOKED_TROUT = 'cooked_trout'
    COOKED_WOLF_MEAT = 'cooked_wolf_meat'
    COPPER = 'copper'
    COPPER_ARMOR = 'copper_armor'
    COPPER_BOOTS = 'copper_boots'
    COPPER_DAGGER = 'copper_dagger'
    COPPER_HELMET = 'copper_helmet'
    COPPER_LEGS_ARMOR = 'copper_legs_armor'
    COPPER_ORE = 'copper_ore'
    COPPER_RING = 'copper_ring'
    COWHIDE = 'cowhide'
    DEAD_WOOD = 'dead_wood'
    DEAD_WOOD_PLANK = 'dead_wood_plank'
    DEATH_KNIGHT_SWORD = 'death_knight_sword'
    DEMON_HORN = 'demon_horn'
    DREADFUL_RING = 'dreadful_ring'
    DREADFUL_STAFF = 'dreadful_staff'
    EARTH_RING = 'earth_ring'
    EGG = 'egg'
    EMERALD = 'emerald'
    EMERALD_AMULET = 'emerald_amulet'
    EMERALD_RING = 'emerald_ring'
    FEATHER = 'feather'
    FEATHER_COAT = 'feather_coat'
    FIRE_AND_EARTH_AMULET = 'fire_and_earth_amulet'
    FIRE_BOW = 'fire_bow'
    FIRE_RING = 'fire_ring'
    FIRE_STAFF = 'fire_staff'
    FLYING_WING = 'flying_wing'
    FOREST_WHIP = 'forest_whip'
    FRIED_EGGS = 'fried_eggs'
    GOLD = 'gold'
    GOLD_AXE = 'gold_axe'
    GOLD_FISHING_ROD = 'gold_fishing_rod'
    GOLD_HELM = 'gold_helm'
    GOLD_MASK = 'gold_mask'
    GOLD_ORE = 'gold_ore'
    GOLD_PICKAXE = 'gold_pickaxe'
    GOLD_PLATEBODY = 'gold_platebody'
    GOLD_PLATELEGS = 'gold_platelegs'
    GOLD_RING = 'gold_ring'
    GOLD_SHIELD = 'gold_shield'
    GOLD_SWORD = 'gold_sword'
    GOLDEN_EGG = 'golden_egg'
    GOLDEN_SHRIMP = 'golden_shrimp'
    GREATER_DREADFUL_STAFF = 'greater_dreadful_staff'
    GREATER_WOODEN_STAFF = 'greater_wooden_staff'
    GREEN_SLIMEBALL = 'green_slimeball'
    GUDGEON = 'gudgeon'
    HARDWOOD_PLANK = 'hardwood_plank'
    IRON = 'iron'
    IRON_ARMOR = 'iron_armor'
    IRON_AXE = 'iron_axe'
    IRON_BOOTS = 'iron_boots'
    IRON_DAGGER = 'iron_dagger'
    IRON_HELM = 'iron_helm'
    IRON_LEGS_ARMOR = 'iron_legs_armor'
    IRON_ORE = 'iron_ore'
    IRON_PICKAXE = 'iron_pickaxe'
    IRON_RING = 'iron_ring'
    IRON_SWORD = 'iron_sword'
    JASPER_CRYSTAL = 'jasper_crystal'
    LEATHER_ARMOR = 'leather_armor'
    LEATHER_BOOTS = 'leather_boots'
    LEATHER_HAT = 'leather_hat'
    LICH_CROWN = 'lich_crown'
    LIFE_AMULET = 'life_amulet'
    LIFE_CRYSTAL = 'life_crystal'
    LIFE_RING = 'life_ring'
    LIZARD_SKIN = 'lizard_skin'
    LIZARD_SKIN_ARMOR = 'lizard_skin_armor'
    LIZARD_SKIN_LEGS_ARMOR = 'lizard_skin_legs_armor'
    LUCKY_WIZARD_HAT = 'lucky_wizard_hat'
    MAGIC_WIZARD_HAT = 'magic_wizard_hat'
    MAGICAL_CURE = 'magical_cure'
    MILK_BUCKET = 'milk_bucket'
    MULTISLIMES_SWORD = 'multislimes_sword'
    MUSHMUSH_BOW = 'mushmush_bow'
    MUSHMUSH_JACKET = 'mushmush_jacket'
    MUSHMUSH_WIZARD_HAT = 'mushmush_wizard_hat'
    MUSHROOM = 'mushroom'
    MUSHROOM_SOUP = 'mushroom_soup'
    MUSHSTAFF = 'mushstaff'
    OGRE_EYE = 'ogre_eye'
    OGRE_SKIN = 'ogre_skin'
    OWLBEAR_HAIR = 'owlbear_hair'
    PIG_SKIN = 'pig_skin'
    PIGGY_PANTS = 'piggy_pants'
    RAW_BEEF = 'raw_beef'
    RAW_CHICKEN = 'raw_chicken'
    RAW_WOLF_MEAT = 'raw_wolf_meat'
    RED_CLOTH = 'red_cloth'
    RED_SLIMEBALL = 'red_slimeball'
    RING_OF_CHANCE = 'ring_of_chance'
    RUBY = 'ruby'
    RUBY_AMULET = 'ruby_amulet'
    RUBY_RING = 'ruby_ring'
    SAPPHIRE = 'sapphire'
    SAPPHIRE_AMULET = 'sapphire_amulet'
    SAPPHIRE_RING = 'sapphire_ring'
    SERPENT_SKIN = 'serpent_skin'
    SERPENT_SKIN_ARMOR = 'serpent_skin_armor'
    SERPENT_SKIN_LEGS_ARMOR = 'serpent_skin_legs_armor'
    SHRIMP = 'shrimp'
    SKELETON_ARMOR = 'skeleton_armor'
    SKELETON_BONE = 'skeleton_bone'
    SKELETON_HELMET = 'skeleton_helmet'
    SKELETON_PANTS = 'skeleton_pants'
    SKELETON_SKULL = 'skeleton_skull'
    SKULL_RING = 'skull_ring'
    SKULL_STAFF = 'skull_staff'
    SKULL_WAND = 'skull_wand'
    SLIME_SHIELD = 'slime_shield'
    SPRUCE_FISHING_ROD = 'spruce_fishing_rod'
    SPRUCE_PLANK = 'spruce_plank'
    SPRUCE_WOOD = 'spruce_wood'
    STEEL = 'steel'
    STEEL_ARMOR = 'steel_armor'
    STEEL_AXE = 'steel_axe'
    STEEL_BOOTS = 'steel_boots'
    STEEL_HELM = 'steel_helm'
    STEEL_LEGS_ARMOR = 'steel_legs_armor'
    STEEL_RING = 'steel_ring'
    STEEL_SHIELD = 'steel_shield'
    STICKY_DAGGER = 'sticky_dagger'
    STICKY_SWORD = 'sticky_sword'
    TASKS_COIN = 'tasks_coin'
    TOPAZ = 'topaz'
    TOPAZ_AMULET = 'topaz_amulet'
    TOPAZ_RING = 'topaz_ring'
    TROMATISING_MASK = 'tromatising_mask'
    TROUT = 'trout'
    VAMPIRE_BLOOD = 'vampire_blood'
    WATER_BOW = 'water_bow'
    WATER_RING = 'water_ring'
    WOLF_BONE = 'wolf_bone'
    WOLF_HAIR = 'wolf_hair'
    WOODEN_SHIELD = 'wooden_shield'
    WOODEN_STAFF = 'wooden_staff'
    WOODEN_STICK = 'wooden_stick'
    YELLOW_SLIMEBALL = 'yellow_slimeball'

    class Type:
        AMULET = 'amulet'
        ARTIFACT = 'artifact'
        BODY_ARMOR = 'body_armor'
        BOOTS = 'boots'
        CONSUMABLE = 'consumable'
        CURRENCY = 'currency'
        HELMET = 'helmet'
        LEG_ARMOR = 'leg_armor'
        RESOURCE = 'resource'
        RING = 'ring'
        SHIELD = 'shield'
        WEAPON = 'weapon'

    class SubType:
        HELM = 'Helm'
        MASK = 'Mask'
        ALLOY = 'alloy'
        AXE = 'axe'
        BAR = 'bar'
        BOW = 'bow'
        COAT = 'coat'
        DAGGER = 'dagger'
        FISHING = 'fishing'
        FOOD = 'food'
        MINING = 'mining'
        MOB = 'mob'
        PLANK = 'plank'
        STAFF = 'staff'
        SWORD = 'sword'
        TASK = 'task'
        TOOL = 'tool'
        WAND = 'wand'
        WHIP = 'whip'
        WOODCUTTING = 'woodcutting'

    class CraftSkill:
        COOKING = 'cooking'
        GEARCRAFTING = 'gearcrafting'
        JEWELRYCRAFTING = 'jewelrycrafting'
        MINING = 'mining'
        WEAPONCRAFTING = 'weaponcrafting'
        WOODCUTTING = 'woodcutting'

    # Effects
    class Effects:
        DMG_AIR = "dmg_air"
        DMG_EARTH = "dmg_earth"
        WOODCUTTING = "woodcutting"
        FISHING = "fishing"
        BOOST_DMG_AIR = "boost_dmg_air"
        RESTORE = "restore"
        BOOST_DMG_FIRE = "boost_dmg_fire"
        RES_WATER = "res_water"
        ATTACK_FIRE = "attack_fire"
        BOOST_DMG_WATER = "boost_dmg_water"
        BOOST_HP = "boost_hp"
        BOOST_DMG_EARTH = "boost_dmg_earth"
        RES_FIRE = "res_fire"
        RES_EARTH = "res_earth"
        MINING = "mining"
        DMG_FIRE = "dmg_fire"
        ATTACK_AIR = "attack_air"
        ATTACK_WATER = "attack_water"
        RES_AIR = "res_air"
        HP = "hp"
        ATTACK_EARTH = "attack_earth"
        HASTE = "haste"
        DMG_WATER = "dmg_water"


### MONSTERS ###
class Monster:
    BANDIT_LIZARD = 'bandit_lizard'
    BLUE_SLIME = 'blue_slime'
    CHICKEN = 'chicken'
    COW = 'cow'
    DEATH_KNIGHT = 'death_knight'
    DEMON = 'demon'
    FLYING_SERPENT = 'flying_serpent'
    GREEN_SLIME = 'green_slime'
    LICH = 'lich'
    MUSHMUSH = 'mushmush'
    OGRE = 'ogre'
    OWLBEAR = 'owlbear'
    PIG = 'pig'
    RED_SLIME = 'red_slime'
    SKELETON = 'skeleton'
    VAMPIRE = 'vampire'
    WOLF = 'wolf'
    YELLOW_SLIME = 'yellow_slime'


### RESOURCES ###
class Resource:
    ASH_TREE = 'ash_tree'
    BASS_FISHING_SPOT = 'bass_fishing_spot'
    BIRCH_TREE = 'birch_tree'
    COAL_ROCKS = 'coal_rocks'
    COPPER_ROCKS = 'copper_rocks'
    DEAD_TREE = 'dead_tree'
    GOLD_ROCKS = 'gold_rocks'
    GUDGEON_FISHING_SPOT = 'gudgeon_fishing_spot'
    IRON_ROCKS = 'iron_rocks'
    SHRIMP_FISHING_SPOT = 'shrimp_fishing_spot'
    SPRUCE_TREE = 'spruce_tree'
    TROUT_FISHING_SPOT = 'trout_fishing_spot'

    class Skill:
        FISHING = 'fishing'
        MINING = 'mining'
        WOODCUTTING = 'woodcutting'

    class Drops:
        BASS = "bass"
        ASH_WOOD = "ash_wood"
        COAL = "coal"
        SPRUCE_WOOD = "spruce_wood"
        TROUT = "trout"
        IRON_ORE = "iron_ore"
        RUBY = "ruby"
        SAPPHIRE = "sapphire"
        TOPAZ = "topaz"
        GOLD_ORE = "gold_ore"
        SHRIMP = "shrimp"
        EMERALD = "emerald"
        GOLDEN_SHRIMP = "golden_shrimp"
        DEAD_WOOD = "dead_wood"
        COPPER_ORE = "copper_ore"
        BIRCH_WOOD = "birch_wood"
        GUDGEON = "gudgeon"


### MAPS ###
class Map:
    CITY = 'City'
    FOREST = 'Forest'
    FOREST_FORGE = 'Forest (Forge)'
    GRAVEYARD = 'Graveyard'
    LAKE = 'Lake'
    SPAWN = 'Spawn'

    class Position:
        COW = [(0, 2)]
        OGRE = [(-5, -5), (-5, -4)]
        GEARCRAFTING = [(3, 1)]
        RED_SLIME = [(1, -1), (2, -2)]
        LICH = [(9, 7)]
        WEAPONCRAFTING = [(2, 1)]
        YELLOW_SLIME = [(1, -2), (4, -1)]
        MONSTERS = [(1, 2)]
        BLUE_SLIME = [(0, -2), (2, -1)]
        COPPER_ROCKS = [(2, 0)]
        FLYING_SERPENT = [(5, 4), (5, 6)]
        ASH_TREE = [(-1, 0), (6, 1)]
        OWLBEAR = [(10, 1), (10, 2)]
        IRON_ROCKS = [(1, 7)]
        GOLD_ROCKS = [(10, -4)]
        GUDGEON_FISHING_SPOT = [(4, 2)]
        WOLF = [(-3, 0), (-2, 1)]
        COAL_ROCKS = [(1, 6)]
        TROUT_FISHING_SPOT = [(-2, 6)]
        MUSHMUSH = [(5, 3), (6, 4)]
        SPRUCE_TREE = [(-2, 5), (2, 6)]
        BIRCH_TREE = [(-1, 6), (3, 5)]
        JEWELRYCRAFTING = [(1, 3)]
        COOKING = [(1, 1)]
        WOODCUTTING = [(-2, -3)]
        SHRIMP_FISHING_SPOT = [(5, 2)]
        VAMPIRE = [(10, 6), (10, 8)]
        BASS_FISHING_SPOT = [(-3, 6)]
        GREEN_SLIME = [(0, -1), (3, -2)]
        BANK = [(4, 1)]
        SKELETON = [(8, 6), (8, 8)]
        PIG = [(-3, -3)]
        GRAND_EXCHANGE = [(5, 1)]
        MINING = [(1, 5)]
        DEATH_KNIGHT = [(8, 7), (10, 7)]
        DEAD_TREE = [(9, 8)]
        CHICKEN = [(0, 1)]


def print_constants(header, constants_name, constants_value=None):
    if header:
        print(header)
    if constants_value is None:
        [print(constant.upper(), "=", f"\"{constant}\"") for constant in constants_name]
    else:
        [print(constants_name[i].upper(), "=", constants_value[i]) for i in range(len(constants_value))]


if __name__ == '__main__':
    from ArtifactsAPI import ArtifactsAPI

    artifactsapi = ArtifactsAPI()
    # print_constants("### ITEMS ###\nclass Item:", list(artifactsapi.get_all_items()))
    print_constants("Effects\nclass Effect:", set(sorted(chain.from_iterable(
        [[effect["name"] for effect in v["effects"] if "name" in effect] for (k, v) in artifactsapi.get_all_items().items()]))))

    # print_constants("### RESOURCES ###class Resource:", list(artifactsapi.get_all_resources()))
    # from itertools import chain
    # print_constants("class Drops:", set(chain.from_iterable(
    #     [[drop["code"] for drop in v["drops"]] for (k, v) in artifactsapi.get_all_resources().items()])))
    # print_constants("### MAPS ###\nclass Map:", sorted({v["name"] for (k, v) in artifactsapi.get_all_maps().items()}))
    # data = [[k, v["content"]] for (k, v) in artifactsapi.get_all_maps().items() if v["content"]]
    # code_positions = {code: [coord for coord, info in data if info['code'] == code]
    #                   for code in {info['code'] for _, info in data}}
    # print_constants("class Position:", list(code_positions.keys()), list(code_positions.values()))
    1
