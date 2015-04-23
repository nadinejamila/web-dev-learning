# GAME: Gothons from Planet Percal #25 (shortened version)

from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        # loop infinitely until the game is finished
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "Your mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "A Gothon jumps out. What do you do?"

        action = raw_input("> ")

        if action == "shoot!":
            print "You are dead. He eats you."
            return 'death'
        elif action == "dodge!":
            print "Gothon stomps your head and eats you."
            return 'death'
        elif action == "tell a joke":
            print "While he's laughing you shoot him,"
            print " and you jump through the Weapon Armory door."
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You see the bomb in it's container."
        print "Enter 3 digits for the container lock to get the bomb out."
        print "Get it wrong 10 times and the lock closes forever."
        
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 1
        
        print code
        
        while guess != code and guesses < 10:
            print "BZZZEEED!"
            guess = raw_input("[keypad]> ")
            guesses += 1
            if guess =='cheat':
                break

        if guess == code or guess == 'cheat':
            print "The container opens! You head to the bridge to blow up the bomb."
            return 'the_bridge'
        else:
            print "The bomb explodes! Everyone dies."
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You encounter 5 Gothons but they're scared that you might set the bomb off."

        action = raw_input("> ")

        if action == 'throw the bomb':
            print "The bomb goes off. Everyone dies."
            return 'death'
        elif action == 'slowly place the bomb':
            print 'Gothons are trapped! You run to the escape pod.'
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "There are 5 pods. Which one do you take?"

        good_pod = randint(1, 5)

        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %d." % guess
            print "That pod is defective!"
            return 'death'
        else:
            print "You jump into the right pod."
            print "Nice escape! The planet is destroyed. You win!"
            return 'finished'


class Finished(Scene):

    def enter(self):
        print "Good job."
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# This sets the central corridor as the starting scene
a_map = Map('central_corridor')

# This sets a_map as the current scene map
a_game = Engine(a_map)

# This calls play on the game Engine
a_game.play()