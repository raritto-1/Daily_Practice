from plyer import notification
import pygame

pygame.init()
sound = pygame.mixer.Sound("output.wav")

if __name__ == "__main__":
    notification.notify(
        title="Please Drink Alcohol Daily",
        message="It makes you happy and also provides relief from the pain of anxiety, so please drink alcohol daily, time to time.",
        timeout=15
    )
    
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    
    pygame.quit()
    print('You got the notification successfully')
