import pymunk

def create_ball(space, pos, radius=30, mass=10):
    body = pymunk.Body()
    body.position = pos
    
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.friction = 0.9
    shape.elasticity = 0.8
    
    space.add(body, shape)
    return body