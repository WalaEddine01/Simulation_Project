#!/usr/bin/python3
import pygame
import pymunk
import pymunk.pygame_util

# Constants
WIDTH, HEIGHT = 1200, 800
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (50, 50, 50)
GROUND_COLOR = (100, 100, 100)
GRID_SPACING = 50

class PhysicsSimulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Physics Simulation")
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        
        self.setup_debug_draw()
        self.create_environment()
    
    def setup_debug_draw(self):
        """Configure physics debug drawing"""
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.draw_options.flags = (
            pymunk.SpaceDebugDrawOptions.DRAW_SHAPES |
            pymunk.SpaceDebugDrawOptions.DRAW_CONSTRAINTS
        )
    
    def create_environment(self):
        """Create ground and walls"""
        self.ground = pymunk.Segment(
            self.space.static_body,
            (0, HEIGHT - 50),
            (WIDTH, HEIGHT - 50),
            5
        )
        self.ground.friction = 1.0
        self.ground.elasticity = 0.8
        self.space.add(self.ground)
    
    def draw_grid(self):
        """Draw background grid"""
        for x in range(0, WIDTH, GRID_SPACING):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, GRID_SPACING):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y), 1)
    
    def handle_events(self):
        """Process user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def update(self):
        """Update physics"""
        self.space.step(1/60.0)
    
    def render(self):
        """Draw everything"""
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grid()

        # Debug draw physics
        self.space.debug_draw(self.draw_options)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            pass
        pygame.quit()

if __name__ == "__main__":
    """Run the simulation"""
    simulation = PhysicsSimulation()
    while True:
        if not simulation.handle_events():
            break
        simulation.update()
        simulation.render()
        simulation.clock.tick(60)
    pygame.quit()