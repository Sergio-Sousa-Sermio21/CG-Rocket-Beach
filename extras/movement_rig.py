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
        self.x_rotate = list()
        self.x_rotating = 0
        self.x_rotate_limit = list()
        self.y_move = list()
        self.y_moving = 0
        self.y_move_limit = list()
        self.y_rotate = list()
        self.y_rotating = 0
        self.y_rotate_limit = list()
        self.z_move = list()
        self.z_moving = 0
        self.z_move_limit = list()
        self.z_rotate = list()
        self.z_rotating = 0
        self.z_rotate_limit = list()

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)

    def remove(self, child):
        self._look_attachment.remove(child)

    def move(self, dist, time_seconds):

        self.x_move.append(dist[0])
        self.x_move_limit.append(int(time_seconds * 60))

        self.y_move.append(dist[1])
        self.y_move_limit.append(int(time_seconds * 60))

        self.z_move.append(dist[2])
        self.z_move_limit.append(int(time_seconds * 60))

    def rotate(self, angle, time_seconds):

        self.x_rotate.append(math.radians(angle[0]))
        self.x_rotate_limit.append(int(time_seconds * 60))

        self.y_rotate.append(math.radians(angle[1]))
        self.y_rotate_limit.append(int(time_seconds * 60))

        self.z_rotate.append(math.radians(angle[2]))
        self.z_rotate_limit.append(int(time_seconds * 60))

    def clear(self):
        self.x_move.clear()
        self.x_move_limit.clear()
        self.x_rotate.clear()
        self.x_rotate_limit.clear()
        self.x_moving = 0
        self.x_rotating = 0
        self.y_move.clear()
        self.y_move_limit.clear()
        self.y_rotate.clear()
        self.y_rotate_limit.clear()
        self.y_moving = 0
        self.y_rotating = 0
        self.z_move.clear()
        self.z_move_limit.clear()
        self.z_rotate.clear()
        self.z_rotate_limit.clear()
        self.z_moving = 0
        self.z_rotating = 0

    def update(self, input_object, delta_time):
        if len(self.x_move) > 0:
            if self.x_move[0] != 0:
                if self.x_move_limit[0] >= 1:
                    self.translate(self.x_move[0] / self.x_move_limit[0], 0, 0, local=False)
                else:
                    self.translate(self.x_move[0], 0, 0, local=False)
            self.x_moving += 1
            if self.x_moving >= self.x_move_limit[0]:
                self.x_move.pop(0)
                self.x_move_limit.pop(0)
                self.x_moving = 0

        if len(self.y_move) > 0:
            if self.y_move[0] != 0:
                if self.y_move_limit[0] >= 1:
                    self.translate(0, self.y_move[0] / self.y_move_limit[0], 0, local=False)
                else:
                    self.translate(0, self.y_move[0], 0, local=False)
            self.y_moving += 1
            if self.y_moving >= self.y_move_limit[0]:
                self.y_move.pop(0)
                self.y_move_limit.pop(0)
                self.y_moving = 0

        if len(self.z_move) > 0:
            if self.z_move[0] != 0:
                if self.z_move_limit[0] >= 1:
                    self.translate(0, 0, self.z_move[0] / self.z_move_limit[0], local=False)
                else:
                    self.translate(0, 0, self.z_move[0], local=False)
            self.z_moving += 1
            if self.z_moving >= self.z_move_limit[0]:
                self.z_move.pop(0)
                self.z_move_limit.pop(0)
                self.z_moving = 0

        if len(self.x_rotate) > 0:
            if self.x_rotate[0] != 0:
                if self.x_rotate_limit[0] >= 1:
                    self.rotate_x(self.x_rotate[0] / self.x_rotate_limit[0], local=True)
                else:
                    self.rotate_x(self.x_rotate[0], local=True)
            self.x_rotating += 1
            if self.x_rotating >= self.x_rotate_limit[0]:
                self.x_rotate.pop(0)
                self.x_rotate_limit.pop(0)
                self.x_rotating = 0

        if len(self.y_rotate) > 0:
            if self.y_rotate[0] != 0:
                if self.y_rotate_limit[0] >= 1:
                    self.rotate_y(self.y_rotate[0] / self.y_rotate_limit[0], local=True)
                else:
                    self.rotate_y(self.y_rotate[0], local=True)
            self.y_rotating += 1
            if self.y_rotating >= self.y_rotate_limit[0]:
                self.y_rotate.pop(0)
                self.y_rotate_limit.pop(0)
                self.y_rotating = 0

        if len(self.z_rotate) > 0:
            if self.z_rotate[0] != 0:
                if self.z_rotate_limit[0] >= 1:
                    self.rotate_z(self.z_rotate[0] / self.z_rotate_limit[0], local=True)
                else:
                    self.rotate_z(self.z_rotate[0], local=True)
            self.z_rotating += 1
            if self.z_rotating >= self.z_rotate_limit[0]:
                self.z_rotate.pop(0)
                self.z_rotate_limit.pop(0)
                self.z_rotating = 0
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
