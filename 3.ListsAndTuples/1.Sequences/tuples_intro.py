# t = ("a", "b", "c")
# print(t)
# welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
# bad = ("Bad Company", "Bad Company", 1974)
# budgie = ("Nightflight", "Budgie", 1981)
# imelda = ("More Mayhem", "Emilda Day", 2011)
# metallica = ("Ride The Lightning", "Metallica", 1984)

albums = [("Welcome To My Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda Day", 2011),
          ("Ride The Lightning", "Metallica", 1984),
          ]

print(len(albums))
# solution 1
for album in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album[0], album[1], album[2]))

# solution 2 most efficient

print("*" * 50)
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# Solution 2

print("*" * 50)
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# #  metallica[0] = "Master of Puppets" # tuples are immutable and therefore you can't do this
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master Of Puppets"
# print(metallica2)

# title, artist, year = metallica
# print("Title:", title)
# print("Artist:", artist)
# print("Year:", year)
#
# print("*" * 5)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# print("*" * 5)
#
# name, length, width, height, price = table
# print(length * width)
