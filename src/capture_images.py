import tomllib

# Import settings
with open("../../config.toml", "rb") as f:
    config = tomllib.load(f)

# for faction in config['countries']:
#     for country in faction:
#         if not os.path.isdir(f"../images/{faction}/{country}"):
#             os.makedirs(f"../images/{faction}/{country}")
#         for unit_type in ['LOG', 'SUP', "TNK", "VHC", "HEL", 'AIR']:
            
                
# btw impliment naval support down the line
# Also make sure people realize inf doesn't work