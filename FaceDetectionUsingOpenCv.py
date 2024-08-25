## importing libraries
import cv2
import os
import face_recognition

## Load the cascade
face_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

## Load the training images and encode faces
known_face_encodings = []
known_face_names = []

# Function to load training images and encode faces
def load_training_images():
    # Directory containing training images
    training_dir = 'training_images'

    # List all folders (each folder represents a person)
    for person_folder in os.listdir(training_dir):
        # Path to the person's folder
        person_folder_path = os.path.join(training_dir, person_folder)
        
        # List all image files in the person's folder
        for filename in os.listdir(person_folder_path):
            # Get the full path of the image file
            path = os.path.join(person_folder_path, filename)
            
            # Load the image using face_recognition library
            image = face_recognition.load_image_file(path)
            
            # Encode the face(s) in the image
            face_encodings = face_recognition.face_encodings(image)
            
            # If face encoding(s) found, add them to known_face_encodings
            if len(face_encodings) > 0:
                known_face_encodings.append(face_encodings[0])
                # Extract the name from the folder name
                name = person_folder
                known_face_names.append(name)

# Load training images and encode faces
load_training_images()

## Read the input image
img = cv2.imread('test/test1.jpg')

## Convert the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

## Recognition
for (x, y, w, h) in faces:
    # Extract face region
    face_image = img[y:y+h, x:x+w]
    
    # Convert face image to RGB format
    rgb_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
    
    # Encode the face
    face_encodings = face_recognition.face_encodings(rgb_face_image)
    
    # Initialize variables for best match
    best_match_name = "Unknown"
    best_match_distance = 1.0  # Set to maximum distance initially
    
    # Check if any face encodings are found
    if len(face_encodings) > 0:
        # Compare with known face encodings
        for i, known_face_encoding in enumerate(known_face_encodings):
            matches = face_recognition.compare_faces([known_face_encoding], face_encodings[0])
            face_distance = face_recognition.face_distance([known_face_encoding], face_encodings[0])
            
            # If the distance is smaller than previous best match, update best match
            if matches[0] and face_distance < best_match_distance:
                best_match_name = known_face_names[i]
                best_match_distance = face_distance
        
        # Draw rectangle and name on the image
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, best_match_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)


## Show the output
cv2.namedWindow('Face Detection', cv2.WINDOW_NORMAL)
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
