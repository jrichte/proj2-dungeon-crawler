## Class concepts

# Player class
init to handle starting hp and inventory
Stores position - index in our map grid ['x','y'], inventory, manages movement
Stats - HP (if hit 0, game ends)
Inventory list - text file containing item names/data
item csv containing names/properties - player object only stores id numbers
lots of basic items, rare cool items with relatively manageable exceptions
inventory system to popout larger images of items (fun auxilary system)

# Map class
__layout (list of lists, each element is an object related to tile/room type)
__init__ takes in x, y for size, generates empty map
PopulateMap() randomly fills in map with rooms, ensures continuity
Stores map composition, state of gates(?), manages map generation
Would storing position here make more sense than a player class?
Classes for tile types?
set up logic for tracking where we've been (minimap populates as you enter rooms)
Room object contains room type, isVisted

# Enemy superclass
Stores general variables for enemies (direction needed to dodge/hit, maybe position if they're pre-loaded traps instead of random encounters?) and have testing logic
Subclasses that initialize directions