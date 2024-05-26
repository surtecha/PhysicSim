import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Effect")

# constants
PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50 # radius of planet
OBJ_SIZE = 5
VEL_SCALE = 100

BG = pygame.transform.scale(pygame.image.load("gravitation/assets/background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("gravitation/assets/planet.png"), (PLANET_SIZE*2, PLANET_SIZE*2))

WHITE = (255, 255, 255) # rgb colour code
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):
        window.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))

class Spacecraft:
    def __init__(self, x, y, x_vel, y_vel, mass):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.mass = mass

    def move(self, planet=None):
        distance = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
        force = (G * self.mass * planet.mass) / distance ** 2

        acceleration = force/self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        acceleration_x = acceleration * math.cos(angle)
        acceleration_y = acceleration * math.sin(angle)

        self.x_vel += acceleration_x
        self.y_vel += acceleration_y

        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self):
        pygame.draw.circle(window, RED, (int(self.x), int(self.y)), OBJ_SIZE)


def create_ship(Location, mouse):
    t_x, t_y = Location
    m_x, m_y = mouse
    x_vel = (m_x - t_x) / VEL_SCALE
    y_vel = (m_y - t_y) / VEL_SCALE
    obj = Spacecraft(t_x, t_y, x_vel, y_vel, SHIP_MASS)
    return obj


def main():
    running = True
    clock = pygame.time.Clock()

    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    objects = []
    temp_obj_pos = None # stores any object that we've placed onto the screen that we've not yet launched

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    t_x, t_y = temp_obj_pos
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        window.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.line(window, WHITE, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(window, RED, temp_obj_pos, OBJ_SIZE)

        for obj in objects[:]:
            obj.draw()
            obj.move(planet)
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet.x)**2 + (obj.y - planet.y)**2) <= PLANET_SIZE
            if off_screen or collided:
                objects.remove(obj)

        planet.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()