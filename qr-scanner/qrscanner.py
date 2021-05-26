from pyzbar import pyzbar
import cv2


def banner():
    print("""
        \033[31m.▄▄▄  ▄▄▄\033[34m  .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄\033[0m
        \033[31m▐▀•▀█ ▀▄ █·\033[34m▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·▀▄ █·\033[0m
        \033[31m█▌·.█▌▐▀▀▄\033[34m ▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄\033[0m
        \033[31m▐█▪▄█·▐█•█▌\033[34m▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌\033[0m
        \033[31m·▀▀█. .▀  ▀\033[34m ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀\033[0m
    """)
    print("\033[32m[+] Created By https://github.com/esrefyigitbasi-dev")
    print("[+] https://github.com/esrefyigitbasi-dev/QR-Code-Cam-Scanner\033[0m\n")


def main():

    capture = cv2.VideoCapture(0)
    code = str()

    while True:

        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            barcodeData = barcode.data.decode("utf-8")
            if code != barcodeData:
                cv2.imwrite(f"{barcodeData}.png", capture.read()[1])
                print(f"\033[34mBarcode : \033[0m{barcodeData}")
            code = barcodeData
            text = "{}".format(barcodeData)
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    banner()
    main()
