############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
 
    # not related to self, all shared (applies to every melon)
    # ex) type = fruit
    
    
    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        # self.pairings = [mint, strawberry, etc etc]
        # Muskmelon = MelonType() 
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color 
        self.is_seedless = is_seedless 
        self.is_bestseller = is_bestseller 
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)
        
        # self.pairings = []
        # pairing = mint / strawberries & mint / ice cream / prosciutto 
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code 


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # order is: self, code, first_harvest, color, is_seedless, is_bestseller, name

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    cas = MelonType("cas", 2003, "orange", True, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)
    
    cren = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)
    
    yw = MelonType("YW", 2013, "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types

melon_types_woo = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # melon type code = melon_type_woo[1]
    # expected output YW: Yellow Watermelon
    # for loop -> for YW not in melon_type_dict 
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:  
            print(f"-{pairing}")
print_pairing_info(melon_types_woo)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_type_dict = {}
    for melon in melon_types:
        if melon.code not in melon_type_dict:
            melon_type_dict[melon.code] = melon
    
    
    # melon_type_dict[key] = "Melon Type"
    # >>> (output) -> melon_type_dict { YW: "Yellow Watermelon"}
    # return a dictionary whose keys are reporting codes, values are melon type for that code
    return melon_type_dict

print_pairing_info(melon_types_woo)


############
# Part 2   #
############


class Melon():
    """A melon in a melon harvest."""
    
    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape, color, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    # expected output:
    #Melon 1
    # Melon type: yw
    # Shape rating: 8
    # Color rating: 7
    # Harvested from Field 2
    # Harvested by Sheila
    
    def is_sellable(self):
        """Should return True or False if Melon is sellable"""
        # Melon is able to be sold if its shape and color ratings are > 5
        # and didn't come from field 3
        if self.shape > 5 and self.color > 5 and self.harvested_from != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # order: self, melon_type, shape, color, harvested_from, harvested_by
    melons_by_id = make_melon_type_lookup(melon_types)
    
    # from lab hint:
    # melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    
    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"],3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 10, 7, 3, "Sheila")

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]
    # return a list
    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        harvester = f"Harvested by {melon.harvested_by}"
        field_num = f"Field #{melon.field}"
        status = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE"
        print(f"{harvester} from {field_num} {status}")


