from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = [int(b) for b in input().split(" ")]
locks = deque([int(l) for l in input().split(" ")])
intelligence = int(input())
bullets_in_gun = gun_barrel
out_of_bullets = False

while locks:
    shot = bullets.pop()
    bullets_in_gun -= 1
    intelligence -= bullet_price
    if locks[0] >= shot:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if bullets:
        if bullets_in_gun < 1:
            bullets_in_gun += gun_barrel
            print("Reloading!")
    else:
        out_of_bullets = True
        break

if out_of_bullets and locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")