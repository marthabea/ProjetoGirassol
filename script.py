import cv2
import pytesseract

# Abrir o arquivo
img = cv2.imread("")

# caminho do executável do tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

# configuração para interpretar letras cursivas em português

# config_port = r'--oem 3 --psm 6 -l por'
result_transf_img = pytesseract.image_to_string(img)


# formatação de string para limpeza do output

def format_text(text=str):
    lines = text.split('\n')  # Dividir o texto em linhas para melhorar a organização
    new_text = ""
    for line in lines: 
        line = line.strip()  # Remover espaços em branco no início e no final de cada linha
        if line:  
            new_text += line + '\n'
    return new_text

# formatação a partir do def
result = format_text(result_transf_img)

# novo texto com a formatação
print(result)
