# actors = [
#     "Nathan Fillion",
#     "Gina Torres",
#     "Alan Tudyk",
#     "Morena Baccarin",
#     "Adam Baldwin",
#     "Jewel Staite",
#     "Sean Maher",
#     "Summer Glau",
#     "Ron Glass"
# ]

# roles = [
#     "Captian Malcolm Reynolds",
#     "Zoe Washburn",
#     "Hoban Washburn",
#     "Inara Serra",
#     "Jaybe Cobb",
#     "Kaylee Frye",
#     "Dr. Simon Tam",
#     "River Tam",
#     "Derrial Book"
# ]
# i = 0
# acts = []
# for i in range(len(actors)):
#     role = actors[i] + " as " + roles[i]
#     acts.append(role)
# print("""
# Featuring:
# -_-_-_-_-_-_-_-_-_-
# """)
# print(acts)
# mine

actorRoles = [
    ["Nathan Fillion", "Captain Malcolm Reynolds"],
    ["Gina Torres", "Zoe Washburn"],
    ["Alan Tudyk", "Hoban Washburn"],
    ["Morena Baccarin", "Inara Serra"],
    ["Adam Baldwin", "Jayne Cobb"],
    ["Jewel Staite", "Kaylee Frye"],
    ["Sean Maher", "Dr. Simon Tam"],
    ["Summer Glau", "River Tam"],
    ["Ron Glass", "Derrial Book"],
]

print('Featuring: \n=-=-=-=-=-=-=-=-=-')
for actor, role in actorRoles:
    print(actor + " as " + role)