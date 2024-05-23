import pandas as pd
import base64
import time
from keras.models import load_model
import mediapipe as mp
from flask import render_template, request, jsonify
from src.app.Http.Controllers.Controller import Controller
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math


class HandSignModel():
    def __init__(self, model_path: str = 'smnist.h5'):
        self.img_counter = 0
        self.img = None
        self.letterpred = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        self.model = load_model(model_path)
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

    def data_uri_to_cv2_img(self, uri):
        encoded_data = uri.split(',')[1]
        nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
        # old (python 2 version):
        # nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)

        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        self.img = img
        return img

    def detect_hand_sign(self, frame = None):
        if frame is None:
            frame = self.img
        h, w, c = frame.shape
        analysisframe = frame
        showframe = analysisframe
        framergbanalysis = cv2.cvtColor(analysisframe, cv2.COLOR_BGR2RGB)
        resultanalysis = self.hands.process(framergbanalysis)
        hand_landmarksanalysis = resultanalysis.multi_hand_landmarks
        if hand_landmarksanalysis:
            for handLMsanalysis in hand_landmarksanalysis:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h
                for lmanalysis in handLMsanalysis.landmark:
                    x, y = int(lmanalysis.x * w), int(lmanalysis.y * h)
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y
                y_min -= 20
                y_max += 20
                x_min -= 20
                x_max += 20

        analysisframe = cv2.cvtColor(analysisframe, cv2.COLOR_BGR2GRAY)
        analysisframe = analysisframe[y_min:y_max, x_min:x_max]
        analysisframe = cv2.resize(analysisframe, (28, 28))

        nlist = []
        rows, cols = analysisframe.shape
        for i in range(rows):
            for j in range(cols):
                k = analysisframe[i, j]
                nlist.append(k)

        datan = pd.DataFrame(nlist).T
        colname = []
        for val in range(784):
            colname.append(val)
        datan.columns = colname

        pixeldata = datan.values
        pixeldata = pixeldata / 255
        pixeldata = pixeldata.reshape(-1, 28, 28, 1)
        prediction = self.model.predict(pixeldata)
        predarray = np.array(prediction[0])
        letter_prediction_dict = {
            self.letterpred[i]: predarray[i] for i in range(
                len(self.letterpred))}
        predarrayordered = sorted(predarray, reverse=True)
        high1 = predarrayordered[0]
        high2 = predarrayordered[1]
        high3 = predarrayordered[2]
        for key, value in letter_prediction_dict.items():
            if value == high1:
                print("Predicted Character 1: ", key)
                print('Confidence 1: ', 100*value)
                return key, 100*value
            elif value == high2:
                print("Predicted Character 2: ", key)
                print('Confidence 2: ', 100*value)
            elif value == high3:
                print("Predicted Character 3: ", key)
                print('Confidence 3: ', 100*value)
        return None, None

class LearningController(Controller):
    global request

    def index():
        title = "Home"
        sub_title = {
            "Home": "web.index", 
            "Learning": "#"
        }
        return render_template("frontend/learning/index.html", title=title, sub_title=sub_title)
    
    def predict():
        if request.form.get("photo"):
            hs = HandSignModel()
            hs.data_uri_to_cv2_img()
            predicted_alphabet, confidence = hs.detect_hand_sign()
        response = {
            "success": False,
            "message": "",
            "predicted": False,
            "alphabet": ""
        }
        if predicted_alphabet:
            response['alphabet'] = predicted_alphabet
            response['predicted'] = True
            response['success'] = True
        print(request.form.get('photo'))
        return jsonify(response)


class VideoStreaming(object):
    def __init__(self):
        super(VideoStreaming, self).__init__()
        self.VIDEO = cv2.VideoCapture(0)

        self.MODEL = HandSignModel()

        self._preview = True
        self._flipH = False
        self._detect = False
        self._exposure = self.VIDEO.get(cv2.CAP_PROP_EXPOSURE)
        self._contrast = self.VIDEO.get(cv2.CAP_PROP_CONTRAST)

    @property
    def preview(self):
        return self._preview

    @preview.setter
    def preview(self, value):
        self._preview = bool(value)

    @property
    def flipH(self):
        return self._flipH

    @flipH.setter
    def flipH(self, value):
        self._flipH = bool(value)

    @property
    def detect(self):
        return self._detect

    @detect.setter
    def detect(self, value):
        self._detect = bool(value)

    @property
    def exposure(self):
        return self._exposure

    @exposure.setter
    def exposure(self, value):
        self._exposure = value
        self.VIDEO.set(cv2.CAP_PROP_EXPOSURE, self._exposure)

    @property
    def contrast(self):
        return self._contrast

    @contrast.setter
    def contrast(self, value):
        self._contrast = value
        self.VIDEO.set(cv2.CAP_PROP_CONTRAST, self._contrast)

    def show(self):
        while (self.VIDEO.isOpened()):
            ret, snap = self.VIDEO.read()
            if self.flipH:
                snap = cv2.flip(snap, 1)

            if ret == True:
                if self._preview:
                    # snap = cv2.resize(snap, (0, 0), fx=0.5, fy=0.5)
                    if self.detect:
                        snap = self.MODEL.detectObj(snap)

                else:
                    snap = np.zeros((
                        int(self.VIDEO.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                        int(self.VIDEO.get(cv2.CAP_PROP_FRAME_WIDTH))
                    ), np.uint8)
                    label = 'camera disabled'
                    H, W = snap.shape
                    font = cv2.FONT_HERSHEY_COMPLEX
                    color = (255, 255, 255)
                    cv2.putText(snap, label, (W//2, H//2), font, 2, color, 2)

                frame = cv2.imencode('.jpg', snap)[1].tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                time.sleep(0.01)

            else:
                break
        print('off')
