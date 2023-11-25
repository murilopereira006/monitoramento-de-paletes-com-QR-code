import cv2
from pyzbar.pyzbar import decode

# Inicialização da captura da webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Erro ao acessar a câmera. Certifique-se de que a câmera está conectada e funcionando corretamente.")
else:
    print("Câmera acessada com sucesso. Pressione 'Esc' para sair.")

while True:
    validacao, frame = webcam.read()
    if not validacao:
        print("Erro ao ler a câmera.")
        break

    # Decodificar QR codes na imagem da webcam
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        # Obter os pontos do QR code como um retângulo
        rect_pts = obj.rect
        cv2.rectangle(frame, (rect_pts[0], rect_pts[1]), (rect_pts[0] + rect_pts[2], rect_pts[1] + rect_pts[3]), (0, 255, 0), 2)

        # Mostrar o conteúdo do QR code na tela
        cv2.putText(frame, "Link: " + str(obj.data.decode('utf-8')), (rect_pts[0], rect_pts[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Leitor de QR Code", frame)

    # Aguardar 1 milissegundo e verificar se a tecla 'Esc' foi pressionada
    key = cv2.waitKey(1)
    if key == 27:
        print("Programa encerrado pelo usuário.")
        break

# Liberar a captura da webcam e fechar as janelas
webcam.release()
cv2.destroyAllWindows()
