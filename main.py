import pygame
import renderer

def init():
    width = 640 # Desire is to change this and make this configurable through a "Config" class that reads in a config file and parses it to find this information
    height = 480

    # Overtime add more program-level configuration stuff here
    # Return the configs as a dictionary of values

    return {
        "width": width,
        "height": height
    }


# Entrypoint to the visualizer
def run():
    pygame.init()
    configs = init()

    running = True
    clock = pygame.time.Clock()

    visualizer_renderer = renderer.Renderer(configs['width'], configs['height'], False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        visualizer_renderer.fill_screen()
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    run()
