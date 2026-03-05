file=input("File name : ").strip().lower()
if "." in file:
    extension=file.rsplit(".",1)[1]
else:
    extension=""

match extension:
    case "gif"|"png" :
        print(f"image/{extension}")
    case "jpg"|"jpeg":
        print("image/jpeg")
    case "pdf":
        print(f"application/{extension}")
    case "zip":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")