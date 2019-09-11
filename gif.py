import os
import imageio


def get_gif(step=0.2):
    image_list = os.listdir(os.getcwd()+'\png')
    image_list.sort(key= lambda x:int(x[:-4]))
    gif_name = 'C://Users/HP/Desktop/street.gif'
    frames = []
    for name in image_list:
        if name[-3:]!= '.py':
            frames.append(imageio.imread('png'+'\\'+name))
        else:
            pass
    imageio.mimsave(gif_name, frames, 'GIF', duration=step)
print(1111123135463)
