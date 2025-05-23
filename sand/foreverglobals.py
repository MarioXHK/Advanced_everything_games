#Things that just won't change, man
illegals = ('\\','//',':','*','?','"','<','>','|')
from pygame.color import Color
from random import randint

class elementIdentity:
    def __init__(self,id: int, name: str,color: Color | None = Color(0,0,0),desc: str | None = None, otherColors: tuple[Color, ...] | None = None):
        self.id = id
        self.name = name
        self.color = color
        self.desc = desc
        self.mColors = otherColors  



elements = (
    elementIdentity(0,"Air",Color(0,0,0),"Just air."),
    elementIdentity(1,"Sand",Color(255,255,0),"Sand falls and piles on[n]top of itself."),
    elementIdentity(2,"Stone",Color(150,150,150),"Stone falls into place[n]and sits."),
    elementIdentity(3,"Water",Color(0,0,255),"Water moves to fill as[n]much space as it can."),
    elementIdentity(4,"Sugar",Color(250,250,250),"Sugar gracefully falls[n]before piling onto stuff."),
    elementIdentity(5,"Wall",Color(100,100,100), "Stays in place no[n]matter what forever."),
    elementIdentity(6,"Dirt",Color(200,100,50), "Floats on top of[n]things and turns into[n]mud when wet."),
    elementIdentity(7,"Mud",Color(150,50,10), "Good for plants."),
    elementIdentity(8,"Plant",Color(0,128,0), "Will grow into dirt[n]and mud when possible."),
    elementIdentity(9,"Lava",Color(255,25,0), "Not made of floor.[n]Is very hot and will[n]burn things."),
    elementIdentity(10,"Wet Sand",Color(200,200,50), "Sand, but it won't[n]pile onto itself."),
    elementIdentity(11,"Gravel",Color(200,200,200), "Eroded stone that will[n]now pile onto itself."), #Fun fact: This was all inspired by someone in my class suggesting that they could make stone erode. If it weren't for that suggestion, I'm not sure I'd be writing this comment here! (Since I probably would've stopped making updates after the assignment was completed since this was an assignment)
    elementIdentity(12,"Obsidian",Color(30,20,40), "Good at taking blasts,[n]can't make portals."),
    elementIdentity(13,"Steam",Color(128,200,255), "Steam from the steamed[n]clams we're having.[n]Given some time,[n]it'll turn into clouds."),
    elementIdentity(14,"Glass",Color(0,255,255), "A bit fragile, but[n]durable at the same time."),
    elementIdentity(15,"Sugar Water",Color(0,128,255), "Sugar mixed with water."),
    elementIdentity(16,"Cloud",Color(230,230,230), "Floats about for awhile[n]before turning into water."),
    elementIdentity(17,"Brick",Color(150,90,60), "structurally sound and[n]can build houses."),
    elementIdentity(18,"Moss/Algae",Color(0,128,0),"Will slowly spread[n]and take over the[n]world."),
    elementIdentity(19,"Glass Shards",Color(randint(0,50),50+randint(0,200),100+randint(0,150)),"Acts as sand since[n]it's just clearer sand[n]now."),
    elementIdentity(20,"The Sun",Color(255,255,128),"Gives the sandbox life[n]by providing plants[n]with photosynthesis and[n]a water cycle."),
    elementIdentity(21,"The Moon",Color(10,60,180), "Makes the sandbox go[n]tame by turning down[n]the temperature."),
    elementIdentity(22,"Snow",Color(240,250,255), "Falls to the ground[n]in a cute way."),
    elementIdentity(23,"Ice",Color(200,255,255), "Frozen water. It can turn[n]back into water through[n]other things."),
    elementIdentity(24,"Sugar Crystals",Color(240,220,255),"Crystalized sugar that[n]stays around in water[n]and makes america the[n]way it is."),
    elementIdentity(25,"Packed Ice",Color(100,200,230),"Stuborn ice that won't[n]melt unless under the[n]most extreme conditions."),
    elementIdentity(26,"Life Particle",Color(255,255,255),"Make sure to enable life[n]by pressing CAPS![n]Or it'll be random![n]Conway's game of life"),
    elementIdentity(27,"Sludge",Color(170,210,250),"Previously frozen water[n]stuff that's now melting[n]back into water."),
    elementIdentity(28,"Flower Seed",None,"Planting it on the[n]correct kind of ground[n]will allow this plant[n]to sprout and blossum.",(Color(40,20,10),Color(0,255,0))),
    elementIdentity(29,"Oil",Color(24,24,24),"A good source of fuel[n]in the sense fire will[n]eat away at it quickly.[n]Can't mix with water."),
    elementIdentity(30,"Fire",Color(192,255,64),"Fire will burn on anything[n]that is flammable, and will[n]continue to burn until it's[n]exhausted."),
    elementIdentity(31,"Wood",Color(140,70,30), "Made from trees.[n]Will not move at all."),
    elementIdentity(32,"Ash",Color(100,100,100),"The remains of what was[n]burnt by fire."),
    elementIdentity(33,"Cloner",Color(100,0,255),"Will clone anything that[n]makes contact with it."),
    elementIdentity(34,"Clay",Color(160,170,180),"Now renewable, can be[n]smelted into brick."),
    elementIdentity(35,"Void",Color(10,10,10),""),
    elementIdentity(36,"Petal",None,"Comes in a variety of[n]colors.",(Color(255,0,0),Color(255,255,0),Color(0,255,0),Color(0,255,255),Color(0,0,255),Color(255,0,255))),
    elementIdentity(37,"Cancer Particle",Color(randint(0,250),randint(0,100),randint(150,250)),"Make sure to enable life[n]by pressing CAPS![n]Or it'll be random![n]Something horribly wrong[n]has happened with this[n]life cell"),
    elementIdentity(38,"Iron",Color(180,180,170),"Stationary metal that[n]transmits electric signals."),
    elementIdentity(39,"Iron Sand",Color(200,200,190),"Piles onto stuff and[n]transmits electricity."),
    elementIdentity(40,"Iron Brick",Color(200,200,150),"It's not advised you[n]make a house out of[n]this brick as you'll[n]likely get electricuted."),
    elementIdentity(41,"Smart Remover",Color(100,20,240),"Removes things smartly[n]when electricity is applied."),
    elementIdentity(42,"Smart Converter",Color(200,50,50),"Converts things smartly[n]when electricity is applied."),
    elementIdentity(43,"Electricity",None,"Electrifies!",(Color(255,255,0),Color(255,255,255))),
    elementIdentity(44,"Rustish Iron",Color(180,130,100),"Iron that can't keep[n]itself stationary and[n]can't show it's signal."),
    elementIdentity(45,"Rust",Color(60,30,15),"Useless junk that's[n]not good if you're[n]considering to be alive."),
    elementIdentity(46,"Salt",Color(255,255,255),"I could make so many[n]social media jokes right[n]now."),
    elementIdentity(47,"Salt Water",Color(128,128,255),"Just like regular water,[n]but it's from the sea[n]and it can be electrified."),
    elementIdentity(48,"Salt Crystal",Color(200,230,255),"Lick"),
    elementIdentity(49,"Leaf",Color(0,150,0),"Sustains itself as[n]long as it's next to[n]something like wood[n]or else it will fall to[n]the ground."),
    elementIdentity(50,"Jammer",None,"Jams a variety of[n]things so they can't[n]work as long as the[n]jammer's out.[n]WARNING: Might burst open.",(Color(255,0,0),Color(255,255,255))),
    elementIdentity(51,"Antisand",Color(0,0,255),"Sand that floats upwards."),
    elementIdentity(52,"Antistone",Color(105,105,105),"Stone that goes up."),
    elementIdentity(53,"Antiwater",Color(255,255,0),"Water that flows up."),
    elementIdentity(54,"Identity Crisis",None,"???",(Color(255,255,0),Color(150,150,150),Color(0,0,255),Color(250,250,250),Color(100,100,100),Color(200,100,50))),
    elementIdentity(55,"Molten Salt",Color(255,200+randint(0,55),200+randint(0,55)),"So hot and salty[n]that it can't be cooled[n]down by regular means."),
    elementIdentity(56,"Smoke",Color(123,123,123),"Bad for the environment.[n]Please use the more healthy[n]kind."),
    elementIdentity(57,"Virus",(100,20+randint(-20,20)//2,240),"It'll turn everything into[n]itself."),
    elementIdentity(58,"Gold",Color(240,230,0),"Gold! It's valuable,[n]doesn't rust, and is a[n]great conductor of[n]electricity."),
    elementIdentity(59,"Covered Wire",Color(25,25,30),"More advanced electric[n]things that don't wear[n]down over time."),
    elementIdentity(60,"Strange Matter",Color(randint(0,50),randint(25,255),randint(0,50))),
    elementIdentity(61,"Shockwave",Color(192,192,192),"Blasts a wave everywhere[n]in the sandbox."),
    elementIdentity(62,"Sapling",None,"grows into a random[n]tree.",(Color(32,24,16),Color(140,70,30))),
    elementIdentity(63,"Broken Brick",Color(130,80,60),"Brick that can't be[n]used as brick anymore."),
    elementIdentity(64,"Acid Cloud",Color(170,250,190),"Corrupted clouds that will[n]make acid rain."),
    elementIdentity(65,"Acid",Color(0,255,0),"Will destroy anything it[n]touches and turn it into[n]acid sludge."),
    elementIdentity(66,"Acid Sludge",Color(randint(0,20),200+randint(0,20),randint(0,20)),"What happens when[n]acid gets to something."),
    elementIdentity(67,"Explosion",Color(randint(150,255),randint(50,230),randint(0,40)), "An explosion!"),
    elementIdentity(68,"TNT",Color(200,0,0),"Creates an explosion when[n]lit up."),
    elementIdentity(69,"C4",Color(200,180,150),"Creates an explosion when[n]electrified."),
    elementIdentity(70,"Nuke",Color(80,100,60),"No."),
    elementIdentity(71,"Holy Water",Color(200,200,255),"Can be used for a[n]variety of things like[n]saving the sandbox from[n]climate change or even[n]reviving dead plants and[n]all sorts of stuff!"),
    elementIdentity(72,"Dead Plant",Color(120,60,10),"Plants that have died."),
    elementIdentity(73,"Coal",Color(20,20,20),"Very old plants[n]that have been crushed[n]into a very bad (in[n]terms of climate change)[n]thing."),
    elementIdentity(74,"Natural Gas",Color(60,30,15),"Smells like burning[n]water."),
    elementIdentity(75,"Polluted Water",Color(0,randint(100,200),randint(30,100)),"When your water can't[n]take it anymore, it turns[n]into polluted water and[n]isn't good for anyone."),
    elementIdentity(76,"Greenhouse Sun",(255,150,120),"The sun but evil because[n]there's too many greenhouse[n]gases in the atmosphere."),
    elementIdentity(77,"Wax",Color(200,150,60),"Great stuff for waxing[n]things with. Turns more[n]liquid the hotter it gets."),
    elementIdentity(78,"Honeycomb",Color(230,200,70),"Wax molded to hold honey[n]and bees."),
    elementIdentity(79,"Honey",Color(160,100,23),"A delicious treat[n]for hard working bees[n]and you~"),
    elementIdentity(80,"Bee",Color(230,230,100),"One of the only truly living[n]things in this world,[n]these basic bees just[n]fly around, build onto[n]their hives and reproduce."),
    elementIdentity(81,"Blood",Color(255,0,0),"Still warm."),
    elementIdentity(82,"Red Sand",Color(200,128,0),"Where does it come[n]from? We may never know,[n]but it does behave like[n]stone half the time and[n]sand the other half,[n]which is interesting."),
    elementIdentity(83,"Good Smoke (Fog maybe)",Color(160,160,160),"Healthy smoke."),
    elementIdentity(84,"Acid Waste",Color(randint(0,10),150+randint(0,60),randint(0,10)),"Sometimes acid sludge[n]leaves behind acid waste[n]which isn't very good."),
    elementIdentity(85,"Sticky Water",Color(40,60,255),"Water but sticky."),
    elementIdentity(86,"Filler",Color(100,0,240),"Will fill any space[n]it's placed in."),
    elementIdentity(87,"Snake",Color(0,128,0),"I love Voxelbox"),
    elementIdentity(88,"Tesla Coil",Color(200,200,0),"Makes Electricity (the[n]element) from current"),
    elementIdentity(89,"Battery",Color(50,50,50),"When the morning's gone,[n]And you can't go on![n]Delivers pulses of[n]electricity."),
    elementIdentity(90,"Thunder Cloud",Color(128,128,128),"Floats in a less calm[n]way than it's... how do[n]I say this in the least[n]racist way possible?[n]Probably not like that.[n]It shoots lightning at[n]random points and can[n]give more water than[n]their non-thunder versions."),
    elementIdentity(91,"Pollen",Color(255,230,128),"Can make things go bloom."),
    elementIdentity(92,"Flower bud",Color(0,64,0),"The actual flower[n]part of the flower.[n]Will either require time[n]and sunlight or pollen[n]for it to bloom."),
    elementIdentity(93,"Feather",Color(235,235,235),"will slowly float down[n]in the air unless[n]something's in the way."),
    elementIdentity(94,"Chicken",Color(230,230,230),"Welcome to the alive[n]club, chicken! A simple[n]thing that moves around[n]on the ground and[n]floats down softly."),
    elementIdentity(95,"Molten Glass",Color(127,255,255),"At last, molten glass[n]is much better at[n]being glass. If only it[n]wasn't so hot and[n]liquidy."),
    elementIdentity(96,"Molten Sugar",Color(255,255,128),"The heart of[n]cookie clicker"),
    elementIdentity(97,"Molten Cheese",Color(230,230,0),"A wonderful thing."),
    elementIdentity(98,"Primordeal Ooze",Color(200,0,0),"All life in the[n]sandbox canotically came[n]from this stuff."),
    elementIdentity(99,"Firework",None,"Celebrate this moment!",(Color(255,0,0),Color(255,255,0),Color(0,255,0),Color(0,255,255),Color(0,0,255),Color(255,0,255))),
    elementIdentity(100,"Player",Color(0,230,230),"It's you."),
    elementIdentity(101,"Frosted Sand",Color(220,250,230),"Sand that acts more[n]like stone than sand."),
    elementIdentity(102,"Static",None,"Randomized Static noise,[n](Cai's favorite!)",(Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)),Color(randint(0,255),randint(0,255),randint(0,255)))),
    elementIdentity(103,"TV Static",Color(128,128,128),"It's static that's[n]much more watery.")
)

#These are just gui colors, they don't 100% predict what the element will look like

crashSplash = (
        "OH F### THIS WASN'T SUPPOSED TO HAPPEN!\nGOODBYE CRUEL WORLD!!!",
        "That's not very healthy!",
        "Well, you tried!",
        "Try using a graph next time.",
        "The sandbox didn't say it's sandboxing time.",
        "Your rot has brained.",
        "DEATH AND DESTRUCTION!!!!",
        "Oh good heavens!",
        "Oh e-gods! My sandbox is ruined!",
        "Why??????????????????????????????????????",
        "HOW?! I DID EVERYTHING RIGHT!",
        "Oh well.",
        "Poo",
        "Huston, we have a problem",
        "Have you tried turning it off and on again?",
        "Ok, what 5th grader touched this?",
        "Lemme guess: Elementary school student?",
        "Funnel.",
        "Unfunny",
        "This isn't such a cash money of you.",
        "NOOOOOOOOOOOOOOOO!!!!!!!!!!!!",
        "HELP! HELP!!!",
        "The house is on fire!",
        "You set the fire alarm off!",
        "It's not you, it's me.",
        "I thought you said extra fries",
        "Hey I heard you liked your sand splattered.",
        "Backups are here to save your day (I hope)",
        "Lemme try to explain",
        ":(",
        "=(",
        ":o",
        ":O",
        "This crash is sponsered by Raid Shadow Legends!",
        "I knew I should've gone for the graph project...",
        "Brazil!",
        "Brazilian Coffee moment.",
        "Unpog",
        "Fish in the meantime.",
        "Text me this problem later.",
        "Remind me in like 256 hours.",
        "I believe a rat ate one of my wires.",
        "Remember to ride the cyclone!",
        "Your lucky number is 13.",
        "How dare me!",
        "How did my physics break now?",
        "1x1 sandbox!",
        "Is this a reference?",
        "Where is the funny?",
        "That's not supposed to happen.",
        "Weeeee- OH NO!!!",
        "I'm on fire!",
        "Bruising our brushes.",
        "I believe this requires an explanation...\nHopefully this one is good for you.",
        "I got stickbugged.",
        "A RICKROLL!",
        "Better call saul.",
        "I told you, you should've played Minceraft.",
        "CMOS battery missing!",
        "Several Migraines later.",
        "One more headache to deal with",
        "Another one bites the dust.",
        "foreverglobals.py failed to load this message",
        "Error: crashSplash not defined! Instead we'll show you the real error.",
        "Aaaaaaaaaaaaand it's gone.",
        ">:(",
        ":/",
        ":\\",
        "N",
        "WRONG LEVER!!!",
        "I bet you weren't expecting this.",
        "Hey, it's me, the console talking since the program pooped itself.",
        "Alright, who invited adult swim to code this?",
        "Antihumor",
        "Unmemable",
        "SUPER MARIO BROS X GO TRY IT!!!",
        "I double checked it, why isn't it working?",
        "Erm, what the blast?",
        "I put a period instead of a comma...",
        "...",
        "NOT FEELING UP TO IT RIGHT NOW SORRY!!!",
        "OW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
        "OWEY! OUCH, YEOUCH!",
        "YEEEEEOOWWWW!!!",
        "That hurt!",
        "It burns!",
        "This isn't so Supercalifragilisticexpialidocious of you",
        "Dociousaliexpiesticfragicalirupes",
        "Dociousaliexpilisticfragicalirupes",
        "There you go, yelling out the U word!",
        "I knew ya needed me!",
        "Lmao bang!",
        "It's been some time, hasn't it?"
    )




yeses = ("y","yes","yeah","do it","sure","alright","ok","ig","i guess","yay","pull the lever, cronk!","pull the lever, cronk","alrighty then","whatever","heck yes","hell yes","probably","ye","yea","yeah!","oh yes","i don't see why not","i dont see why not","the opposite of no","yep","yes sir","yessir","please do","do","1","i'd love to","i'd love to try it out","let's see what you've got","let's-a go!","lets a go","let's a go","lets a go!","mushroom kingdom here we come","may","smash","yeah, sure","yesure","let's kick bubblegum","activate","throttle","upgrade","proceed","bb","shure","surry boi","surry","yes please","yes maam","yes hoobaab","what could go wrong","what could possibly go wrong")
noes = ("n","no","nah","nay","nein","it's opposite day","don't you dare","poop","do not","do not the cat","perish","hell no","heck no","probably not","jumpscare","no!","no!!","no!!!","mmm...","how could you screw it up this badly?","the opposite of yes","nope","not even close","please don't","don't","0","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","unrun","kill","oh no","ho ho ho ho no","steamed hams","nada","nay","pass","t_t","i'm sick rn","not today","chewing bubblegum","deactivate","turn back","i said turn back","snowgrave","die","di","noooooooooo","b","lmao nah","nada","zilch","q","no please","no thank you","no thanks")




splashes = (
    "Let's-a go!",
    "Time to begin your creative journey!",
    "Also try Sandboxels!",
    "Also try Sandspiel!",
    "Please don't make an upside-down T",
    "Brains!",
    "Now with 30% more sand!",
    "Heh, I'm doing a Minecraft thing",
    "Console splash jumpscare!",
    "Mustard or mayo?\nNeither are here but I'm just asking in general.",
    "I'm waisting time doing this when I should be doing graphs!",
    "It's finally!",
    "It's good for your heart!",
    "Eating lava since 50",
    "Release the holy water!",
    "Without a doubt, it was gravel!",
    "Antisand without water?",
    "Now (not) playing: Wet sand!",
    "At least it's not an epilectic hell!\n(Yet)",
    "Randomatt!",
    "It's filled with randomness!",
    "Now with more files!",
    "At least 10 lines of code!",
    "if you.pos == \"Here\": cake.give(you)",
    "Oceans of oil!",
    "There's not a good chance it's your birthday",
    "Happy not april fools!",
    "Other programing languages? Never!",
    "Not porting to anything else, fight me.",
    "Without a doubt one of the projects of all time!",
    "At last, it's perfect!",
    "Also try Purrgatory!",
    "Also try Minecraft!",
    "Also try Stardew Valley!",
    "Also try Roblox!",
    "Also try Super Mario Bros X!",
    "Also try Terraria!",
    "Also try modding games!",
    "Also try touching some grass!",
    "It's about damn time!",
    "Is there a brush right for you?",
    "We have the elements for you!",
    "Meets basic requirements!",
    "HELP",
    "You pulled the lever!",
    "Dun dun dunn!",
    "How anti-annoying!",
    "Flashbang!",
    "Yahoo!",
    "Wahoo!",
    "This is totally a gaming moment in gaming history!",
    "Did you know there are at least 2 elements here?",
    "Not a missing assignment!",
    "Let's do this!",
    "Made with Migranes!",
    "Also try that good cookie clicker clone!",
    "Also try Block Story!",
    "In a Nutshell!",
    "Breathe!",
    "Remember to breathe!",
    "You are now breathing manually!",
    "Free!",
    "Runs in Python!",
    "Uses Pygame!",
    "Python ftw!",
    "You can't do this in other coding languages!\n(Don't quote me on that)",
    "Oh, I almost forgot!",
    "Piracy....is a complicated subject!",
    "Support your communities!",
    "Share your creations!",
    "Share your world!",
    "Share your sandbox!",
    "Save and load work!",
    "Load others work!",
    "Watch others projects!",
    "See what others have done with this sandbox!",
    "See what others have made!",
    "I wonder what others have done!",
    "sandsaves confirmed!!",
    "Sandbox confirmed!!",
    "Ohmagad, popscartch!",
    "Ohmehgerd!",
    "Do the harlem shake!",
    "Bitten with butts!",
    "Hacks!",
    "Nah I'd win",
    "We good!",
    "It's all fine!",
    "Everything's Ok!",
    "It's all working!",
    "Let's get started!",
    "Here you come!",
    "It's time to sand!",
    "Not object oriented!",
    "Function oriented!",
    "Oriental Avenue!",
    "Yay!",
    ":)",
    "SUPER MARIO BROS X GO TRY IT!!!",
    "I double checked, should be good!",
    "Whoops, all air!",
    "You could say this is a console game in a way.",
    "Made in Colorado!",
    "Made in Denver!",
    "Made at CEC!",
    "Made with love!",
    "Please don't fill up the screen with TNT!",
    "Unlikely to have dragons!",
    "Graze the roof!",
    "There's a sandbox on your lawn!",
    "When it rains sand, it pours sand!",
    "Now including Mud! (You can't eat it)",
    "Opening the door to a whole new world!",
    "What will we do today?",
    "This is the story of a sandbox named whatever you want to call it",
    "Mouse input!",
    "Keyboard input!",
    "More than just a console game!",
    "This is text, so is this a text based game?",
    "Question mark!",
    "When the morning's gone and you can't go on!",
    "Better than Overwatch! (Not really)",
    "Let's play this lil simulation!",
    "Press Start, Player 2!",
    "Ready, Player 1!",
    "Insert Coin, Player 3!",
    "Player 4!",
    "It burns!",
    "Blood and Honey!",
    "Supercalifragilisticexpialidocious!",
    "Guess you didn't need me after all...",
    "Now with GUIs!",
    "Guess the tutorial!",
    "The game of life!",
    "Run you fool, I hunger!",
    "I don't get what's the big deal about gex and saying it.",
    "Lists, selection, iteration, programming!",
    "No cats.... yet.",
    "Nom nom nom!"
)

titleScreenSandbox=[
    #0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5
    #                    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#0
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#2
    [0,0,0,0,0,0,4,4,4,4,0,0,0,0,4,4,0,0,0,4,4,0,0,4,4,0,4,4,4,4,4,0,0,4,4,4,4,4,0,0,0,4,4,4,4,0,0,4,4,0,0,4,4,0,0,0,0,0,0,0],#3
    [0,0,0,0,0,4,4,0,0,0,0,0,0,4,4,4,4,0,0,4,4,4,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,0,4,4,4,4,0,0,0,0,0,0,0,0],#4
    [0,0,0,0,0,0,4,4,4,4,0,0,0,4,4,4,4,0,0,4,4,4,4,4,4,0,4,4,0,0,4,4,0,4,4,4,4,4,0,0,4,4,0,0,4,4,0,0,0,4,4,0,0,0,0,0,0,0,0,0],#5
    [0,0,0,0,0,0,0,0,0,4,4,0,4,4,4,4,4,4,0,4,4,0,4,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,0,4,4,4,4,0,0,0,0,0,0,0,0],#6
    [0,0,0,0,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,0,0,0,0,0,0],#7
    [0,0,0,0,0,0,4,4,4,4,0,0,4,4,0,0,4,4,0,4,4,0,0,4,4,0,4,4,4,4,4,0,0,4,4,4,4,4,0,0,0,4,4,4,4,0,0,4,4,0,0,4,4,0,0,0,0,0,0,0],#8
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9
    [4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4],#10
    [4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4],#11
    [4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4],#12
    [4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4],#13
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#14
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#16
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#17
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#18
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#19
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#20
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#21
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#22
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#23
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#24
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#25
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#26
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#27
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#28
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#29
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#30
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#31
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#32
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#33
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#34
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#35
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#36
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#37
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#38
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#39
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#40
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#41
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#42
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#43
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#44
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#45
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#46
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#47
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#48
    [0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],#49
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#50
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#51
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#52
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#53
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#54
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#55
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#56
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#57
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#58
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#59-This is so tedious
]

print("This is getting global...")