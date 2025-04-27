import pymunk
import pygame

class RollingBall:
    def __init__(self, space, position, radius=30):
        self.space = space
        self.radius = radius
        self.color = (65, 105, 225, 255)  # Royal blue with alpha
        
        # Physics body with moment of inertia for rolling
        mass = 10
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        
        # Shape with friction for realistic rolling
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.friction = 0.9
        self.shape.elasticity = 0.7
        self.shape.color = self.color
        
        space.add(self.body, self.shape)
    
    def draw(self, surface):
        """Custom ball drawing with proper scaling"""
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(surface, self.color[:3], pos, self.radius)  # Remove alpha for Pygame