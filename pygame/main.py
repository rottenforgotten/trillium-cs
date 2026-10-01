"""A tiny Pygame game that also runs in the browser.

Run it in the browser (this is the normal way in a codespace):
    pygbag --port 3000 pygame
then open the forwarded port 3000 when the notification appears.

The only rule for browser-friendly Pygame: the game loop is `async` and
calls `await asyncio.sleep(0)` once per frame. Everything else is ordinary
Pygame. On a real desktop the same file runs with `python main.py`.
"""
import asyncio
import pygame
import crashscreen  # shows errors on the game screen and in the terminal

WIDTH, HEIGHT = 640, 400


async def main():
    pygame.init()
    
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Trillium starter")
    clock = pygame.time.Clock()
    x, y, = WIDTH // 2, HEIGHT // 2
    speed = 2
    #movement must be divisible by speed
    tx, ty = x, y
    running = True
    movement = 40
    hitlist = [(x,y)]
    while running:
        #input phase
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hitlist.append((hitlist[-1][0] - movement, hitlist[-1][1]))
                elif event.key == pygame.K_RIGHT:
                    hitlist.append((hitlist[-1][0] + movement, hitlist[-1][1]))
                elif event.key == pygame.K_UP:
                    hitlist.append((hitlist[-1][0], hitlist[-1][1] - movement))
                elif event.key == pygame.K_DOWN:
                    hitlist.append((hitlist[-1][0], hitlist[-1][1] + movement))
        print("input done")
        # math phase
        if len(hitlist) == 0:
            tx,ty = x,y
        else:
            (tx,ty) = hitlist[0]
        if tx != x:
            if tx > x:
                x += speed
            else:
                x -= speed
        if ty != y:
            if ty > y:
                y -= speed
            else:
                y += speed
                if (x,y) == hitlist[0]:
                    hitlist.pop(0)
                    print("aignfxyur")
        print("math done")
        #output phase
        screen.fill((24, 28, 36))
        pygame.draw.circle(screen, (120, 200, 160), (x, y), 18)
        pygame.draw.circle(screen, (200, 0, 0), (tx, ty), 2)
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)  # hands control to the browser once per frame
    print("output done")
    pygame.quit()


asyncio.run(crashscreen.guard(main))
