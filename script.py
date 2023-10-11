import cv2
import pytesseract

# Abrir o arquivo
image = cv2.imread("teste_letras.png")

# caminho do executável do tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

# configuração para interpretar letras em português e conversão da img
config_br = r'--oem 3 --psm 6 -l por'
new_image = pytesseract.image_to_string(image)

# formatação de string para limpeza do output
class FormatText:
    def text(self, text):
     lines = text.split('\n')  # Dividir o texto em linhas para melhorar a organização
     new_text = ""
     for line in lines: 
        line = line.strip()  # Remover espaços em branco no início e no final de cada linha
        if line:  
            new_text += line + '\n'

     return new_text

# formatação do texto contido na minha imagem
format = FormatText() 
result = format.text(new_image)

# novo texto com a formatação
print(result)
