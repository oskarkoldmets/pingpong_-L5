import pygame
import sys

# Initsialiseerime pygame
pygame.init()

# Mänguakna suurus
screenWidth = 640
screenHeight = 480
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Ping-Pong")

# Funktsioon piltide laadimiseks
def load_image(image_path, width, height):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))
    return image

# Palli ja aluse pildid
base_image = load_image("pad.png", 120, 20)
ball_image = load_image("ball-1.png", 20, 20)

# Aluse parameetrid
baseX = (screenWidth - base_image.get_width()) // 2
baseY = int(screenHeight / 1.5)
baseSpeed = 5

# Palli parameetrid
ballX = screenWidth // 2
ballY = screenHeight // 2
ballSpeedX = 5
ballSpeedY = 5

# Punktid
score = 0

# Põhiprogramm
def main():
    global ballX, ballY, ballSpeedX, ballSpeedY, baseX, score

    clock = pygame.time.Clock()
    while True:
        screen.fill((255, 255, 255))

        # Sündmuste töötlus
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Palli liikumine
        ballX += ballSpeedX
        ballY += ballSpeedY

        # Palli põrkamine seintest
        if ballX <= 0 or ballX + ball_image.get_width() >= screenWidth:
            ballSpeedX *= -1
        if ballY <= 0:
            ballSpeedY *= -1

        # Palli ja aluse kokkupõrge
        if ballY + ball_image.get_height() >= baseY and baseX <= ballX <= baseX + base_image.get_width() and ballSpeedY > 0:
            ballSpeedY *= -1
            score += 1

        # Kui pall puudub alumisest äärest
        if ballY + ball_image.get_height() >= screenHeight:
            score -= 1
            ballX = screenWidth // 2
            ballY = screenHeight // 2

        # Aluse liikumine
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and baseX > 0:
            baseX -= baseSpeed
        if keys[pygame.K_RIGHT] and baseX + base_image.get_width() < screenWidth:
            baseX += baseSpeed

        # Palli ja aluse joonistamine
        screen.blit(ball_image, (ballX, ballY))
        screen.blit(base_image, (baseX, baseY))

        # Punktid
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
