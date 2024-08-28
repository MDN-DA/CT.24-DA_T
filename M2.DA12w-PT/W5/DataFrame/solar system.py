import pandas as pd

df=pd.DataFrame([
    ("Mercury",166.85,2439.7,"Gray","Smallest planet in our solar system, often referred to as Earth's 'twin'"),
    ("Venus",463.85,6051.8,"Yellowish-Brown","Hottest planet in our solar system, with a thick atmosphere that traps heat"),
    ("Earth",15.85,6371,"Blue","Only known planet to support life, with a unique atmosphere that allows for liquid water"),
    ("Mars",-63.15,3389.5,"Reddish-Brown","Often called the 'Red Planet' due to its iron oxide-rich surface"),
    ("Jupiter",-108.15,69911,"Reddish-Brown with white bands","Largest planet in our solar system, with a Great Red Spot, a massive storm that has been raging for centuries."),
    ("Saturn",-178.15,58232,"Pale Yellow","Known for its prominent rings, composed of ice and rock particles"),
    ("Uranus",-201.15,25362,"Blue-Green","Rotates on its side, likely due to a collision early in its history"),
    ("Neptune",-214.15,24622,"Blue","Has the strongest winds in the solar system, capable of reaching speeds of over 2,000 km/h")
    ],columns=["Planet","Average Temperature (°C)","Radius (in km)","Color","Interesting Feature"])
# df.to_excel("solar system.xlsx", index=False)
# print(df)

df["Discovered by"]=["Ancient Civilizations","Ancient Civilizations","N/A","Ancient Civilizations","Ancient Civilizations","Ancient Civilizations","William Herschel","John Couch Adams & Urbain Le Verrier"]
df["Year"]=["Unknown","Unknown","N/A","Unknown","Unknown","Unknown","1781","1846"]
df["Elements"]=["Rock & Metal","Rock & Metal","Rock & Metal","Rock & Metal","Gas Giant (hydrogen, helium)","Gas Giant (hydrogen, helium)","Ice Giant (hydrogen, helium, methane)","Ice Giant (hydrogen, helium, methane)"]
# print(df)
# print()
pluto=pd.DataFrame({
    "Planet":["Pluto"],
    "Average Temperature (°C)":[-229],
    "Radius (in km)":[1188.3],
    "Color":["Light Brown with white and darker regions"],
    "Interesting Feature":["Pluto was reclassified as a dwarf planet in 2006 but remains an object of fascination due to its complex surface and five known moons, including Charon, its largest moon"],
    "Discovered by":["Clyde Tombaugh"],
    "Year":[1930],
    "Elements":["Ice & Rock"]})
df=pd.concat([df, pluto])
# df.to_excel("solar system_2.xlsx", index=False)
# print(df)
# print()
df=df.set_index("Planet")
print(df.loc["Venus":"Jupiter"])
# print()
# df=df.set_index("Planet Name")
# planet_selected = input("Planet name: ")
