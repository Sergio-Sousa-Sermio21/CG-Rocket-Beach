import math

from core_ext.object3d import Object3D


class MovementRig(Object3D):
    """
    Add moving forwards and backwards, left and right, up and down (all local translations),
    as well as turning left and right, and looking up and down
    """
    def __init__(self, units_per_second=1, degrees_per_second=60):
        # Initialize base Object3D.
        # Controls movement and turn left/right.
        super().__init__()
        # Initialize attached Object3D; controls look up/down
        self._look_attachment = Object3D()
        self.children_list = [self._look_attachment]
        self._look_attachment.parent = self
        # Control rate of movement
        self._units_per_second = units_per_second
        self._degrees_per_second = degrees_per_second
        self.x_move = list()
        self.x_moving = 0
        self.x_move_limit = list()
        self.y_move = list()
        self.y_moving = 0
        self.y_move_limit = list()
        self.z_move = list()
        self.z_moving = 0
        self.z_move_limit = list()

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)

    def remove(self, child):
        self._look_attachment.remove(child)

    def move(self, coordinate, dist, time_seconds):
        if coordinate == 0:
            self.x_move.append(dist)
            self.x_move_limit.append(int(time_seconds*60))
        if coordinate == 1:
            self.y_move.append(dist)
            self.y_move_limit.append(int(time_seconds*60))
        if coordinate == 2:
            self.z_move.append(dist)
            self.z_move_limit.append(int(time_seconds*60))

    def update(self, input_object, delta_time):
        if len(self.x_move) > 0:
            if self.x_move[0] > 0:
                if self.x_move_limit[0] > 0:
                    self.translate(self.x_move[0]/self.x_move_limit[0], 0, 0)
                else:
                    self.translate(self.x_move[0], 0, 0)
            self.x_moving += 1
            if self.x_moving >= self.x_move_limit[0]:
                self.x_move.pop(0)
                self.x_move_limit.pop(0)
                self.x_moving = 0

        if len(self.y_move) > 0:
            if self.y_move[0] > 0:
                if self.y_move_limit[0] > 0:
                    self.translate(0, self.y_move[0]/self.y_move_limit[0], 0)
                else:
                    self.translate(0, self.y_move[0], 0)
            self.y_moving += 1
            if self.y_moving >= self.y_move_limit[0]:
                self.y_move.pop(0)
                self.y_move_limit.pop(0)
                self.y_moving = 0

        if len(self.z_move) > 0:
            if self.z_move[0] > 0:
                if self.z_move_limit[0] > 0:
                    self.translate(0, 0, self.z_move[0]/self.z_move_limit[0])
                else:
                    self.translate(0, 0, self.z_move[0])
            self.z_moving += 1
            if self.z_moving >= self.z_move_limit[0]:
                self.z_move.pop(0)
                self.z_move_limit.pop(0)
                self.z_moving = 0

        """
        move_amount = self._units_per_second * delta_time
        rotate_amount = self._degrees_per_second * (math.pi / 180) * delta_time
        if input_object.is_key_pressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -move_amount)
        if input_object.is_key_pressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, move_amount)
        if input_object.is_key_pressed(self.KEY_MOVE_LEFT):
            self.translate(-move_amount, 0, 0)
        if input_object.is_key_pressed(self.KEY_MOVE_RIGHT):
            self.translate(move_amount, 0, 0)
        if input_object.is_key_pressed(self.KEY_MOVE_UP):
            self.translate(0, move_amount, 0)
        if input_object.is_key_pressed(self.KEY_MOVE_DOWN):
            self.translate(0, -move_amount, 0)
        if input_object.is_key_pressed(self.KEY_TURN_RIGHT):
            self.rotate_y(-rotate_amount)
        if input_object.is_key_pressed(self.KEY_TURN_LEFT):
            self.rotate_y(rotate_amount)
        if input_object.is_key_pressed(self.KEY_LOOK_UP):
            self._look_attachment.rotate_x(rotate_amount)
        if input_object.is_key_pressed(self.KEY_LOOK_DOWN):
            self._look_attachment.rotate_x(-rotate_amount)
        """

