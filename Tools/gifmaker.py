import cv2

background = cv2.VideoCapture("background.mp4")
overlay = cv2.VideoCapture("overlay.mp4")

# First overlay crop (top-left region)
overlay1_x_percent = 0.4
overlay1_y_percent = 0.38

# Second overlay crop (top-left region)
overlay2_x_percent = 0.13
overlay2_y_percent = 1

# Frame offset
overlay_delay_frames = 30

fps = background.get(cv2.CAP_PROP_FPS)
width = int(background.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(background.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Apply delay
if overlay_delay_frames > 0:
    overlay.set(cv2.CAP_PROP_POS_FRAMES, overlay_delay_frames)
elif overlay_delay_frames < 0:
    background.set(cv2.CAP_PROP_POS_FRAMES, -overlay_delay_frames)

out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

while True:
    ret_bg, bg_frame = background.read()
    ret_ov, ov_frame = overlay.read()

    if not ret_bg or not ret_ov:
        break

    ov_frame = cv2.resize(ov_frame, (width, height))

    # ----- Overlay 1 -----
    x1 = int(width * overlay1_x_percent)
    y1 = int(height * overlay1_y_percent)

    x1 = max(0, min(x1, width))
    y1 = max(0, min(y1, height))

    bg_frame[:y1, :x1] = ov_frame[:y1, :x1]

    # ----- Overlay 2 -----
    x2 = int(width * overlay2_x_percent)
    y2 = int(height * overlay2_y_percent)

    x2 = max(0, min(x2, width))
    y2 = max(0, min(y2, height))

    bg_frame[:y2, :x2] = ov_frame[:y2, :x2]

    out.write(bg_frame)

background.release()
overlay.release()
out.release()
cv2.destroyAllWindows()







from moviepy import VideoFileClip

clip = VideoFileClip("output.mp4")

# Optional: resize and reduce FPS to keep GIF size reasonable
clip = clip.resized(width=400)
clip = clip.with_fps(10)

clip.write_gif("output.gif")