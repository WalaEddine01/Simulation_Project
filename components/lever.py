import pymunk
import pygame

class Lever:
    def __init__(self, space, pivot_pos, length=200, angle=0):
        self.space = space
        self.length = length
        self.color = (150, 150, 150, 255)  # Gray lever
        
        # Create lever body
        self.body = pymunk.Body()
        self.body.position = pivot_pos
        
        # Create lever shape (as a segment)
        self.shape = pymunk.Segment(
            self.body, 
            (0, 0), 
            (length, 0), 
            5  # Thickness
        )
        self.shape.mass = 5
        self.shape.color = self.color
        
        # Create pivot joint
        self.pivot = pymunk.PivotJoint(
            space.static_body,
            self.body,
            pivot_pos
        )
        
        # Set initial angle
        self.body.angle = angle
        
        space.add(self.body, self.shape, self.pivot)
    
    def draw(self, surface):
        """Draw the lever"""
        start_pos = self.body.local_to_world((-self.length/2, 0))
        end_pos = self.body.local_to_world((self.length/2, 0))
        pygame.draw.line(
            surface, 
            self.color[:3], 
            (int(start_pos.x), int(start_pos.y)),
            (int(end_pos.x), int(end_pos.y)), 
            5
        )
        # Draw pivot point
        pygame.draw.circle(
            surface, 
            (200, 0, 0), 
            (int(self.body.position.x), int(self.body.position.y)), 
            8
        )