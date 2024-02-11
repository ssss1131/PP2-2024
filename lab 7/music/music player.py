import pygame, os
from random import randint

pygame.init()
bg = pygame.image.load("bg.png")
screen = pygame.display.set_mode(bg.get_size())
pygame.display.set_caption("Music player")
directory_path = r"C:\Users\Acer\Desktop\универ\2-семестр\пп2\lab\lab 7\music"

play = True
play_music = True

music = [file for file in os.listdir(directory_path) if file.endswith('.mp3')]
current_music = randint(0, len(music) - 1)
pygame.mixer.music.load(music[current_music])
pygame.mixer.music.play(0)
pos=0

# 140-180
# 90-135
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play_music:
                    pygame.mixer.music.pause()
                    play_music=False
                else:
                    pygame.mixer.music.unpause()
                    play_music=True
            elif event.key == pygame.K_RIGHT:
                if current_music != len(music) - 1:
                    current_music += 1
                    pygame.mixer.music.load(music[current_music])
                    pygame.mixer.music.play(0)
                else:
                    current_music = 0
            elif event.key == pygame.K_LEFT:
                if current_music != 0:
                    current_music -= 1
                    pygame.mixer.music.load(music[current_music])
                    pygame.mixer.music.play(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_PX, mouse_PY = pygame.mouse.get_pos()
            if (mouse_PX > 140 and mouse_PX < 180) and (mouse_PY > 90 and mouse_PY < 135):
                if play_music:
                    pygame.mixer.music.pause()
                    play_music=False
                else:
                    pygame.mixer.music.unpause()
                    play_music=True
            elif (mouse_PX > 83 and mouse_PX < 108) and (mouse_PY > 106 and mouse_PY < 121):
                if current_music!=0:
                    current_music-=1
                    pygame.mixer.music.load(music[current_music])
                    pygame.mixer.music.play(0)
            elif (mouse_PX > 220 and mouse_PX < 245) and (mouse_PY > 107 and mouse_PY < 116):
                if current_music != len(music) - 1:
                    current_music += 1
                    pygame.mixer.music.load(music[current_music])
                    pygame.mixer.music.play(0)
                else:
                    current_music = 0

            print(f"x : {mouse_PX}\ny : {mouse_PY}\n")

    screen.blit(bg, (0, 0))

    pygame.display.update()
