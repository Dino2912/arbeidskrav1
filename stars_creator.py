
import random
import math

file_content = ""

opacity_stars_array = [(16,4),(15,5),(17,5),(9,6),(10,6),(11,6),(12,6),(13,6),(14,6),(15,6),(16,6),(17,6),(18,6),(19,6),(20,6),(21,6),(22,6),(23,6),(10,7),(13,7),(19,7),(22,7),(11,8),(12,8),(20,8),(21,8),(11,9),(12,9),(20,9),(21,9),(10,10),(13,10),(19,10),(22,10),(9,11),(10,11),(11,11),(12,11),(13,11),(14,11),(15,11),(16,11),(17,11),(18,11),(19,11),(20,11),(21,11),(22,11),(23,11),(15,12),(17,12),(16,13)]

index = 50
total_width = 1024 #This and next line should be removed and it should use percentage instead of px TODO
total_height = 568

width = math.floor(index/3*2)
height = index-width

for h in range(height):
    for w in range(width):
        rannumX = 0#random.randrange(-10,10)
        rannumY = 0#random.randrange(-10,10)
        star_squad = random.randrange(0,5)
        matrix_pos = (w,h)
        if(matrix_pos in opacity_stars_array):
            print(f"Opacity star found for matrix position: {matrix_pos[0]},{matrix_pos[1]}!")
            file_content+=f'<div class="star dynamic_opacity_star star_squad_{star_squad}" style="left:calc({math.floor(w*(105/width))}% + {rannumX}px);top:calc({math.floor(h*(105/height))}% + {rannumY}px);"></div>'
        else:
            file_content+=f'<div class="star static_opacity_star star_squad_{star_squad}" style="left:calc({math.floor(w*(105/width))}% + {rannumX}px);top:calc({math.floor(h*(105/height))}% + {rannumY}px);"></div>'

div_file = open("stars_div.txt","w")
div_file.write(file_content)
div_file.close()