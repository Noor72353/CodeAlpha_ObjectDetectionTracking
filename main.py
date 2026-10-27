
import cv2
import argparse
from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser(
        description="Object detection and tracking using YOLO and ByteTrack."
    )
    parser.add_argument(
        "--source",
        type=str,
        default="0",
        help="Webcam index or path to a video file."
    )
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source

    model = YOLO("yolo11n.pt")
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"Error: Could not open video source: {args.source}")
        return

    print("Object detection and tracking started. Press Q to quit.")

    while True:
        success, frame = cap.read()

        if not success:
            print("Video ended or a frame could not be read.")
            break

        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False
        )

        annotated_frame = results[0].plot()

        # Resize proportionally without distorting the image.
        height, width = annotated_frame.shape[:2]
        max_width = 960
        max_height = 540

        scale = min(max_width / width, max_height / height)

        new_width = int(width * scale)
        new_height = int(height * scale)

        display_frame = cv2.resize(
            annotated_frame,
            (new_width, new_height)
        )

        cv2.imshow(
            "CodeAlpha - Object Detection and Tracking",
            display_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
