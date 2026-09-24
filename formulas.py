def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC) e retorna o valor e a classificação."""
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25.0:
        classificacao = "Peso normal"
    elif 25.0 <= imc < 30.0:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
        
    return round(imc, 2), classificacao

def calcular_tmb(peso, altura_cm, idade, sexo):
    """Calcula a Taxa Metabólica Basal (TMB / Gasto Basal) usando a fórmula de Mifflin-St Jeor."""
    if sexo.lower() == 'm':
        tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
    else:
        tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
    return round(tmb, 2)

def calcular_get(tmb, nivel_atividade):
    """Calcula o Gasto Energético Total (GET) com base no fator de atividade física."""
    fatores = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'intenso': 1.725,
        'muito_intenso': 1.9
    }
    fator = fatores.get(nivel_atividade.lower(), 1.2)
    return round(tmb * fator, 2)

def calcular_macros(get, objetivo):
    """Define as calorias alvo e distribui os macronutrientes (proteína, carboidrato, gordura)."""
    if objetivo.lower() == 'cutting': # Perda de gordura (déficit de 20%)
        calorias_alvo = get * 0.80
    elif objetivo.lower() == 'bulking': # Ganho de massa (superávit de 10%)
        calorias_alvo = get * 1.10
    else: # Manutenção
        calorias_alvo = get

    # Distribuição padrão: 30% proteínas, 40% carboidratos, 30% gorduras
    proteina_g = (calorias_alvo * 0.30) / 4
    carboidrato_g = (calorias_alvo * 0.40) / 4
    gordura_g = (calorias_alvo * 0.30) / 9

    return {
        "calorias_alvo": round(calorias_alvo, 2),
        "proteina": round(proteina_g, 2),
        "carboidrato": round(carboidrato_g, 2),
        "gordura": round(gordura_g, 2)
    }




