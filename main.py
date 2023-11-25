
import cv2
from pyzbar.pyzbar import decode

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Erro ao acessar a câmera. Certifique-se de que a câmera está conectada e funcionando corretamente.")
else:
    print("Câmera acessada com sucesso. Pressione 'Esc' para sair.")

while True:
    validacao, frame = webcam.read()

    frameWidth = webcam.get(3)  # float `frameWidth`640 / 3 = 212
    frameHeight = webcam.get(4)  # float `height`480 / 3 = 160

    if not validacao:
        print("Erro ao ler a câmera.")
        break

    decoded_objects = decode(frame)
    for obj in decoded_objects:
        rect_pts = obj.rect

        center_x = rect_pts[0] + rect_pts[2] // 2
        center_y = rect_pts[1] + rect_pts[3] // 2

        if center_x < frameWidth / 3:
            color = (155,8,140)  # roxo 
        elif center_x < 2 * frameWidth / 3:
            if center_y < frameHeight / 2:
                color = (0,0,255)  # Vermelho
            else:
                color = (0,255,0)  # verde        
        else:
            color = (155,8,140)  # roxo


        cv2.rectangle(frame, (rect_pts[0], rect_pts[1]), (rect_pts[0] + rect_pts[2], rect_pts[1] + rect_pts[3]), color, 2)
        cv2.putText(frame, "-> " + str(obj.data.decode('utf-8')), (rect_pts[0] + rect_pts[2] + 10, rect_pts[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Leitor de QR Code", frame)

    key = cv2.waitKey(1)
    if key == 27:
        print("Programa encerrado pelo usuário.")
        break

webcam.release()
cv2.destroyAllWindows()



# Camera fixa
# imagem dividida em 9 quadros
# coluna centras (verde e vermelho), colunas laterais (roxo)

# QR codes tem um lugar pre determinado
# ordem de empilhamento
# quando removido fica vermelho, quando volta fica verde