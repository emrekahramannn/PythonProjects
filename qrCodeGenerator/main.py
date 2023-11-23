import pyqrcode

def TakeUrl():
    url = input("Enter url to generate qr code: ")
    return url


def GenerateQR(url, size=5):
    """
        This functions creates a QR code for given URL.
        Return -> .svg file
    """
    while True:
        size = input("Choose a size between 1-10 for your QR code image: ")
        
        size = size.strip()

        if size == "":
            size = 5
            break
        else:
            try:
                size = int(size)
            except ValueError:
                print("Please enter a valid number in the range.")
                continue
            else:
                if 1<= size <= 10:
                    break
    


    try:
        qr_code = pyqrcode.create(url)
    except:
        print("An error has occured.")
        quit()
    else:
        qr_code.svg("qrcode.svg", scale=size)


if __name__ == "__main__":
    url = TakeUrl()
    GenerateQR(url)