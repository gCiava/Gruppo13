import json
import time

# Funzione per aprire la mano
def fingeropen_r(i01):
    i01_rightHand_thumb.moveTo(0)
    i01_rightHand_ringFinger.moveTo(0)
    i01_rightHand_pinky.moveTo(0)
    i01_rightHand_majeure.moveTo(0)
    i01_rightHand_index.moveTo(0)
    i01_rightArm_bicep.moveTo(30)
    i01_rightArm_omoplate.moveTo(0)
    i01_rightArm_rotate.moveTo(90)
    i01_rightArm_shoulder.moveTo(50)
    time.sleep(1)

# Funzione per chiudere la mano
def fingerclose_r(i01):
    i01_rightHand_thumb.moveTo(160)
    i01_rightHand_ringFinger.moveTo(160)
    i01_rightHand_pinky.moveTo(160)
    i01_rightHand_majeure.moveTo(160)
    i01_rightHand_index.moveTo(160)
    i01_rightArm_bicep.moveTo(30)
    i01_rightArm_omoplate.moveTo(0)
    i01_rightArm_rotate.moveTo(90)
    i01_rightArm_shoulder.moveTo(50)
    time.sleep(1)

# Funzione per la posizione "N/A" o di riposo
def NanHand_r(i01):
    i01_rightHand_thumb.moveTo(0)
    i01_rightHand_ringFinger.moveTo(0)
    i01_rightHand_pinky.moveTo(0)
    i01_rightHand_majeure.moveTo(0)
    i01_rightHand_index.moveTo(0)
    i01_rightArm_bicep.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    i01_rightArm_rotate.moveTo(90)
    i01_rightArm_shoulder.moveTo(30)
    time.sleep(1)
    
# Funzione per aprire la mano
def fingeropen_l(i01):
    i01_leftHand_thumb.moveTo(0)
    i01_leftHand_ringFinger.moveTo(0)
    i01_leftHand_pinky.moveTo(0)
    i01_leftHand_majeure.moveTo(0)
    i01_leftHand_index.moveTo(0)
    i01_leftArm_bicep.moveTo(30)
    i01_leftArm_omoplate.moveTo(0)
    i01_leftArm_rotate.moveTo(90)
    i01_leftArm_shoulder.moveTo(50)
    time.sleep(1)

# Funzione per chiudere la mano
def fingerclose_l(i01):
    i01_leftHand_thumb.moveTo(160)
    i01_leftHand_ringFinger.moveTo(160)
    i01_leftHand_pinky.moveTo(160)
    i01_leftHand_majeure.moveTo(160)
    i01_leftHand_index.moveTo(160)
    i01_leftArm_bicep.moveTo(30)
    i01_leftArm_omoplate.moveTo(0)
    i01_leftArm_rotate.moveTo(90)
    i01_leftArm_shoulder.moveTo(50)
    time.sleep(1)

# Funzione per la posizione "N/A" o di riposo
def NanHand_l(i01):
    i01_leftHand_thumb.moveTo(0)
    i01_leftHand_ringFinger.moveTo(0)
    i01_leftHand_pinky.moveTo(0)
    i01_leftHand_majeure.moveTo(0)
    i01_leftHand_index.moveTo(0)
    i01_leftArm_bicep.moveTo(0)
    i01_leftArm_omoplate.moveTo(0)
    i01_leftArm_rotate.moveTo(90)
    i01_leftArm_shoulder.moveTo(30)
    time.sleep(1)

# Avvia il motore del robot (i01 è il nome dell'oggetto del robot)
i01 = Runtime.createAndStart("i01", "Speech")
k = 0
while k < 20:
    try:
        # Leggi il file JSON
        with open('C:\\Users\\giang\\Desktop\\Desktop\\Università\\Meccatronica\\CloseOpenHand.json', 'r') as json_file:
            data = json.load(json_file)
            print("Dati JSON letti:", data)  # Messaggio di debug
            
            # Controlla se una mano è rilevata
            if data.get('hand_detected', False):  # Se la chiave esiste e ha valore True
                hand_state = data.get('hand_state', 'Unknown')  # Default 'Unknown' se non esiste
                hand_side = data.get('hand_side', 'Unknown')    # Default 'Unknown' se non esiste
                
                # Casistiche possibili
                if hand_side == "Right" and hand_state == "Open":
                    print("Mano destra aperta!")
                    fingeropen_r(i01)
                    NanHand_l(i01)
                    #i01.speak("La tua mano destra è aperta!")
                
                if hand_side == "Right" and hand_state == "Closed":
                    print("Mano destra chiusa!")
                    fingerclose_r(i01)
                    NanHand_l(i01)
                    #i01.speak("La tua mano destra è chiusa!")
                
                if hand_side == "Left" and hand_state == "Open":
                    print("Mano sinistra aperta!")
                    fingeropen_l(i01)
                    NanHand_r(i01)
                    #i01.speak("La tua mano sinistra è aperta!")
                
                if hand_side == "Left" and hand_state == "Closed":
                    print("Mano sinistra chiusa!")
                    fingerclose_l(i01)
                    NanHand_r(i01)
                    #i01.speak("La tua mano sinistra è chiusa!")
                
                if hand_state == "Unknown" or hand_side == "Unknown":
                    print("Stato della mano o lato sconosciuto.")
                    NanHand_r(i01)
                    NanHand_l(i01)
                    #i01.speak("Non sono sicuro dello stato della tua mano.")
            
            else:  # Nessuna mano rilevata
                print("Nessuna mano rilevata.")
                NanHand_r(i01)
                NanHand_l(i01)
                #i01.speak("Non vedo alcuna mano.")
    
    except FileNotFoundError:
        print("File non trovato. Assicurati che lo script Python sia in esecuzione.")
    
    k += 1
    time.sleep(2)  # Aspetta 10 secondi prima di rileggere
