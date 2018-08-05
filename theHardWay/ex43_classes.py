from sys import exit


# skleton
class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Scene(object):
    def __init__(self):
        self.scenes = ['Death', 'CentralCorridor', 'LaserWeaponArmory', 'TheBridge', 'Escape']

    def enter(self):
        print "Now you are in a scene."

class Death(Scene):
    def enter(self):
        print "You die!"
        exit(0)
        # action = raw_input("> Restart or Exit: ")
        # if action == 'Restart':


class CentralCorridor(Scene):
    def enter(self):
        print "This is the staring point. And a Gothon is standing there."
        print "You have to defeat it!"


class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class Escape(Scene):
    def enter(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
