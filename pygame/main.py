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
    #maps
    LEVEL1 = [
    "wwwwwwwwwwwwwwww",
    "w..............w",
    "w..............w",
    "w..............w",
    "w..............w",
    "w..............w",
    "w..............w",
    "w..............w",
    "w..............w",
    "wwwwwwwwwwwwwwww" 
    ]
    # important
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Trillium starter")
    clock = pygame.time.Clock()
    px, py, = WIDTH // 2, HEIGHT // 2
    speed = 2.5
    #movement must be divisible by speed
    tx, ty = px, py
    running = True
    movement = 40
    hitlist = [(px,py)]
    while running:
        #input phase
        for event in pygame.event.get():
            if len(hitlist) == 0:
                hitlist.append ((px,py))
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
        # math phase
        if tx != px:
            if tx > px:
                px += speed
            else:
                px -= speed
        if ty != py:
            if ty > py:
                py += speed
            else:
                py -= speed
        if len(hitlist) == 0:
            hitlist.append((px,py))
        else:
            (tx,ty) = hitlist[0] 
            if (px,py) == hitlist[0]:
                hitlist.pop(0) 

        #output phase
        screen.fill((24, 28, 36))
        for y in range(10):
               for x in range(16):
                   current_cell = LEVEL1[y][x]
                   if current_cell == "w":
                       pygame.draw.rect(screen,(12,12,12),pygame.Rect((x*40,y*40),(40,40)))
                   elif current_cell == ".":
                       # code for drawing an empty space at x*40, y*40 (pixel position)
                       print("hi")
       
        pygame.draw.circle(screen, (120, 200, 160), (px, py), 18)
        pygame.draw.circle(screen, (200, 0, 0), (tx, ty), 2)
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)  # hands control to the browser once per frame
    pygame.quit()


asyncio.run(crashscreen.guard(main))