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
    x, y, speed = WIDTH // 2, HEIGHT // 2, 2
    tx, ty = x, y
    running = True
#for DI 0 is horizontal 1 is vertical
    movement = 40
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and (tx, ty) == (x, y):
                if event.key == pygame.K_LEFT:
                    tx -= movement
                elif event.key == pygame.K_RIGHT:
                    tx += movement
                elif event.key == pygame.K_UP:
                    ty += movement
                elif event.key == pygame.K_DOWN:
                    ty -= movement
            
            
            screen.fill((24, 28, 36))
            pygame.draw.circle(screen, (120, 200, 160), (x, y), 18)
            pygame.draw.circle(screen, (200, 0, 0), (tx, ty), 2)
            pygame.display.flip()
            clock.tick(60)
            await asyncio.sleep(0)  # hands control to the browser once per frame
    pygame.quit()


asyncio.run(main())
