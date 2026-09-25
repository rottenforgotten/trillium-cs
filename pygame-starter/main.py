"""A tiny Pygame game that also runs in the browser.

Run it in the browser (this is the normal way in a codespace):
    pygbag --port 3000 pygame-starter
then open the forwarded port 3000 when the notification appears.

The only rule for browser-friendly Pygame: the game loop is `async` and
calls `await asyncio.sleep(0)` once per frame. Everything else is ordinary
Pygame. On a real desktop the same file runs with `python main.py`.
"""
import asyncio
import pygame

WIDTH, HEIGHT = 640, 400


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Trillium starter")
    clock = pygame.time.Clock()
    x, y, speed = WIDTH // 1.8, HEIGHT // 1.8, 40
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            DI = "horizontal"
            movement = "negitive"
        elif keys[pygame.K_RIGHT]:
            DI = "horizontal"
            movement = "positive"
        elif keys[pygame.K_UP]:
            DI = "vertical"
            movement = "positive"
        elif keys[pygame.K_DOWN]:
            DI = "vertical"
            movement = "negitive"
        PML = 0
        while PML >= 20:
            if DI == "vertical":
                if movement == "negitive":
                    y -= speed
                else:
                    y += speed
            else:
                if movement == "negitive":
                    x -= speed
                else:
                    x += speed
            PML += 1
            screen.fill((24, 28, 36))
            pygame.draw.circle(screen, (120, 200, 160), (x, y), 24)
            pygame.display.flip()
            clock.tick(60)
            await asyncio.sleep(0)  # hands control to the browser once per frame

    pygame.quit()


asyncio.run(main())
