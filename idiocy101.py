def event1():
    print "As you walk down the hall, still half asleep, you bump into things as you go. You try to turn on the lights, but they don't come on. As a bolt of lightning flashes out the window, you see a shadow fly across the room. Startled, you cry out. Will you\n"
    print "A: continue further to find out what it was?"
    print "B: run screaming like a lil girl into the bathroom to hide?"
    print "C: run out into the rain to look for a phone"
    answer = raw_input()

    if answer == 'A': 
        print "you follow your gut and continue down the hall. You turn into the kitchen to find Beauty, your dog, lying on the floor. She wasn't moving. You rush to her side, tears burning in your eyes... When you regain control of yourself, you look around the room for any sign of forced entry. It doesnt seem that way... You feel a cool rush of the night air on the back of you neck. You turn around and see that the window above the sink is wide open! Sheer panic and rage runs over you like a cloud. You grab a knife and work your way back to your room, cautious of every step you take, peering around every corner. You head for the closet to get the .38 special you have hidden in the back. As you open the closet door, you see someone in the mirror on the top shelf. As you turn to defend yourslef, you're struck across the temple. You hit the floor like a ton of brick, unable to see your assaillant. Before you sink into unconsiousness, you hear the distant laughter of the intruder...\n"
        event2()
    elif answer == 'B': 
        print "As you turn around to run into the bathroom like a coward, your are faced directly with what made the sound. A masked man, dressed in all black. He sees you, you see him, and as you turn to get away, he sweeps your legs out from under you, and shoots you in the head. Hiding was a bad choice. You are dead.\n"
    elif answer == 'C': 
        print "You make a run for the front door, not wanting to find out what the strange figure was. You find it locked as it was when you went to bed, but it doesn't deter you. You open the door and run out into the pouring rain. As you stand in the rain, in the middle of the steet, cloathes now soaked, you remember that you left you cell in you car. You head for it when you see a man out of the corner of you eye, staring at you from the front door. You run faster toward your Ford Escort. You open the door, jam the key in the ignition and are out of the driveway before you have a chance to close the door. As you speed down the road, a sheet of relieaf washing over you, your cell phone rings. You look at the caller ID and you don't recognize the number. You answer and a mans voice, clearly being desguised, comes over the phone. He says to head to the old wearhouse district at the end of town or he'll kill your sister, he says that you have one hour. Before you have a chance to respond, the line clicks off. You think that this man must be insane, and obviously bluffing, because you kno that your sister is in the mountains, skiing for the week. You attempt to call her cell, as it picks up, you hear the same mans voice come over the phone and says... '59 minutes, tick tock'... The line goes dead. You dont kno wat to do.\n"

def event2():
        print "You wake up with your hands and feet bound. You try to speak, but you choke on a ball gag. As you become more and more aware of your surroundings, you relize that you're actually suspended... Up-side-down!! You panic and start to struggle, frantically trying to get your hands free to remove the gag. Vomit begins to creep its way up your throught... As you fight it back, you stop moving, now more exhausted than you were before. You realize your struggle's in vain. As you listen to yourself breathing, coming in small gasps, you begin to hear the faint sound of footsteps down the hall. A giant of a man walks in.... He looked like an Italian mafia, and he was easily six foot seven and two hundred and thirty pounds, all muscle. A nervous sweat breaks out across your brow... As he removes the gag, you spit, with various colors of vomit spraying upon the clean tile floor. He looks at you in disgust.  "



print "you wake up in your room one night, startled by a noise. Do you investigate? (yes/no)"
answer = raw_input()

if answer == "yes":
    print "you stummble out of bed, you grab the rod and crop that your girlfriend left, and stalk out of the room\n"
    event1()

elif answer == "no": 
    print "you roll over and go back to sleep. THE END"

answer = raw_input()
        
