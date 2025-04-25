#!/usr/bin/python3
import pygame
import pymunk
import pymunk.pygame_util
from components import ball, spring, lever

def create_ground(space):
    ground = pymunk.Segment(space.static_body, (0, HEIGHT-50), (WIDTH, HEIGHT-50), 5)
    ground.friction = 1.0
    ground.elasticity = 0.8
    space.add(ground)

def run():
    # Initialize
    pygame.init()
    WIDTH, HEIGHT = 1200, 800
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spring-Mass with Rolling Ball")
    
    space = pymunk.Space()
    space.gravity = (0, 981)
    
    # Create ground
    create_ground(space)
    
    # Create spring-mass system
    spring_body, mass = spring.create_spring(space, (600, 200), 100, 30)
    
    # Create rolling ball
    ball.create_ball(space, (200, HEIGHT-100), 30)
    
    # Create lever if needed
    # lever.create_lever(space, ...)
    
    # Simulation loop
    clock = pygame.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        window.fill((30, 30, 30))
        space.step(1/60.0)
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    run()