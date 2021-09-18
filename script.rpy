# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Moreno")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.




    show  char1
             #Naro character
    # These display lines of dialogue.
    scene bg0
    show char1
    e "Bonjour a tous  perkenalan  nama gua Moreno Royyansyah Adhikusuma"
    e "Angkatan eternals  kelas X Mipa 5 "
    e "gua lahir di bandung 19 september 2005"


    with dissolve

    scene bg3
    show char1
    e "Selama pandemi ini gua suka  menghabiskan waktu main game yang berjudul squad "
    e "jadi di game  ini genre nya milsim atau military simulation, mirip mirip battlefield"
    e "tapi lebih realistic. gua suka main game ini karna pace nya yang lambat."

    with dissolve

    scene bg4
    show char1
    e "kalo makanan  gua paling suka kue red velvet karna paduan rasa kue sama cream cheese nya yang enak . "
    with dissolve
    show char1
    scene bg5
    show char1
    e "kalo minuman  nya gua suka  minum teh manis karna cara bikin  nya yang simple dan bisa buat obat ajaib kalo lu pingsan pas upacara  "
    with dissolve
    show char1
    e "itu aja perkenalan dari gua makasih untuk perhatian nya see u next time comrades"



    # This ends the game.

    return
