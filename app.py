from cProfile import label
from re import I
from tkinter import image_names
import face_recognition
import cv2
import numpy as np
import csv

video_capture = cv2.VideoCapture(0)

# 空の配列を定義しないとappendで要素を追加できない
labels = []
filenames =[]
images = []
encodings = []
known_face_encodings = []
known_face_names = []


# 画像リスト(csvファイルを読み込み
with open('list.csv',encoding="utf-8") as f:
    #header = next(csv.reader(f))         # ヘッダーをスキップして2行目から読み込む
    reader = csv.reader(f)
    for row in reader:
        labels.append(row[0])            # 1列目のラベルデータをlabelsリストに格納する
        filenames.append(row[1])         # 2列目のデータをfilenameリストに格納する

data_num = len(filenames)    

for i in range(data_num):
    # 画像を読み込み、顔の特徴値を取得してリストに格納していく
    images.append(face_recognition.load_image_file("images/" + filenames[i]))
    encodings.append(face_recognition.face_encodings(images[i])[0])
    known_face_encodings.append(encodings[i])
    known_face_names.append(labels[i])

while True:
    # Webカメラの1フレームを取得、顔を検出し顔の特徴値を取得する
    _, frame = video_capture.read()
    #メモリ上の連続した配列(Cオーダー)を返す(変更)
    rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # 1フレームで検出した顔分ループする
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 認識したい顔の特徴値と検出した顔の特徴値を比較する
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding,0.4)
        name = "Unknown"
        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # 顔の周りに四角を描画する
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 名前ラベルを描画
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
        
        # 検出した人名をテキストファイルに書き込む
        with open("name.txt", "w", encoding='utf-8') as f:
            f.write(name)

    # 結果を表示する
    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
