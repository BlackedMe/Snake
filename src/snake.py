import pygame
from collections import deque

class Snake(pygame.sprite.Group):
    def __init__(self, turn_texture, head_texture, body_texture, tail_texture, head_index, grid):
        head = SnakeJoint(head_texture, head_index, grid)
        body = SnakeJoint(body_texture, (head_index[0] - 1, head_index[1]), grid)
        tail = SnakeJoint(tail_texture, (head_index[0] - 2, head_index[1]), grid)

        super().__init__(tail, body, head)

        self._turn_texture = turn_texture
        self._head_texture = head_texture
        self._body_texture = body_texture
        self._tail_texture = tail_texture

        self._head_index = pygame.Vector2(head_index)
        self._tail_index = pygame.Vector2(head_index[0] - 2, head_index[1])

        self.uturns = deque()

        self._front = pygame.math.Vector2(1, 0)

    # take rightwards as positive
    def rotate(self, dir, grid):
        angle = -90 * dir

        # Rotate the head and move it forward by one grid
        _back = -self._front
        self._front = self._front.rotate(-angle) # angle is negated because of pygame's inverted y coordinate system
        self._head_index += self._front

        self._head_texture = pygame.transform.rotate(self._head_texture, angle)
        self.add(SnakeJoint(self._head_texture, self._head_index, grid))
        
        # Rotate the body
        self._body_texture = pygame.transform.rotate(self._body_texture, angle)

        # Store the position of the u-turn and perform a u-turn
        self.uturns.append((self.sprites()[-2].rect.center, angle))

        self.sprites()[2].image = pygame.transform.rotate(self._turn_texture, self._get_uturn_angle(_back, self._front))

        # Move the tail forward by one grid
        self.remove(self.sprites()[0])

        if self.sprites()[0].rect.center == self.uturns[0][0]:
            self.uturns.popleft()
            self._tail_texture = pygame.transform.rotate(self._tail_texture, angle)

        self.sprites()[0].image = self._tail_texture
    
    def move_forward(self, grid):
        # Move the head forward by one grid
        self._head_index += self._front
        self.add(SnakeJoint(self._head_texture, self._head_index, grid))

        # Replace the old head with its body
        self.sprites()[-2].image = self._body_texture

        # Move the tail forward by one grid
        self.remove(self.sprites()[0])

        if len(self.uturns) > 0 and self.sprites()[0].rect.center == self.uturns[0][0]:
            self._tail_texture = pygame.transform.rotate(self._tail_texture, self.uturns[0][1])
            self.uturns.popleft()

        self.sprites()[0].image = self._tail_texture

    def _get_uturn_angle(self, back, front):
        vec2 = back + front

        if vec2.y == -1:
            return -45 * vec2.x - 45 * vec2.y

        return 45 * vec2.x + 225 * vec2.y
        
class SnakeJoint(pygame.sprite.Sprite):
    def __init__(self, image, index, grid):
        super().__init__()

        self.image = image
        
        center = grid[int(index[1])][int(index[0])].center
        self.rect = pygame.Rect(center[0] - image.get_size()[0] / 2, center[1] - image.get_size()[1] / 2, image.get_size()[0], image.get_size()[1])
