
import cv2
import time
from collections import Counter
from ultralytics import YOLO

# Load your pretrained model
model = YOLO("yolo26n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam.")
    raise SystemExit

# Try to request a reasonable webcam resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

previous_time = time.time()

print("Real-Time Object Detection started!")
print("Press Q to quit.")

while True:
    success, frame = cap.read()

    if not success:
        print("Could not read webcam frame.")
        break

    # Run YOLO detection
    results = model.predict(
        source=frame,
        conf=0.35,
        imgsz=640,
        verbose=False
    )

    result = results[0]
    output = result.plot()

    # Count objects in the current frame
    labels = [
        model.names[int(box.cls[0])]
        for box in result.boxes
    ]
    counts = Counter(labels)

    # Calculate FPS
    current_time = time.time()
    elapsed = current_time - previous_time
    fps = 1 / elapsed if elapsed > 0 else 0
    previous_time = current_time

    # Add dashboard information
    cv2.rectangle(output, (5, 5), (300, 105), (25, 25, 25), -1)

    cv2.putText(
        output,
        f"FPS: {fps:.1f}",
        (15, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        f"Objects detected: {len(labels)}",
        (15, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # Display counts by class
    summary = ", ".join(
        f"{name}: {count}" for name, count in counts.most_common(3)
    ) or "No objects detected"

    cv2.putText(
        output,
        summary[:42],
        (15, 88),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        (0, 255, 255),
        1
    )

    cv2.imshow("AI Real-Time Object Detector", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("Object detector closed.")
