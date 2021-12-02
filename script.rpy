# The script of the game goes in this file.

# Declare characters used by this game. In this case just the teacher.

define e = Character("Ms Eileen")

# Declare the chalk board font styling for easy reuse.
define chalk_style = {
    "font":"chalk.ttf", # A chalky font
    "color":"#fbf7f5aa", # A chalky color
    "size":66, # Nice, readable size
    }

# Define custom positions.
transform board_tl: # Board Top Left
    # alings are from 0.0 to 1.0. 0 is left/top and 1 right/bottom of screen.
    xalign 0.2
    yalign 0.15

transform board_tc: #Board Top Center
    xalign 0.5
    yalign 0.15

# The game starts here.

label start:

    # Show the classroom background. "scene" clears all displayed items
    # and starts fresh.
    scene bg room

    # Let's turn on some music.
    play music "sunflower-slow-drag.ogg" fadein 3

    # Define and show a text image. We give it the chalk_style to make it seem
    # like it is written on the board.
    image msg = Text("Welcome!", **chalk_style)
    show msg at truecenter

    # Shows the picture "images/eileen happy.png". The Ren'Py knows to look
    # for this pattern of character tags if we name our files properly.
    show eileen happy

    # This is dialogue. We defined the character "e" as Ms Eileen earlier.
    # leaving off the character definition allows text to show without a speaker
    # name as if it were plain narration or internal monologue. Dialoge
    # statements also stop the interpreter until you click or advance the text.
    e "Hello and Welcome to our virtual Classroom. Click, Press Space, or Enter
    to advance the to the next line."

    # Let's move eileen so the user can see the chalk board.
    show eileen vhappy at right
    with move

    e "Pretty neat, isn't it?"

    # We can change eileen's expression (or position) without restating what has
    # already been stated. All transformations to an image are persistant until
    # overwriten.
    show eileen happy

    # You can break up lines that are too long.
    # Text wrap happens in game not here
    e "Today we are just going to demonstrate
        what this classroom might be like."

    # Remove the welcome from the board. Hidden objects no longer exist.
    hide msg

    # Get the rainbow image from images folder and define an image object.
    image rainbow = Image("rainbow.png")

    # Show our new image slightly transparent so it fits with the chalk board.
    # The colors are way too bright otherwise and don't fit the scene.
    show rainbow behind eileen at truecenter:
        alpha 0.67

    # Another text image.
    image title_colors = Text("Lesson 1: Colors", **chalk_style)

    show title_colors behind eileen at board_tc

    e "The first thing we will learn is about basic colors."

    # Defining a unicode character and size to be filled in with a color.
    # The braced tags work very much like html tags do. ex. {b} is Bold.
    define fill_sq = "{size=66}\u25aa{/size}"

    label red_quiz:
        # Reset eileen to happy. This is only for the case if the user answers
        # incorrectly.
        show eileen happy

        # These images Thisare boxes. The hex code is fill color and if size isn't
        # specified, it fills the whole screen.
        image red = Solid("#f00", xysize=(200,200))
        image blue = Solid("#00f", xysize=(200,200))
        image yellow = Solid("#ff0", xysize=(200,200))

        # Menus give the user choices to make in the game. Good for quizes.
        menu:
            # Ms Eileen asks the question that the user has to answer.
            # Luckily it is multiple choice because its a hard question.
            e "Which one is RED?"

            # These are the options. Only the block below the choice the user
            # makes runs.

            # Red Square
            "{color=f00}[fill_sq]{/color}":
                show eileen vhappy
                show red at truecenter
                e "That one is red! Good Job!"
                hide red

            # Blue Square
            "{color=00f}{size=66}[fill_sq]{/size}{/color}":
                show eileen concerned
                show blue at truecenter
                e "This one is actually Blue."
                hide blue
                jump red_quiz

            # Yellow Square
            "{color=ff0}{size=66}[fill_sq]{/size}{/color}":
                show eileen concerned
                show yellow at truecenter
                e "This one is actually Yellow."
                hide yellow
                jump red_quiz

    # Now we are back in the root (start) label of the script.
    show eileen happy
    e "Colors are interesting things! Just wait until you're old enough to
    learn about wavelengths of light and how colors really work."

    show eileen vhappy
    e "{b}So Cool!{/b}" #Bolded text

    # Return at base level ends the game.
    return
