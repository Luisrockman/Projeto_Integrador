
def calculate_taxes(tipo_atividade, receita_mensal):
    INSS = 75.90
    ISS = 5.00
    ICMS = 1.00

    if tipo_atividade == "Comércio":
        inss = receita_mensal * 0.05
        icms = ICMS
        total = inss + icms
    elif tipo_atividade == "Serviços":
        inss = receita_mensal * 0.05
        iss = ISS
        total = inss + iss
    elif tipo_atividade == "Comércio e Serviços":
        inss = receita_mensal * 0.05
        icms = ICMS
        iss = ISS
        total = inss + icms + iss
    else:
        return None

    return {
        "INSS": round(inss, 2),
        "ICMS": round(icms, 2) if 'icms' in locals() else 0,
        "ISS": round(iss, 2) if 'iss' in locals() else 0,
        "Total": round(total, 2)
    }
