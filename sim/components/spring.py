import pymunk

def create_spring(space, pos, length=100, mass=30):
    # Create static anchor point
    anchor = pymunk.Body(body_type=pymunk.Body.STATIC)
    anchor.position = pos
    
    # Create mass body
    mass_body = pymunk.Body()
    mass_body.position = (pos.x, pos.y + length)
    shape = pymunk.Circle(mass_body, 10)
    shape.mass = mass
    shape.friction = 0.7
    
    # Create spring between anchor and mass
    spring = pymunk.DampedSpring(
        anchor, mass_body, (0, 0), (0, 0),
        rest_length=length, stiffness=50, damping=10)
    
    space.add(mass_body, shape, spring)
    return mass_body