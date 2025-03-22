# Declare characters used by this game. The color argument colorizes the
# name of the character.
label characters:
    define Inase = Character("Inase", color="#42e3f5")

# Sets a transform to ensure all sprites are a consistent size.
transform inaseTransform:
    xzoom 0.60
    yzoom 0.60

# Organizes all the sprites with their assigned image and uniform transform.
label inaseSprites:
    image inase default = At("inase default.png", inaseTransform)
    image inase talking = At("inase talking.png", inaseTransform)
    image inase annoyed = At("inase annoyed.png", inaseTransform)
    image inase frustrated = At("inase frustrated.png", inaseTransform)
    image inase nervous = At("inase nervous.png", inaseTransform)