import cv2
from youtube_dl import YoutubeDL


def get_stream_url(url: str) -> str:

    dl = YoutubeDL()
    vid_info = dl.extract_info(url, download=False)

    # Get the highest stream
    stream_format = vid_info["formats"][-1]

    return stream_format["url"]

def extract_frame_to_image(url: str, file_path: str):

    stream = cv2.VideoCapture(url)

    flag, frame = stream.read()
    cv2.imwrite(file_path, frame)


def main():

    # Lofi girl vid_id
    url = "jfKfPfyJRdk"

    stream_url = get_stream_url(url)
    extract_frame_to_image(stream_url, "example.jpg")


if __name__ == "__main__":
    main()

