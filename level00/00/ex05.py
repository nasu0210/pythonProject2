from PIL import Image
# image=Image.open('c:/data2/b.png')
# resized_image=image.resize((200,100))
# resized_image.save('c:/data2/b_small.png')
for i in range(1,13):
    imName='m'+str(i).zfill(2)+'.png'
    newName = 'm' + str(i).zfill(2) + '_big.png'
    image = Image.open('c:/data2/'+imName)
    resized_image = image.resize((150, 150))
    resized_image.save('c:/data2/'+newName)