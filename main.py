import cv2 as cv
from pyzbar.pyzbar import decode
import random

def pickingContainerColor () -> int:
    x = random.randint(1,2)
    
    if x == 1:
        return 0
    else:
        return 255

webcam = cv.VideoCapture(0)

if not webcam.isOpened():
    print("Erro ao acessar a câmera. Certifique-se de que a câmera está conectada e funcionando corretamente.")
else:
    print("Câmera acessada com sucesso. Pressione 'Esc' para sair.")

while True:
    validacao, frame = webcam.read()
    if not validacao:
        print("Erro ao ler a câmera.")
        break

    decoded_objects = decode(frame)
    for obj in decoded_objects:
        # r: int = pickingContainerColor
        # g: int = pickingContainerColor
        # b: int = pickingContainerColor

        rect_pts = obj.rect
        # cv.rectangle(frame, (rect_pts[0], rect_pts[1]), (rect_pts[0] + rect_pts[2], rect_pts[1] + rect_pts[3]), (r, g, b), 2)
        cv.rectangle(frame, (rect_pts[0], rect_pts[1]), (rect_pts[0] + rect_pts[2], rect_pts[1] + rect_pts[3]), (0, 255, 0), 2)

        # cv.putText(frame, "Link: " + str(obj.data.decode('utf-8')), (rect_pts[0], rect_pts[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (r, g, b), 2)
        cv.putText(frame, "Link: " + str(obj.data.decode('utf-8')), (rect_pts[0] + rect_pts[2] + 10, rect_pts[1]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv.imshow("Leitor de QR Code", frame)

    key = cv.waitKey(1)
    if key == 27:
        print("Programa encerrado pelo usuário.")
        break

webcam.release()
cv.destroyAllWindows()
