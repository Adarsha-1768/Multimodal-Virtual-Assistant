import face_recognition
import os

# Path to the directory containing sample images
path = 'samples'

# Function to load images and corresponding labels
def load_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_encodings = []
    labels = []

    for image_path in image_paths:
        # Load the image using face_recognition
        image = face_recognition.load_image_file(image_path)

        # Extract face encodings from the image
        face_encoding = face_recognition.face_encodings(image)

        if len(face_encoding) > 0:
            # Assuming only one face per image for simplicity
            face_encodings.append(face_encoding[0])
            labels.append(os.path.splitext(os.path.basename(image_path))[0])

    return face_encodings, labels

print("Training faces. Please wait...")

# Load images and corresponding labels
faces_encodings, labels = load_images_and_labels(path)

print("Training complete. Now you can recognize faces.")

# Now you can use 'faces_encodings' and 'labels' for face recognition tasks

