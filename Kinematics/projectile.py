import math
import random
import pygame

def main():
    pygame.init()
    SCREEN = WIDTH, HEIGHT = 1500, 700

    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h

    if width >= height:
        win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
    else:
        win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    FPS = 60

    BLACK = (18, 18, 18)
    WHITE = (217, 217, 217)
    RED = (252, 91, 122)
    GREEN = (29, 161, 16)
    BLUE = (78, 193, 246)
    ORANGE = (252,76,2)
    YELLOW = (254,221,0)
    PURPLE = (155,38,182)
    AQUA = (0,249,182)

    COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE]

    font = pygame.font.SysFont('verdana', 12)

    origin = (20, 340)
    radius = 250

    g = 9.8

    def toRadian(theta):
        return theta * math.pi / 180

    def toDegrees(theta):
        return theta * 180 / math.pi

    def getGradient(p1, p2):
        if p1[0] == p2[0]:
            m = toRadian(90)
        else:
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        return m

    def getAngleFromGradient(gradient):
        return math.atan(gradient)

    def getAngle(pos, origin):
        m = getGradient(pos, origin)
        thetaRad = getAngleFromGradient(m)
        theta = round(toDegrees(thetaRad), 2)
        return theta

    def getPosOnCircumeference(theta, origin):
        theta = toRadian(theta)
        x = origin[0] + radius * math.cos(theta)
        y = origin[1] + radius * math.sin(theta)
        return (x, y)

    class Projectile(pygame.sprite.Sprite):
        def __init__(self, u, theta):
            super(Projectile, self).__init__()

            self.u = u
            self.theta = toRadian(abs(theta))
            self.x, self.y = origin
            self.color = random.choice(COLORS)

            self.ch = 0
            self.dx = 2

            self.f = self.getTrajectory()
            self.range = self.x + abs(self.getRange())

            self.path = []

        def timeOfFlight(self):
            return round((2 * self.u * math.sin(self.theta)) / g, 2)

        def getRange(self):
            range_ = ((self.u ** 2) * 2 * math.sin(self.theta) * math.cos(self.theta)) / g
            return round(range_, 2)

        def getMaxHeight(self):
            h = ((self.u ** 2) * (math.sin(self.theta)) ** 2) / (2 * g)
            return round(h, 2)

        def getTrajectory(self):
            return round(g /  (2 * (self.u ** 2) * (math.cos(self.theta) ** 2)), 4)

        def getProjectilePos(self, x):
            return x * math.tan(self.theta) - self.f * x ** 2

        def update(self):
            if self.x >= self.range:
                self.dx = 0
            self.x += self.dx
            self.ch = self.getProjectilePos(self.x - origin[0])

            self.path.append((self.x, self.y-abs(self.ch)))
            self.path = self.path[-50:]

            pygame.draw.circle(win, self.color, self.path[-1], 5)
            pygame.draw.circle(win, WHITE, self.path[-1], 5, 1)
            for pos in self.path[:-1:5]:
                pygame.draw.circle(win, WHITE, pos, 1)

    projectile_group = pygame.sprite.Group()

    clicked = False
    currentp = None

    theta = -30
    end = getPosOnCircumeference(theta, origin)
    arct = toRadian(theta)
    arcrect = pygame.Rect(origin[0]-30, origin[1]-30, 60, 60)

    # Function to draw text input
    def draw_text_input(win, font, text, x, y):
        text_surface = font.render(text, True, WHITE)
        win.blit(text_surface, (x, y))

    # Function to get user input for initial velocity
    def get_user_velocity():
        velocity_input = ''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            velocity = float(velocity_input)
                            return velocity
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    elif event.key == pygame.K_BACKSPACE:
                        velocity_input = velocity_input[:-1]
                    else:
                        velocity_input += event.unicode
            win.fill(BLACK)
            draw_text_input(win, font, "Enter initial velocity (m/s): " + velocity_input, 20, 20)
            pygame.display.update()
            clock.tick(FPS)

    # Get user input for initial velocity
    u = get_user_velocity()

    running = True
    while running:
        win.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_r:
                    projectile_group.empty()
                    currentp = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False

                pos = event.pos
                theta = getAngle(pos, origin)
                if -90 < theta <= 0:
                    projectile = Projectile(u, theta)
                    projectile_group.add(projectile)
                    currentp = projectile

            if event.type == pygame.MOUSEMOTION:
                if clicked:
                    pos = event.pos
                    theta = getAngle(pos, origin)
                    if -90 < theta <= 0:
                        end = getPosOnCircumeference(theta, origin)
                        arct = toRadian(theta)

        pygame.draw.line(win, WHITE, origin, (origin[0] + 1400, origin[1]), 2)
        pygame.draw.line(win, WHITE, origin, (origin[0], origin[1] - 250), 2)
        pygame.draw.line(win, AQUA, origin, end, 2)
        pygame.draw.circle(win, WHITE, origin, 3)
        pygame.draw.arc(win, AQUA, arcrect, 0, -arct, 2)

        projectile_group.update()

        # Info *******************************************************************
        title = font.render("PROJECTILE MOTION", True, WHITE)
        fpstext = font.render(f"FPS : {int(clock.get_fps())}", True, WHITE)
        thetatext = font.render(f"Angle : {int(abs(theta))}", True, WHITE)
        degreetext = font.render(f"{int(abs(theta))}°", True, YELLOW)
        win.blit(title, (700, 30))
        win.blit(fpstext, (20, 400))
        win.blit(thetatext, (20, 420))
        win.blit(degreetext, (origin[0]+38, origin[1]-20))

        if currentp:
            veltext = font.render(f"Velocity : {currentp.u}m/s", True, WHITE)
            timetext = font.render(f"Time : {currentp.timeOfFlight()}s", True, WHITE)
            rangetext = font.render(f"Range : {currentp.getRange()}m", True, WHITE)
            heighttext = font.render(f"Max Height : {currentp.getMaxHeight()}m", True, WHITE)
            win.blit(veltext, (WIDTH-250, 400))
            win.blit(timetext, (WIDTH-250, 420))
            win.blit(rangetext, (WIDTH-250, 440))
            win.blit(heighttext, (WIDTH-250, 460))

        pygame.draw.rect(win, (0,0,0), (0, 0, WIDTH, HEIGHT), 5)
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
