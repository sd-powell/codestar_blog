import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name="dfavq8q6t",
  api_key="127194834435842",
  api_secret="mXMAOvIF_d_OtRCi07BuYboizY0"
)

result = cloudinary.uploader.upload("/Users/stevenpowell/Downloads/google.jpg")
print(result['secure_url'])