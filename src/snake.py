import pygame

class Snake(pygame.sprite.Group):
    def __init__(self, head_texture, body_texture, tail_texture, head_index, grid):
        head = SnakeJoint(head_texture, head_index, grid)
        body = SnakeJoint(body_texture, (head_index[0] - 1, head_index[1]), grid)
        tail = SnakeJoint(tail_texture, (head_index[0] - 2, head_index[1]), grid)

        super().__init__(tail, body, head)

        self._head_texture = head_texture
        self._body_texture = body_texture
        self._tail_texture = tail_texture

        self._head_index = head_index

class SnakeJoint(pygame.sprite.Sprite):
    def __init__(self, image, index, grid):
        super().__init__()

        self.image = image
        
        center = grid[index[1]][index[0]].center
        self.rect = pygame.Rect(center[0] - image.get_size()[0] / 2, center[1] - image.get_size()[1] / 2, image.get_size()[0], image.get_size()[1])
