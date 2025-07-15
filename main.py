import pygame

def init():
    running = True
    surf = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surf.fill("purple")
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

def main():
    pygame.init()

    init()

    pygame.quit()


if __name__ == "__main__":
    main()
