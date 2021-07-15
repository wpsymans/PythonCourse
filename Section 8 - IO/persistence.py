#this file creates or opens a dat and dir file

import shelve

d = shelve.open("weapons")

d['Sword'] = "a long blade for slashing and hacking"
d['Axe'] = "a heavy two handed blade for chopping"

for weapon in d:
    print(d.get(weapon))

