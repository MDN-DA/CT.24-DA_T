dinosaurs=["Triceratops","Velociraptor","Ankylosaurus","Archaeopteryx","Tyrannosaurus Rex","Stegosaurus","Iguanodon"]
# saurus_dinosaurs =[]

# for dino in dinosaurs:
#     if "saurus" in dino:
#         saurus_dinosaurs.append(dino)
# print(saurus_dinosaurs)
# print(dinosaurs)

saurus_dinosaurs=[dino for dino in dinosaurs if "saurus" in dino]
print(saurus_dinosaurs)
