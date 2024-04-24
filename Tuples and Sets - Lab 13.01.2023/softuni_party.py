number_of_guests = int(input())
guests = input()
all_guests = []

while guests != "END":
    all_guests.append(guests)
    guests = input()

invited = set(all_guests[:number_of_guests])
arrived = set(all_guests[number_of_guests:])

guests_did_not_came = invited.difference(arrived)

print(f"{len(guests_did_not_came)}")
print('\n'.join(sorted(guests_did_not_came)))