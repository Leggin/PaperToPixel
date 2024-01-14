import io
import streamlit as st
from PIL import Image
import requests
import config

if "image_rotation" not in st.session_state:
    st.session_state["image_rotation"] = 0


def rotate_image(image: Image.Image, angle: float) -> Image.Image:
    st.session_state["image_rotation"] = (
        st.session_state["image_rotation"] + angle
    ) % 360
    return image.rotate(st.session_state["image_rotation"], expand=True).copy()


def main():
    st.title("PaperToPixel Upload")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)

        # make sure image has the rotation from state
        image = rotate_image(image, 0)

        # Button to rotate the image
        if st.button("↺"):
            image = rotate_image(image, 90)

        st.image(image, caption="Uploaded Image", width=200)
        if st.button("Send"):
            # Convert Image to Bytes
            image_bytes = io.BytesIO()

            if image.mode != "RGB":
                # This is required to save the image in JPEG format
                image = image.convert("RGB")

            image.save(image_bytes, format="JPEG")
            image_bytes = image_bytes.getvalue()

            # Prepare data for the POST request
            files = {"file": ("image.jpg", image_bytes, "image/jpeg")}
            response = requests.post(
                f"{config.API_BASE_URL}/upload", files=files, timeout=15
            )

            if response.status_code == 200:
                st.success("Image successfully sent!")
            else:
                st.error(f"Error sending image. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
