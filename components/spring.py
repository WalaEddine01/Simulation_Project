import pymunk
import math
import pygame

class SpringSystem:
    def __init__(self, space, position, rest_length=200, mass=30, stiffness=40, damping=5):
        self.space = space
        self.spring_color = (200, 200, 200, 255)
        self.mass_color = (150, 50, 50, 255)
        self.anchor_color = (100, 100, 255, 255)
        
        # Anchor point (fixed)
        self.anchor = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.anchor.position = position
        
        # Mass body (dynamic)
        self.mass = pymunk.Body()
        self.mass.position = position[0], position[1] + rest_length/2
        
        # Mass shape
        self.mass_shape = pymunk.Circle(self.mass, 20)
        self.mass_shape.mass = mass
        self.mass_shape.friction = 0.5
        self.mass_shape.color = self.mass_color
        
        # Spring constraint
        self.spring = pymunk.DampedSpring(
            self.anchor, self.mass, (0, 0), (0, 0),
            rest_length=rest_length,
            stiffness=stiffness,
            damping=damping
        )
        
        space.add(self.mass, self.mass_shape, self.spring)
    
    def draw(self, surface):
        """Draw spring with coils"""
        start_pos = self.anchor.position
        end_pos = self.mass.position
        segments = 20
        coil_radius = 15
        
        # Calculate spring points
        dir_vec = (end_pos - start_pos).normalized()
        perp_vec = pymunk.Vec2d(-dir_vec.y, dir_vec.x) * coil_radius
        length = (end_pos - start_pos).length
        coil_length = length / segments
        
        points = []
        for i in range(segments + 1):
            phase = i * math.pi * 2 * 3 / segments  # 3 full coils
            offset = perp_vec * math.sin(phase)
            point = start_pos + dir_vec * (i * coil_length) + offset
            points.append((int(point.x), int(point.y)))
        
        pygame.draw.lines(surface, self.spring_color, False, points, 2)
        pygame.draw.circle(surface, self.anchor_color, (int(start_pos.x), int(start_pos.y)), 8)
        pygame.draw.circle(surface, self.mass_color, (int(end_pos.x), int(end_pos.y)), 20)
    
    def reset(self):
        """Reset to initial position"""
        self.mass.position = self.anchor.position[0], self.anchor.position[1] + self.spring.rest_length/2
        self.mass.velocity = (0, 0)