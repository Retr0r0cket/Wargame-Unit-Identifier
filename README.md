# Wargame Unit Identifier
Wargame Unit Identifier is a tensorflow powered machine learning model designed to differentiate between unit types when optics cannot confirm the unit type in Wargame: Red Dragon. 

## How it works
- Filters all units by faction (redfor or blufor)
- Based on image, attempts to classify unit
    - If unit variants have enough differences, will classify
    - If unit variants are too similar, will not classify. Will present list of possible options
- Will then filter results by nations known to be/not be in the match

## License
While the license for the project hasn't been determined yet, it will most likely be either GNU-GPL 3.0 or later or the MPL-2.0, but probably the GNU GPL. 
#### Free and open source software FTW am I right?

## Releases:
Releases will contain the following elements:
- The entire source code (duh, but images for training included too)
    - Also will be provided without images
- Model testing script only
- Pretrained models

## Contributing
- #### TL;DR contributions appreciated
- If you can train a more accurate model than me with the same images, please share it that would be fantastic.
- If you want to make any changes to the model training scheme, that's fine as long as it results in higher accuracy.
- If you want to change the image capture, test, and verification scripts, that's fine as long as they support the same features and have genuine benefits.
- I am not changing this repository to use another enviorment/package management solution for python. I've considered poetry and there is a slim change I might do it, but don't push me on it.
- If you want to add images to the training dataset, please do so to the images/all-images directory only

## Notes
- This was not designed for use of the infantry tab (too hard to differentiate), the naval tab (will be added down the line due to ships being rather distinct), or the air tab (because that's just impractical for the user).
- This also was not designed for Wargame: Airland Battle and definitley not Wargame: European Escalation, but could easily be modified into working for those. That will probably be a future project.
- #### This is probably cheating so don't use this in any multiplayer matches. This is more of a proof of concept than a tool you should play with. The game is designed for you not to be sure what something is sometimes. Just get better recon or blow it up.
    - "But Retr0r0cket why are you making this if it's cheating?" Because I thought it was a cool idea that I'd worked on previously to a limited extent (not without visual confirmation of unit type though) and because I don't give a shit if it's cheating.
- I might use tauri and Tensorflow.js to make this a desktop app in the future.
- Could potentially be integrated with some deckcode software to automatically assess best units you have to counter said unit OR to further enhance accuracy of unit guesses
- If you're wondering why I'm doing development in docker, it's because setting up tensorflow on WSL is a pain and it's just so much easier. You don't have to, but that's how I'm doing it. I'll hopefully publish the image later