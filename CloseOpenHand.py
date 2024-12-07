import json
import cv2
import mediapipe as mp

# Inizializzazione di MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Inizializza il rilevamento delle mani
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Apri la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Impossibile aprire la webcam")
    exit()

while True:
    # Leggi un fotogramma dalla webcam
    success, img = cap.read()
    if not success:
        print("Impossibile ricevere il fotogramma. Uscita...")
        break

    # Specchia l'immagine orizzontalmente (così sarà come se la persona si guarda allo specchio)
    img = cv2.flip(img, 1)  # 1 significa specchiare orizzontalmente

    # Converti l'immagine in RGB (MediaPipe lavora in RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Esegui il rilevamento delle mani
    result = hands.process(img_rgb)

    # Variabili per determinare se una mano è stata rilevata, il suo stato e il lato (destra/sinistra)
    hand_detected = False
    hand_state = "Unknown"
    hand_side = "Unknown"

    # Se ci sono mani rilevate, estrai i landmarks
    if result.multi_handedness and result.multi_hand_landmarks:
        hand_detected = True
        for hand_info, hand_landmarks in zip(result.multi_handedness, result.multi_hand_landmarks):
            # Ottieni il lato della mano (Left o Right)
            hand_side = hand_info.classification[0].label

            # Disegna i landmarks e lo scheletro della mano
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Estrai i punti di riferimento dei landmarks per il pollice e l'indice
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calcola la distanza tra il pollice e l'indice per determinare se la mano è aperta o chiusa
            if abs(thumb_tip.x - index_tip.x) < 0.05:  # Se il pollice e l'indice sono vicini
                hand_state = "Closed"
            else:
                hand_state = "Open"

    # Scrivi i dati nel file JSON
    with open('CloseOpenHand.json', 'w') as json_file:
        json.dump({
            'hand_detected': hand_detected,
            'hand_state': hand_state,
            'hand_side': hand_side
        }, json_file)

    # Mostra l'immagine con lo scheletro
    cv2.imshow("Hand Skeleton", img)

    # Premi 'q' per uscire
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia la webcam e chiudi tutte le finestre
cap.release()
cv2.destroyAllWindows()