import pygame

pygame.init()

# Akna suurus ja seadistused
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ül2.tekstid-Jürgen Almar")

bg = pygame.image.load("pood.jpg")
myya = pygame.image.load("müüa.png")
myya = pygame.transform.scale(myya, [250,300])
jutumull = pygame.image.load("jutumull.png")
jutumull = pygame.transform.scale(jutumull, [260,200])
mook = pygame.image.load("Mõõk.png")
mook = pygame.transform.scale(mook, [100,200])


screen.blit(bg,[0,0])
screen.blit(myya,[110,160])
screen.blit(jutumull,[250,67])
screen.blit(mook,[150, 160])
# Teksti seadistamine
font = pygame.font.Font(None, 26)
text = font.render("Tere! Mina olen Jürgen Almar", True, (255, 255, 255)) # Valge vär
text_rect = text.get_rect(center=(380, 150))
screen.blit(text, text_rect) # Joonistame teksti

pygame.display.flip()
pygame.display.update()  # Kuvame ekraanile


running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

pygame.quit()