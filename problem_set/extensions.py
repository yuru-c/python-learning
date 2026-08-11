# file_name = input("File name: ").strip().lower()
# extensions = ("gif", "jpg", "jpeg", "png", "pdf", "txt", "zip")

# if file_name.endswith(extensions):
#     _, extension = file_name.split(".")
#     if extension in ("gif", "jpg", "jpeg", "png"):
#         print(f"image/{extension}")
#     elif extension in ("pdf", "zip"):
#         print(f"application/{extension}")
#     elif extension == "txt":
#          print("text/plain")
# else:
#     print("application/octet-stream")

file_name = input("File name: ").strip().lower()

if "." in file_name:
    extension = file_name.rsplit(".", 1)[1]
    # my.photo.jpg => ["my.photo", "jpg"]
else:
    extension = ""

if extension in ("gif", "jpg", "jpeg", "png"):
    print(f"image/{extension}")
elif extension in ("pdf", "zip"):
    print(f"application/{extension}")
elif extension == "txt":
    print("text/plain")
else:
    print("application/octet-stream")