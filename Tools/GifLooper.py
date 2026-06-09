# from PIL import Image, ImageSequence
# import numpy as np

# GIF_PATH = "output.gif"

# MIN_FRAMES = 30        # don't consider frames before this
# THRESHOLD = 50         # lower = stricter
# best=0
# gif = Image.open(GIF_PATH)

# frames = [
#     np.array(frame.convert("L"), dtype=np.float32)
#     for frame in ImageSequence.Iterator(gif)
# ]

# first = frames[0]

# for i in range(MIN_FRAMES, len(frames)):
#     mse = np.mean((frames[i] - first) ** 2)

#     if mse < THRESHOLD:
#         print(f"Loop frame: {i}")
#         best=i
#         print(f"MSE: {mse:.2f}")
#         break
# else:
#     print("No frame passed threshold.")




from PIL import Image, ImageSequence

INPUT_GIF = "output.gif"
OUTPUT_GIF = "trimmed.gif"

END_FRAME = 80  # loop point found by your other script

gif = Image.open(INPUT_GIF)

frames = []
durations = []

for i, frame in enumerate(ImageSequence.Iterator(gif)):
    if i >= END_FRAME:
        break

    frames.append(frame.copy())
    durations.append(frame.info.get("duration", 100))

if not frames:
    raise RuntimeError("No frames were copied.")

frames[0].save(
    OUTPUT_GIF,
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    optimize=False
)

print(f"Saved {OUTPUT_GIF}")
print(f"Frames kept: {len(frames)}")