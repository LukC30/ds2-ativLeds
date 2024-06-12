from database import banco
from agenda import app, leds

def corLed():
    cor = ""
    if(leds.LedAzul.isChecked()):
        cor = "Azul"
        return cor
    elif(leds.LedVermelho.isChecked()):
        cor = "Vermelho"
        return cor
    cor = "Verde" 
    return cor


def submit():
    cursor = banco.cursor()
    try:
        cursor.execute(f"Insert into tbl_led (nome) values('{corLed()}')")
        banco.commit()
        print("Cadastro realizado com sucesso")
    except Exception as e:
        print(f"Deu merda ai filhao, ve ai: {e}")
    return    

leds.BtnEnviar.clicked.connect(submit)
leds.show()
app.exec()
