import qrcode
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

### função para criar nomes aleatórios
def nomes_imagens(tam):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(tam))
    return result_str

@app.route("/url", methods=["POST"])

### Agora sua rota é /url logo no teste do .http deve acrescentar /url 
def get_url_QRCode():
    ### Coleta da URL enviada no json
    url_data = request.json["url_to_qrcode"]

    qr = qrcode.QRCode(version = 1, box_size = 10, border = 1) ### configuração do estilo do QR Code
    ### metodo para gerar correção
    qr.add_data(url_data)
    qr.make(fit=True) # para ficar quadrado

    ### Renderiza a img na memoria e define as cores
    img = qr.make_image(fill_color = "black", back_color = "white")

    ### Salva a imagem e define local
    name_image = nomes_imagens(15) + ".png"
    img.save(name_image)

    return jsonify({"img_image": name_image})



if __name__ == "__main__":
    app.run(debug=True)