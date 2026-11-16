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
    map = [
    "wwwwwwwwwwwwwwww",
    "w..............w",
    "w..............w",
    "w.........w....w",
    "w......b.......w",
    "w..............w",
    "w...w..........w",
    "w..............w",
    "w..............w",
    "wwwwwwwwwwwwwwww" 
    ]
    # important
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    boxlist = []
    for y in range(10):
        for x in range(16):
            current_cell = map[y][x]
            if current_cell == "b":
                boxlist.append((x,y))
    pygame.display.set_caption("Trillium starter")
    clock = pygame.time.Clock()
    px, py, = 8.5,8.5
    speed = 2.5/40
    #movement must be divisible by speed
    tx, ty = px, py
    running = True
    movement = 1
    hitlist = [(px,py)]
    while running:
        #input phase
        for event in pygame.event.get():
            if len(hitlist) == 0:
                hitlist.append ((px,py))
            if event.type == pygame.QUIT:
                running = False    
            thingy=(hitlist[-1][1])
            gizmo=(hitlist[-1][0])
            if event.type == pygame.KEYDOWN:
                if event.key==(pygame.K_LEFT or pygame.K_A)and (map[int(thingy)][int(gizmo-movement)])!="w":
                    hitlist.append((gizmo-movement,thingy))                               
                elif event.key==(pygame.K_RIGHT or pygame.K_D)and (map[int(thingy)][int(gizmo+movement)])!="w":
                    hitlist.append((gizmo+movement,thingy))
                elif event.key==(pygame.K_UP or pygame.K_W)and (map[int(thingy-movement)][int(gizmo)])!="w":
                    hitlist.append((gizmo,thingy-movement))
                elif event.key==(pygame.K_DOWN or pygame.K_S) and (map[int(thingy+movement)][int(gizmo)])!= "w":
                    hitlist.append((gizmo,thingy+movement))
        # math phase
        bcy=(ty-0.5)
        bcx=(tx-0.5)
        bcyi=int(bcy)
        bcxi=int(bcx)
        if tx != px:
            if tx > px:      
                if (bcx,bcy) in boxlist:
                    boxlist[boxlist.index[bcyi,bcxi]] = (bcy,bcx+speed)
                px += speed       
            elif tx < px:
                if (bcx,bcy) in boxlist:
                    boxlist[boxlist.index(bcxi,bcyi)] = (bcx-speed,bcy)
                px -= speed
        elif ty != py:
            if ty > py:
                if (bcx,bcy) in boxlist:
                    boxlist[boxlist.index(bcxi,bcyi)] = (bcx,bcy+speed)
                py += speed
            elif ty < py:     
                if (bcx,bcy) in boxlist:
                    boxlist[boxlist.index(bcxi,bcyi)] = (bcx,bcy-speed)
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
                current_cell = map[y][x]
                if current_cell == "w":
                    pygame.draw.rect(screen,(0,150,200),pygame.Rect((x*40,y*40),(40,40)))
                elif current_cell == ".":
                    # code for drawing an empty space at x*40, y*40 (pixel position)
                    pygame.draw.rect(screen,(0,200,50),pygame.Rect((x*40,y*40),(40,40)))
        for box in boxlist:
            pygame.draw.rect(screen,(200,200,0),pygame.Rect((box[0]*40,box[1]*40),(40,40)))
            print(box[0])
            print(box[1])
        pygame.draw.circle(screen, (170, 100, 0), (px*40, py*40), 18)
        pygame.draw.circle(screen, (200, 0, 0), (tx*40, ty*40), 2)
        pygame.display.flip()
        
        clock.tick(60)
        await asyncio.sleep(0)  # hands control to the browser once per frame
    pygame.quit()
asyncio.run(crashscreen.guard(main))