import cv2
import numpy as np

def detect_objects(image_path):
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
        
        
    layer_names = net.getUnconnectedOutLayers()
    
    img = cv2.imread(image_path)
    
    height, width, _ = img.shape
    
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416,416), (0, 0, 0), True, crop = False)
    net.setInput(blob)
    outs = net.forward(layer_names)
    
    class_ids = []
    confidences = []
    boxes = []
    
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[1] * width)
                h = int(detection[2] * height)
                
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
                
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    
    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h = boxes[i]
            label  = str(classes[class_ids[i]])
            confidence = confidence[i]
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX)
            
    cv2.imshow("Object Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
detect_objects("example_img.jpg")