import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.helpers.database import db
from app.models import SistemaCriacao, Territorio, ClasseGalinaceos, Galinaceos

def limpar_numero(valor):
    if pd.isna(valor):
        return None
    valor_str = str(valor).strip().replace(".", "").replace(",", ".")
    if valor_str in ("X", "-", "", "x"):
        return None
    try:
        return int(valor_str)
    except ValueError:
        try:
            return float(valor_str)
        except ValueError:
            return None

def seed():
    app = create_app()

    with app.app_context():
        print("Lendo CSV...")
        df = pd.read_csv(
            os.path.join(os.path.dirname(__file__), "GALINACEOS.csv"),
            sep=";",
            dtype=str
        )

        print("Limpando tabelas...")
        Galinaceos.query.delete()
        ClasseGalinaceos.query.delete()
        Territorio.query.delete()
        SistemaCriacao.query.delete()
        db.session.commit()

        print("Populando sistema_criacao...")
        sistemas = {}
        for valor in df["SIST_CRIA"].unique():
            partes = valor.split("-", 1)
            codigo = partes[0].strip()
            descricao = partes[1].strip() if len(partes) > 1 else valor
            if codigo not in sistemas:
                obj = SistemaCriacao(codigo=codigo, descricao=descricao)
                db.session.add(obj)
                db.session.flush()
                sistemas[codigo] = obj.id

        print("Populando territorio...")
        territorios = {}
        for _, row in df[["NIV_TERR", "COD_TERR", "NOM_TERR"]].drop_duplicates().iterrows():
            chave = (row["NIV_TERR"], str(row["COD_TERR"]).strip(), row["NOM_TERR"])
            if chave not in territorios:
                obj = Territorio(
                    nivel_territorial=row["NIV_TERR"],
                    codigo_territorio=None if pd.isna(row["COD_TERR"]) else str(row["COD_TERR"]).strip(),
                    nome_territorio=row["NOM_TERR"]
                )
                db.session.add(obj)
                db.session.flush()
                territorios[chave] = obj.id

        print("Populando classe_galinaceos...")
        classes = {}
        for _, row in df[["CL_GAL", "NOM_CL_GAL"]].drop_duplicates().iterrows():
            codigo = limpar_numero(row["CL_GAL"])
            if codigo is None or codigo in classes:
                continue
            obj = ClasseGalinaceos(codigo=int(codigo), descricao=row["NOM_CL_GAL"])
            db.session.add(obj)
            db.session.flush()
            classes[int(codigo)] = obj.id

        print("Populando galinaceos...")
        for _, row in df.iterrows():
            partes = row["SIST_CRIA"].split("-", 1)
            codigo_sist = partes[0].strip()
            sist_id = sistemas.get(codigo_sist)

            chave_terr = (row["NIV_TERR"], str(row["COD_TERR"]).strip(), row["NOM_TERR"])
            terr_id = territorios.get(chave_terr)

            cl_codigo = limpar_numero(row["CL_GAL"])
            cl_id = classes.get(int(cl_codigo)) if cl_codigo is not None else None

            if not all([sist_id, terr_id, cl_id]):
                continue

            obj = Galinaceos(
                sist_cria_id=sist_id,
                territorio_id=terr_id,
                cl_gal_id=cl_id,
                e_cria_gal=limpar_numero(row.get("E_CRIA_GAL")),
                e_tem_gal=limpar_numero(row.get("E_TEM_GAL")),
                e_gal_vend=limpar_numero(row.get("E_GAL_VEND")),
                gal_total=limpar_numero(row.get("GAL_TOTAL")),
                gal_vend=limpar_numero(row.get("GAL_VEND")),
                v_gal_vend=limpar_numero(row.get("V_GAL_VEND")),
                vtp_agro=limpar_numero(row.get("VTP_AGRO")),
                rect_agro=limpar_numero(row.get("RECT_AGRO")),
                n_trab_total=limpar_numero(row.get("N_TRAB_TOTAL")),
            )
            db.session.add(obj)

        db.session.commit()
        print("Seed concluído com sucesso!")

if __name__ == "__main__":
    seed()