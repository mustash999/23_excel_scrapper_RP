import time
import pygame

def splash():
	pygame.init()

	# Load the image
	image = pygame.image.load("resources/sscreen.jpg")
	resized_image = pygame.transform.scale(image, (640, 360))

	# Create a window to display the image
	infoObject = pygame.display.Info()
	window = pygame.display.set_mode((640 , 360),pygame.NOFRAME|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.SRCALPHA)
	pygame.display.set_caption("Splash Screen")

	# Display the image for 2 seconds
	window.blit(resized_image, (0, 0))
	pygame.display.flip()
	time.sleep(2)

	# Close the window
	pygame.quit()