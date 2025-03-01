import mediapipe as mp
import cv2
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
def find_face(frame):
    x,y,h,w=0,0,0,0
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        x,y,w,h = x/1000,y/500,w/1000,h/1000
    return x,y,w,h
def locate_point(n, h):
    hi = results.multi_hand_landmarks[-1]
    x = str(results.multi_hand_landmarks[-h].landmark[n]).split('\n')[0]
    y = str(results.multi_hand_landmarks[-h].landmark[n]).split('\n')[1]
    z = str(results.multi_hand_landmarks[-h].landmark[n]).split('\n')[2]
    x = float(x.split(" ")[1])
    y = float(y.split(" ")[1])
    z = float(z.split(" ")[1])
    return x,y,z
sll = []
on = 0
lio = 0
li = []
cuhs = 'a'
cshs = ''
hso = ''
chsfn = 0
wv = ''
wv2 = ''
wvn = 0
wve = 0
def gesture_recognition(frame):
    global sll
    global lio
    global li
    global cuhs
    global cshs
    global chsfn
    global wv
    global wv2
    global hso
    global wvn
    global wve
    num_hands = len(results.multi_hand_landmarks)
    if num_hands == 2:
        x28,y28,z28 = locate_point(8, 2)
        x25,y25,z25 = locate_point(5, 2)
        x212,y212,z212 = locate_point(12, 2)
        x29,y29,z29 = locate_point(9, 2)
        x216,y216,z216 = locate_point(16, 2)
        x213,y213,z213 = locate_point(13, 2)
        x220,y220,z20 = locate_point(20, 2)
        x217,y217,z17 = locate_point(17, 2)
        x24,y24,z24 = locate_point(4, 2)
    else:
        x28,y28,z28 = 0,0,0
        x25,y25,z25 = 0,0,0
        x212,y212,z212 = 0,0,0
        x29,y29,z29 = 0,0,0
        x216,y216,z216 = 0,0,0
        x213,y213,z213 = 0,0,0
        x220,y220,z20 = 0,0,0
        x217,y217,z17 = 0,0,0
        x24,y24,z24 = 0,0,0
    x2i = x25-x28
    y2i = y25-y28
    x2m = x29-x212
    y2m = y29-y212
    x2r = x213-x216
    y2r = y213-y216
    x2p = x217-x220
    y2p = y217-y220
    if x2i < -0.05 and y2i < 0.05 and y2i > -0.05 and x2m < -0.05 and y2m < 0.05 and y2m > -0.05:
        wv2 = 'h2'
    x,y,w,h = 100,100,100,100
    x8,y8,z8 = locate_point(8, 1)
    x5,y5,z5 = locate_point(5, 1)
    xi = x5-x8
    yi = y5-y8
    x12,y12,z12 = locate_point(12, 1)
    x9,y9,z9 = locate_point(9, 1)
    xm = x9-x12
    ym = y9-y12
    x16,y16,z16 = locate_point(16, 1)
    x13,y13,z13 = locate_point(13, 1)
    xr = x13-x16
    yr = y13-y16
    x20,y20,z20 = locate_point(20, 1)
    x17,y17,z17 = locate_point(17, 1)
    xp = x17-x20
    yp = y17-y20
    x4,y4,z4 = locate_point(4, 1)
    xt = x4-x13
    yt = y4-y13
    x0,y0,z0 = locate_point(0, 1)
    wn = 0.08
    wne = 0.12
    if yi < wn and yi > -wn and ym < wn and ym > -wn and yr < wn and yr > -wn and yp < wn and yp > -wn:
        wv = 'wh1.5'
    if wv=='wh1.5' and yi > wne and yi > -wn and ym > wne and ym > -wn and yr > wne and yr > -wn and yp > wne and yp > -wn:
        wv = 'wh1'
    if y2i < wn and y2i > -wn and y2m < wn and y2m > -wn and y2r < wn and y2r > -wn and y2p < wn and y2p > -wn and y2i !=0:
        wv2 = 'wh2.5'
    if wv2 == 'wh2.5' and y2i > wne and y2i > -wn and y2m > wne and y2m > -wn: #and yr > wne and yr > -wn and yp > wne and yp > -wn:
        wv2 = 'wh2'
    x,y,w,h = find_face(frame)
    sizemax = 0.15
    min = 0.09
    minn = -0.09
    if xi > 0.05 and yi < 0.05 and yi > -0.05 and xm > 0.05 and ym < 0.05 and ym > -0.05:
        wv = 'h1'
    if yi< sizemax and yi>-0.15 and xi < min and xi > minn:
        resi = 0
    else:
        resi = 1  
    if ym< sizemax and ym>-0.15 and xm < min and xm > minn:
        resm = 0
    else:
        resm = 1  
    if yr< sizemax and yr>-0.15 and xr < min and xr > minn:
        resr = 0
    else:
        resr = 1  
    if yp> sizemax-0.05: #and xp < min and xp > minn:
        resp = 1
    else:
        resp = 0
    if xt > -0.06 and yt > -0.06 and yt < 0.06 and xt < 0.06:
        rest = 0
    else:
        rest = 1
    if rest == 1 and resi == 1 and resm == 1 and  resr == 1 and resp == 1 :
        cuhs = '5'#'5'
    elif rest == 0 and resi == 0 and  resm == 0 and  resr == 0 and resp == 0 :
        cuhs = 's'
    elif rest == 0 and resi == 1 and  resm == 0 and  resr == 0 and resp == 0 :
        cuhs = '1'
    elif rest == 0 and resi == 1 and resm == 1 and  resr == 0 and resp == 0 :  
        if x8 - x12 > -0.001:
            cuhs = 'r'
        elif x8 - x12 < -0.05:
            cuhs = '2'
        elif x8 - x12 > -0.05 and x8 - x12 < -0.001:
            cuhs = 'u'
        else:
            cuhs = 'none'
    elif rest == 0 and resi == 1 and resm == 1 and  resr == 1 and resp == 0 :
        cuhs = 'w'
    elif rest == 0 and resi == 1 and resm == 1 and  resr == 1 and resp == 1 :
        cuhs = 'b'
    elif rest == 1 and resi == 0 and resm == 0 and  resr == 0 and resp == 1:
        cuhs = 'y'
    elif rest == 1 and resi == 1 and resm == 0 and  resr == 0 and resp == 0 and x4-x12<-0.1 and x4-x16<-0.1 and x4-x20<-0.1:
        cuhs = 'l'
    elif rest == 1 and resi == 1 and x4-x12>-0.1 and x4-x16>-0.1 and x4-x20>-0.1:
        cuhs = 'd'
    elif  rest == 0 and resi == 0 and resm == 0 and  resr == 0 and resp == 1 :
        cuhs = 'i'
    elif  rest == 1 and resi == 1 and resm == 0 and  resr == 0 and resp == 1 :
        cuhs = 'I love you'
    elif rest == 1 and resi == 0 and resm == 1 and  resr == 1 and resp == 1 and x4-x8>-0.1:
        cuhs = 'f'
    elif rest == 1 and x4-x8>-0.05 and x4-x12>-0.05 and x4-x16>-0.05 and x4-x20>-0.05 and x4-x8<0.05 and x4-x12<0.05 and x4-x16<0.05 and x4-x20<0.05:
        cuhs = 'o'
    elif  rest == 1 and resi == 0 and  resm == 0 and  resr == 0 and resp == 0 and x5-x4<0.09 and y5-y4<0.09 and y5-y4>-0.1: 
        cuhs = 'a'
    elif  rest == 1 and resi == 0 and  resm == 0 and  resr == 0 and resp == 0: 
        cuhs = 'approval'
    elif rest == 1 and resi == 1 and resm == 1 and  resr == 0 and resp == 0:
        cuhs = '3'
    elif rest == 0 and resi == 1 and resm == 1 and  resr == 0 and resp == 1:
        cuhs = '7'
    elif rest == 0 and resi == 1 and resm == 0 and  resr == 1 and resp == 1:
        cuhs = '8'
    elif wv=='h1':
        cuhs = 'h'
    else:
        cuhs = 'none'
    if cuhs == cshs:
        chsfn = chsfn + 1
        if chsfn >= 5:
            print(cuhs)
            hso = cuhs
            chsfn = 0
    else:
        chsfn = 0
    cshs = cuhs
    slw = []
    if x-x8 < 0.1 and x-x8 > -0.1: #and sl == 'b':
        wv = 'fh'
    if y-y8 < -0.2 and x-x8 > 0 and y-y8 > -0.5 and x-x8 < 0.2 and hso == 'a':
        wv = 'mfh'
    if y-y4 < -0.2 and x-x4 > 0 and y-y4 > -0.5 and x-x4 < 0.2 and hso == 's':
        wv = 'ifh'
    if x-x8 < -0.2 and x-x8 > -0.4 and wv=='fh':# and sl=='b':
        slw = ['hello']
    if wv=='mfh':
        slw = ['my']
    if wv=='h1' and wv2=='h2':
        slw = ['name']
    if wv=='ifh':
        slw = ['I']
    if wv=='wh1' and wv2=='wh2':
        slw = ['want']
    if wv2=='wh2.5' and yi < -0.1 and ym < -0.1 and yr < -0.1 and yp < -0.1:
        slw = ['cookie']
    if hso=='3' or hso=='u':
        wv = 'no1'
    if wv=='no1' and y4-y8<0.08 and y4-y12<0.08:
        slw = ['no']
    if hso=='o' and x24-x28>-0.05 and x24-x212>-0.05 and x24-x216>-0.05 and x24-x220>-0.05 and x24-x28<0.05 and x24-x212<0.05 and x24-x216<0.05 and x24-x220<0.05:
        slw = ['more']
    if hso=='a':
        wv = 'yes1'
    if wv=='yes1' and hso=='a' and y0-y16<0.08:
        slw = ['yes']
    if hso=='5':
        if wv!='your1':
            wvn = z0
        wv = 'your1'
    if wv=='your1' and wvn< z0:
        slw = ['your']
    if hso=='a' or hso=='o' or hso=='approval' and x8-x5<0.02 and x8-x5>-0.02 and y8-y5<0.02 and y8-y5>-0.02:
        slw = ['you']
    if hso=='d' and x24-x212>-0.1 and x24-x216>-0.1 and x24-x220>-0.1:
        if wve==0:
            wvn = x8-x28
            wvn = wvn-0.1
            wve = 1
        wv = 'meet1'
    if wv=='meet1' and x8-x28<wvn:
        slw = ['meet']
        wve = 0
    [sll.append(item) for item in slw if item not in sll] 
    return hso,sll
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, img = cap.read()
            image = img.copy()
            sl = 'no hand'
            x,y,w,h = 100,100,100,100
            if not success:
                print("Ignoring empty camera frame.")
                continue
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:                      
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    sl,sll = gesture_recognition(image)
            image = cv2.putText(image, sl, (1100,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0), 2,cv2.LINE_4)
            print(sll)    
            cv2.imshow('MediaPipe Hands', image)
            if cv2.waitKey(5) & 0xFF == ord("q"):
                break
cap.release()
