# import cv2


# try:
#     # Your code here
#   cap = cv2.VideoCapture(0)
#   cap.set(3, 640)
#   cap.set(4, 480)

#   while True:
#     success, img = cap.read()
#     cv2.imshow("Face Attendance", img)
#     cv2.waitKey(1)
# except KeyboardInterrupt:
#     print("Program interrupted by user.")
# except IOError:
#     print("Error reading webcam or image.")
# except Exception as e:
#     print(f"Unexpected error: {e}")
# finally:
#     # Release resources, regardless of errors
#     cap.release()
#     cv2.destroyAllWindows()