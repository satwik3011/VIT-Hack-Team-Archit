from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import pandas as pd

data = pd.read_csv('mast_data.csv')

names_list = data['Names']
dates_list = data['Dates']
projects_list = data['Project']
positions_list = data['Position']

f1 = open("coords.txt", "r")
coordinates = f1.read().split("\n")

flag = True

for i in range(len(names_list)):

    name_to_print = names_list[i]
    date_to_print = dates_list[i]
    project_to_print = projects_list[i]
    position_to_print = positions_list[i]

    image = cv2.imread("sample.jpg")

    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pil_im = Image.fromarray(cv2_im_rgb)

    draw = ImageDraw.Draw(pil_im)
    font = ImageFont.truetype("./fonts/SourceSansPro-Regular.ttf", 28)
    font1 = ImageFont.truetype("./fonts/SourceSansPro-Regular.ttf", 20)

    draw.text((int(coordinates[0]), int(coordinates[1])), name_to_print, font=font, fill='red')
    draw.text((int(coordinates[2]), int(coordinates[3])), date_to_print, font=font1, fill='blue')
    draw.text((int(coordinates[4]), int(coordinates[5])), project_to_print, font=font1, fill='blue')
    draw.text((int(coordinates[6]), int(coordinates[7])), position_to_print, font=font1, fill='blue')

    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    if flag:
        cv2.imshow('Certificate', cv2_im_processed)
        flag = False
    path = ''
    cv2.imwrite('./output/' + name_to_print + '.png', cv2_im_processed)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

f1.close()