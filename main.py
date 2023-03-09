import cv2
import pygame

pygame.init() 

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("hoang son")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Vẽ một cái hình chữ nhật quanh mặt trong tranh
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Biến frame thành RGB cho pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Chạy frame lên pygame
    frame = cv2.flip(frame, 1)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            quit()