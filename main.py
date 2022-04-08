from resources import *
from sys import exit


def draw():
    def draw_triangle():
        for point in MAIN_POINTS:
            pygame.draw.circle(WIN, BLACK, point, 1)

    def draw_midpoint():
        p1 = choice(MAIN_POINTS)
        p2 = midpoints[-1]
        midpoints.append(midpoint(p1, p2))

    WIN.fill(WHITE)
    draw_triangle()
    for pt in midpoints:
        pygame.draw.circle(WIN, BLACK, pt, 1)
    draw_midpoint()
    pygame.display.update()


def pause():
    while True:
        CLOCK.tick(FPS)
        # pygame.display.update()
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_SPACE:
                    return
            if evt.type == pygame.QUIT:
                pygame.quit()
                exit()


def main():
    running = True
    while running:
        CLOCK.tick(FPS)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()
    exit()


if __name__ == '__main__':
    main()
