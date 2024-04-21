clothes_in_box = [int(i) for i in input().split(" ")]
rack_capacity = int(input())
cnt = 1
rack = rack_capacity

while clothes_in_box:
    if rack < clothes_in_box[-1]:
        cnt += 1
        rack = rack_capacity
    else:
        rack -= clothes_in_box.pop()

print(cnt)