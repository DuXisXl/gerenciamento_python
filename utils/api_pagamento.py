import mercadopago
import qrcode
import qrcode_terminal
from qrcode.constants import ERROR_CORRECT_L
from database import DataBase
from datetime import datetime, timezone, timedelta

class Pagamentos(object):
    def __init__(self):
        pass

    def cobrar_pix(self, id_usuario, valor, descricao, email=None):
        sdk = mercadopago.SDK("SEU TOKEN DE ACESSO DO MP")
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {}
        payment_data = {
            "transaction_amount": valor,
            "description": f"{descricao}",
            "payment_method_id": "pix",
            "payer": {
                "email": f"{email}"
            }
        }

        payment_response = sdk.payment().create(payment_data, request_options)
        payment = payment_response["response"]
        info_pagamento = payment
        id_pagamento = info_pagamento["id"]
        status = info_pagamento["status"]
        data = info_pagamento["date_created"]
        data_mili = self.converter_milisegundos(data)
        qr_code_base = info_pagamento["point_of_interaction"]["transaction_data"]["qr_code"]
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(qr_code_base)
        qr.make(fit=True)
        qr.print_tty()
        db = DataBase()
        db.conectar()
        db.insert_pagamento(id_usuario, id_pagamento, valor, descricao, status, data_mili)
        db.close_connection()

    def verificar_pagamento(self, id_usuario):
        db = DataBase()
        db.conectar()
        infos = db.buscar_pagamento(id_usuario)
        for info in infos:
            if info is not None:
                dados = info
        db.close_connection()
        # Consulta o status do pagamento
        sdk = mercadopago.SDK("SEU TOKEN DE ACESSO DO MP")
        payment_info_response = sdk.payment().get(dados["id_pagamento"])
        payment_info = payment_info_response["response"]
        status = payment_info["status"]

        # Verifica se o pagamento foi processado com sucesso
        if status == "approved":
            print("Pagamento aprovado! Realize as ações necessárias.")

        if status == "cancelled":
            print("Pagamento cancelado!")

        if status == "pending":
            print("Pagamento pendente!")

    def cancelar_pagamento(self, id_usuario):
        db = DataBase()
        db.conectar()
        infos = db.buscar_pagamento(id_usuario)
        for info in infos:
            if info is not None:
                if info["status"] == "pending":
                    sdk = mercadopago.SDK("SEU TOKEN DE ACESSO DO MP")
                    payment_id = info["id_pagamento"]
                    payment_data = {
                        "status": "cancelled"
                    }
    
                    payment_response = sdk.payment().update(payment_id, payment_data)
                    payment = payment_response["response"]
                    print('Pagamento cancelado com sucesso')
                    return "Pagamento cancelado com sucesso!"
                elif info["status"] == "approved":
                    print("Pagamento está aprovado!")
                    return "Pagamento está aprovado!"
                else:
                    print("Pagamento já havia sido cancelado!")
                    return "Pagamento já havia sido cancelado!"
            else:
                print('Não foi localizado nenhum pagamento para este usuario.')
                return "Não foi localizado nenhum pagamento para este usuario."
        db.close_connection()

    def converter_milisegundos(self, data):
        date_without_timezone = data[:-6]
        dt = datetime.fromisoformat(date_without_timezone)
        offset = timedelta(hours=int(data[-5:-3]), minutes=int(data[-2:]))
        dt_with_offset = dt.replace(tzinfo=timezone(offset))
        timestamp_ms = int(dt_with_offset.timestamp() * 1000)
        return timestamp_ms

# Pagamentos = Pagamentos()
# Pagamentos.verificar_pagamento(id_usuario='1')
# Pagamentos.cancelar_pagamento(id_usuario='1')
# Pagamentos.cobrar_pix(valor=0.01, descricao="Teste Banco de Dados.", email="eduardoramos245r@gmail.com", id_usuario=1)
