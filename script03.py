# %%
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

# from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime

import pandas as pd
import time
import os

# DRIVER_PATH = "C://Users/paulo/OneDrive/Documentos/Consorcio Automation/Chrome/chromedriver.exe"
# CLI_PATH = "C://Users/paulo/OneDrive/Documentos/Consorcio Automation/Clientes"
CLI_PATH = "C://Users/paulo/OneDrive/Documentos/Projeto_Automation/Clientes03"
CREDENTIALS_PATH = "./credentials3.txt"
# grupos_buscar = ['020372','020360','020365','020362']
numerdo_grupo_vencedor_campeao_amigao = ""


# %%
def read_xlsx_files(CLI_PATH):
    xlsx_files = []
    for file in os.listdir(CLI_PATH):
        if file.endswith(".xlsx"):
            xlsx_files.append(os.path.join(CLI_PATH, file))

    for xlsx_file in xlsx_files:
        df = pd.read_excel(xlsx_file)
        # Process the DataFrame here
        # print(df)

        cpf_cli = df.iloc[0, 1]
        dt_nasc = df.iloc[1, 1].date().strftime("%d/%m/%Y")
        grupo_filtro = df.iloc[2, 1]
        genero = df.iloc[3, 1]
        nacionalidade = df.iloc[4, 1]
        estado_civil = df.iloc[5, 1]
        Residenc_ext = df.iloc[6, 1]
        Expost_Polit = df.iloc[7, 1]
        tp_doc = df.iloc[8, 1]
        num_doc = df.iloc[9, 1]
        org_expd = df.iloc[10, 1]
        uf_exped = df.iloc[11, 1]
        Dt_expedi = df.iloc[12, 1].date().strftime("%d/%m/%Y")
        cep = df.iloc[13, 1]
        logradouro = df.iloc[14, 1]
        num_resid = df.iloc[15, 1]
        complemento = df.iloc[16, 1]
        bairro = df.iloc[17, 1]
        cidade = df.iloc[18, 1]
        estado = df.iloc[19, 1]
        celular = df.iloc[20, 1]
        email = df.iloc[21, 1]
        autorizacao = df.iloc[22, 1]
        profissao = df.iloc[23, 1]
        renda_mensal = df.iloc[24, 1]
        patrimonio = df.iloc[25, 1]
        num_grupo_possiveis = df.iloc[26, 1]

        # print(cpf_cli,dt_nasc ,genero,nacionalidade,estado_civil,Residenc_ext,Expost_Polit,tp_doc,num_doc,org_expd,Dt_expedi,
        #       cep,logradouro,num_resid,complemento,bairro,cidade,celular,email,autorizacao,profissao,renda_mensal,patrimonio,num_grupo_possiveis)

        return (
            cpf_cli,
            dt_nasc,
            grupo_filtro,
            genero,
            nacionalidade,
            estado_civil,
            Residenc_ext,
            Expost_Polit,
            tp_doc,
            num_doc,
            org_expd,
            uf_exped,
            Dt_expedi,
            cep,
            logradouro,
            num_resid,
            complemento,
            bairro,
            cidade,
            estado,
            celular,
            email,
            autorizacao,
            profissao,
            renda_mensal,
            patrimonio,
            num_grupo_possiveis,
        )


(
    cpf_cli,
    dt_nasc,
    grupo_filtro,
    genero,
    nacionalidade,
    estado_civil,
    Residenc_ext,
    Expost_Polit,
    tp_doc,
    num_doc,
    org_expd,
    uf_exped,
    Dt_expedi,
    cep,
    logradouro,
    num_resid,
    complemento,
    bairro,
    cidade,
    estado,
    celular,
    email,
    autorizacao,
    profissao,
    renda_mensal,
    patrimonio,
    num_grupo_possiveis,
) = read_xlsx_files(CLI_PATH)


# %%
def read_credentials(verbose=True):
    f = open(CREDENTIALS_PATH)
    url = f.readline().strip().split(":")[1].strip()
    username = f.readline().strip().split(":")[1].strip()
    company = f.readline().strip().split(":")[1].strip()
    password = f.readline().strip().split(":")[1].strip()

    if verbose:
        print(username, company, password)
    return (username, company, password)


(username, company, password) = read_credentials()

# %% [markdown]
# ##### Start Driver

# %%
import undetected_chromedriver as uc

options = uc.ChromeOptions()
#options.headless = True
# setting profile
#options.user_data_dir = r"C:\WhateverFolder"
options.browser_version = "120"
browserPrefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
options.add_experimental_option("prefs", browserPrefs)
options.add_argument("--disable-single-click-autofill")
options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
# options.add_argument('--incognito')
#options.add_argument("--window-size=1024,768")
#options.add_argument("--start-maximized")
#options.add_argument("--disable-extensions")
#options.add_argument("--disable-application-cache")
#options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--start-zoom=25")

# another way to set profile is the below (which takes precedence if both variants are used
#options.add_argument(
#    r"--user-data-dir=C:\WhateverFolder"
#)

#options.add_argument("--disable-gpu")
#options.add_argument("--no-sandbox")
#options.add_argument("--disable-setuid-sandbox")
#options.add_argument("--headless")

# just some options passing in to skip annoying popups
#options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
driver = uc.Chrome(use_subprocess=True, options=options)

# with driver:
driver.implicitly_wait(30)
#driver.get('chrome://settings/')
#driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.25);')
driver.get(
    "https://canal360i.cloud.itau.com.br/login/iparceiros"
)  # known url using cloudflare's "under attack mode"


def fechar_cliente():
    driver.close()


# %%
def find_element_click(driver, by, elem):
    try:
        return (
            WebDriverWait(driver, 30)
            .until(EC.element_to_be_clickable((by, elem)))
            .click()
        )
    except:
        print("Could not find element within 30 seconds")
        fechar_cliente()


# %%
def find_element_load(driver, by, elem):
    try:
        return WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((by, elem))
        )
    except:
        print("Could not find element within 30 seconds")
        fechar_cliente()


# %%
def find_elements_load(driver, by, elem):
    try:
        return WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((by, elem))
        )
    except:
        print("Could not find element within 30 seconds")
        fechar_cliente()


# %%
# Define Elements paths
ELEM_USERNAME_ID = "voxel-input-0"
ELEM_PASSWORD_ID = "voxel-input-1"
ELEM_LOGIN_BUTTON_XPATH = '//*[@id="btn-entrar"]'

# %%
#driver.execute_script("document.body.style.zoom='25%'")


elem_username = find_element_load(driver, By.ID, ELEM_USERNAME_ID)
elem_password = find_element_load(driver, By.ID, ELEM_PASSWORD_ID)
elem_login_button = find_element_load(driver, By.XPATH, ELEM_LOGIN_BUTTON_XPATH)

elem_username.send_keys(username)
elem_password.send_keys(password)
elem_login_button.click()


# %%
ELEM_DISCOUNT_ITEM_EXPANDER_XPATH = "menu-simulação e contratação"

# %%
elem_discount_item_expander = find_element_load(
    driver, By.ID, ELEM_DISCOUNT_ITEM_EXPANDER_XPATH
)
wait = WebDriverWait(driver, 30)

while (
    driver.current_url
    != "https://canal360i.cloud.itau.com.br/painel/wrapper/999/simulacao"
):
    elem_discount_item_expander = find_element_load(
        driver, By.ID, ELEM_DISCOUNT_ITEM_EXPANDER_XPATH
    )
    try:
        elem_discount_item_expander.click()
    except ElementClickInterceptedException:
        print("wwwwElementClickInterceptedException occurred. Retrying...")

# %%
shadow_host1 = find_element_load(
    driver, By.CSS_SELECTOR, "mf-parceirossimulacao[ng-version='13.4.0']"
)
shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", shadow_host1)
wait2 = WebDriverWait(shadow_root1, 30)
time.sleep(3)

# %%
ELEM_TIPO_PESSOA_ID = find_element_load(
    shadow_root1, By.CSS_SELECTOR, "input[class='ids-radio-button__input']"
)
wait2.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[class='ids-radio-button__input']")
    )
)
ELEM_TIPO_PESSOA_ID.click()

# %%
ELEM_CPF_CLASS = "input[id='cpfCnpj']"
ELEM_DT_NASC_CLASS = "input[id='dtalNascimentoFundacao']"
ELEM_TP_PRODUCT_ID = "div[id='codigoProduto']"
ELEM_FILTER_BUTTON_ID = "btnFiltrar"
# grupo = "veículos leves"

# %%
elem_cpf = find_element_load(shadow_root1, By.CSS_SELECTOR, ELEM_CPF_CLASS)
elem_cpf.send_keys(cpf_cli)

elem_dt_nasc = find_element_load(shadow_root1, By.CSS_SELECTOR, ELEM_DT_NASC_CLASS)
elem_dt_nasc.send_keys(dt_nasc)

elem_tp_product = find_element_load(shadow_root1, By.CSS_SELECTOR, ELEM_TP_PRODUCT_ID)
elem_tp_product.click()
# elem_tp_product.send_keys(grupo_filtro)
elem_tp_product_leves = find_element_load(
    driver, By.CSS_SELECTOR, "voxel-option[id='voxel-option-1']"
).click()
# driver.execute_script("arguments[0].click();", elem_tp_product)

elem_filter_button = find_element_load(shadow_root1, By.ID, ELEM_FILTER_BUTTON_ID)
elem_filter_button.click()


# %%
def contratar_cota():
    # Seleciona clicar em creditos disponiveis
    ELEM_TP_PRODUCT_ID = "//*[@id='voxel-modal-0']/voxel-modal-footer/footer/button"
    ELEM_EXIB_CRED_WW = find_element_load(driver, By.XPATH, ELEM_TP_PRODUCT_ID)
    ELEM_EXIB_CRED_WW.click()

    # Clica em exibir creditos
    Ordernar_ID = "voxel-icon[data-name='valor_total_credito']"
    Ordernar = find_element_load(shadow_root1, By.CSS_SELECTOR, Ordernar_ID)
    Ordernar.click()

    ELEM_TP_PRODUCT_ID = "voxel-icon[variant='secondary']"
    ELEM_EXIB_CRED_XPT = find_elements_load(
        shadow_root1, By.CSS_SELECTOR, ELEM_TP_PRODUCT_ID
    )[0]
    ELEM_EXIB_CRED_XPT.click()

    # Clica em contratar a cota
    ELEM_TP_G_ID = "button[voxelbutton]"
    ELEM_SEGURO_CLASS = (
        "input[class='ids-switch__input ng-untouched ng-pristine ng-valid']"
    )

    ELEM_EXIB_CRED_XPT_BT = find_elements_load(
        shadow_root1, By.CSS_SELECTOR, ELEM_TP_G_ID
    )[0]
    ELEM_SEGURO = find_elements_load(shadow_root1, By.CSS_SELECTOR, ELEM_SEGURO_CLASS)[0]

    #driver.execute_script("arguments[0].scrollIntoView(true)", ELEM_EXIB_CRED_XPT_BT)

    # ELEM_TP_G_ID = "button[voxelbutton]"

    elem_exib_cred_xpt_bt = find_elements_load(
        shadow_root1, By.CSS_SELECTOR, ELEM_TP_G_ID
    )
    
    while True:
        try:
            if elem_exib_cred_xpt_bt[0].is_displayed():
                elem_exib_cred_xpt_bt[0].click()
                break
        except (
            ElementClickInterceptedException,
            StaleElementReferenceException,
            NoSuchElementException,
        ):
            print("rrrrrElementClickInterceptedException occurred. Retrying...")

    # Selecionar o Shadow Content de cadastro de cliente
    shadow_host2 = find_element_load(
        driver, By.CSS_SELECTOR, "mf-iparceiros-cadastrocliente[ng-version='13.4.0']"
    )
    shadow_root2 = driver.execute_script("return arguments[0].shadowRoot", shadow_host2)
    
    # Contratação de consórcio
    ELEM_GENERO_ID = "div[id='voxel-select-0']"
    ELEM_NACIONALIDADE_ID = "div[id='voxel-select-1']"
    ELEM_ESTADO_CIVIL_ID = "div[id='voxel-select-2']"
    ELEM_EXTERIOR_ID = "input[id='voxel-radio-button-2']"
    ELEM_EXPOST_POLIT_ID = "input[id='voxel-radio-button-6']"
    ELEM_TIPO_DOCUMETO_ID = "div[id='voxel-select-value-3']"
    ELEM_NUMERO_DOCUMENTO_ID = "input[id='numeroDocumento']"
    ELEM_ORGAO_ID = "input[id='orgaoExpedidor']"
    ELEM_UF_EXPEDIDOR_ID = "input[id='mat-input-1']"
    ELEM_DATA_EXPD_ID = "input[id='dataExpedicao']"
    ELEM_CEP_ID = "input[id='cep']"
    ELEM_LOGRADOURO_ID = "input[id='logradouro']"
    ELEM_NUMERO_RESIDENC_ID = "input[id='numero']"
    ELEM_COMPLEMENTO_ID = "input[id='complemento']"
    ELEM_BAIRRO_ID = "input[id='bairro']"
    ELEM_CIDADE_ID = "input[id='cidade']"
    ELEM_UF_ID = "input[id='uf']"
    ELEM_CEL_ID = "input[id='celular']"
    ELEM_EMAIL_ID = "input[id='email']"
    ELEM_AUTORIZACAO_ID = "input[id='voxel-radio-button-3']"
    ELEM_PROFISSAO_ID = "input[id='mat-input-0']"
    ELEM_RENDA_MENSAL_ID = "input[id='rendaMensal']"
    ELEM_PATRIMONIO_ID = "input[id='patrimonio']"
    ELEM_CONTINUAR_ID = "button[class='ids-button']"

    # Genero
    ELEM_GENERO = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_GENERO_ID)
    ELEM_GENERO.click()
    ELEM_GENERO_MASC = find_element_load(
        driver, By.CSS_SELECTOR, "voxel-option[id='voxel-option-0']"
    ).click()

    # Nacionalidade
    ELEM_NACIONALIDADE = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_NACIONALIDADE_ID
    )
    ELEM_NACIONALIDADE.click()
    ELEM_NACIONALIDADE_BR = driver.find_element(
        By.CSS_SELECTOR, "voxel-option[id='voxel-option-11']"
    ).click()

    # Estado Civil
    ELEM_ESTADO_CIVIL = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_ESTADO_CIVIL_ID
    )
    ELEM_ESTADO_CIVIL.click()
    ELEM_ESTADO_CIVIL_ID_Solt = find_element_load(
        driver, By.CSS_SELECTOR, "voxel-option[id='voxel-option-2']"
    ).click()
    ELEM_EXTERIOR = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_EXTERIOR_ID)
    ELEM_EXTERIOR.click()

    ELEM_EXPOST_POLIT = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_EXPOST_POLIT_ID
    )
    ELEM_EXPOST_POLIT.click()

    ELEM_TIPO_DOCUMETO = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_TIPO_DOCUMETO_ID
    )
    ELEM_TIPO_DOCUMETO.click()
    ELEM_TIPO_DOCUMETO_RG = find_element_load(
        driver, By.CSS_SELECTOR, "voxel-option[id='voxel-option-8']"
    ).click()
    
    # Documento
    ELEM_NUMERO_DOCUMENTO = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_NUMERO_DOCUMENTO_ID
    )
    ELEM_NUMERO_DOCUMENTO.send_keys(num_doc)

    ELEM_ORGAO = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_ORGAO_ID)
    ELEM_ORGAO.send_keys(org_expd)

    ELEM_UF_EXPEDIDOR = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_UF_EXPEDIDOR_ID
    )
    ELEM_UF_EXPEDIDOR.send_keys(uf_exped)
    ELEM_UF_EXPEDIDOR_MG = find_element_load(
        driver, By.CSS_SELECTOR, "mat-option[id='mat-option-10']"
    ).click()

    ELEM_DATA_EXPD = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_DATA_EXPD_ID)
    ELEM_DATA_EXPD.send_keys(Dt_expedi)

    # RESIDENCIA
    ELEM_CEP = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_CEP_ID)
    ELEM_CEP.send_keys(cep)

    ELEM_LOGRADOURO = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_LOGRADOURO_ID
    )
    ELEM_LOGRADOURO.send_keys(logradouro)

    ELEM_NUMERO_RESIDENC = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_NUMERO_RESIDENC_ID
    )
    ELEM_NUMERO_RESIDENC.send_keys(num_resid)

    ELEM_COMPLEMENTO = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_COMPLEMENTO_ID
    )
    ELEM_COMPLEMENTO.send_keys(complemento)

    ELEM_BAIRRO = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_BAIRRO_ID)
    ELEM_BAIRRO.send_keys(bairro)

    ELEM_CIDADE = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_CIDADE_ID)
    ELEM_CIDADE.send_keys(cidade)

    ELEM_UF = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_UF_ID)
    ELEM_UF.send_keys(estado)

    # CONTATO E DADOS PESSOAIS
    ELEM_CEL = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_CEL_ID)
    ELEM_CEL.send_keys(celular)

    ELEM_EMAIL = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_EMAIL_ID)
    ELEM_EMAIL.send_keys(email)

    ELEM_AUTORIZACAO_ID = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_AUTORIZACAO_ID
    )
    #driver.execute_script("arguments[0].scrollIntoView(true)", ELEM_AUTORIZACAO_ID)
    ELEM_AUTORIZACAO_ID.click()
    ELEM_PROFISSAO = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_PROFISSAO_ID)
    ELEM_PROFISSAO.send_keys(profissao)
    ELEM_PROFISSAO_select = find_elements_load(driver, By.ID, "mat-autocomplete-0")[0]
    ELEM_PROFISSAO_select.click()

    ELEM_RENDA_MENSAL = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_RENDA_MENSAL_ID
    )
    ELEM_RENDA_MENSAL.send_keys(renda_mensal)

    ELEM_PATRIMONIO = find_element_load(
        shadow_root2, By.CSS_SELECTOR, ELEM_PATRIMONIO_ID
    )
    ELEM_PATRIMONIO.send_keys(patrimonio)

    ELEM_CONTINUAR = find_element_load(shadow_root2, By.CSS_SELECTOR, ELEM_CONTINUAR_ID)
    ELEM_CONTINUAR.click()

    # Selecionar o Shadow Content de Contratação
    shadow_host3 = find_element_load(
        driver, By.CSS_SELECTOR, "mf-iparceiros-contratacao[ng-version='13.4.0']"
    )
    shadow_root3 = driver.execute_script("return arguments[0].shadowRoot", shadow_host3)

    INPUT_SELECIONADO = "voxel-form-selection__input--radio ng-dirty ng-touched"

    SELEC_FORMA_PAGA = find_element_load(shadow_root3, By.ID, "voxel-radio-button-1")
    SELEC_FORMA_PAGA_V = find_element_load(
        shadow_root3, By.CSS_SELECTOR, "input[class='ids-radio-button__input']"
    )

    while True:
        try:
            SELEC_FORMA_PAGA.click()
            if SELEC_FORMA_PAGA.is_selected:
                print("Deu certo migao")
                break
        except (
            ElementClickInterceptedException,
            StaleElementReferenceException,
            NoSuchElementException,
        ):
            print("vvvvvvElementClickInterceptedException occurred. Retrying...")

    # Forma de Receber
    FORM_RECEBER_ID = "input[id='voxel-radio-button-4']"
    TERMOS_CONTRATA_1_ID = "input[id='voxel-checkbox-1']"
    TERMOS_CONTRATA_2_ID = "input[id='voxel-checkbox-2']"

    FORM_RECEBER = find_element_load(shadow_root3, By.CSS_SELECTOR, FORM_RECEBER_ID)
    #driver.execute_script("arguments[0].scrollIntoView(true)", FORM_RECEBER)
    FORM_RECEBER.click()

    TERMOS_CONTRATA_1 = find_element_load(
        shadow_root3, By.CSS_SELECTOR, TERMOS_CONTRATA_1_ID
    )
    TERMOS_CONTRATA_1.click()

    TERMOS_CONTRATA_2 = find_element_load(
        shadow_root3, By.CSS_SELECTOR, TERMOS_CONTRATA_2_ID
    )
    TERMOS_CONTRATA_2.click()

    BUTTON_FIM_ID = "button[class='ids-button']"

    BUTTON_FIM = find_element_load(shadow_root3, By.CSS_SELECTOR, BUTTON_FIM_ID)
    #driver.execute_script("arguments[0].scrollIntoView(true)", BUTTON_FIM)
    BUTTON_FIM.click()
    BUTTON_CONTRATAR_ID = "button[id='btn-contratar-formalizacao']"

    BUTTON_CONTRATAR = find_element_load(
        shadow_root3, By.CSS_SELECTOR, BUTTON_CONTRATAR_ID
    )

    while True:
        try:
            #BUTTON_CONTRATAR.click()
            driver.save_screenshot("scream.png")
            print("Parabens Venda Realizada")
            break
        except Exception:
            print("Tentando Clicar de novo.....")

    #return True


# %%
def verifica_grupo(row_gp):
    ELEM_TP_PRODUCT_ID = "//*[@id='voxel-modal-0']/div[2]/button"
    ELEM_SELECT_TABLE_ID = "table[class='ng-star-inserted']"
    ELEM_SELECT_TABLE = find_element_load(
        shadow_root1, By.CSS_SELECTOR, ELEM_SELECT_TABLE_ID
    )
    wait = WebDriverWait(driver, 30)

    if row_gp == []:
        driver.close()

    for i in range(len(row_gp)):
        if row_gp[i] is not None:
            if row_gp[i].text in num_grupo_possiveis:
                print("Valor Encontrado", row_gp[i].text)
                #driver.execute_script("arguments[0].scrollIntoView(true)", row_gp[i])
                grupoEncontrado = row_gp[i].text

                while True:
                    try:
                        if row_gp[i].is_displayed():
                            driver.execute_script(
                                "arguments[0].scrollIntoView(true)", row_gp[i]
                            )
                            row_gp[i].click()
                            break

                    except (
                        ElementClickInterceptedException,
                        StaleElementReferenceException,
                        NoSuchElementException,
                    ):
                        print(
                            "xxxxxxElementClickInterceptedException occurred. Retrying...",
                            row_gp[i].text,
                        )
                
                numerdo_grupo_vencedor_campeao_amigao = row_gp[i].text
                contratar_cota()
                driver.save_screenshot("print-", grupoEncontrado, ".png")
                time.sleep(60000)


# %%
# %%tee capt
shadow_host1 = find_element_load(
    driver, By.CSS_SELECTOR, "mf-parceirossimulacao[ng-version='13.4.0']"
)
shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", shadow_host1)

ELEM_SELECT_PAGE_ID = "select[style='cursor: pointer;']"
ELEM_SELECT_TABLE_ID = "table[class='ng-star-inserted']"
ELEM_SELECT_TABLE = find_element_load(
    shadow_root1, By.CSS_SELECTOR, ELEM_SELECT_TABLE_ID
)

for x in list(range(90)):
    #if x == 0:
    print("Loop:", x)
    for i in list(range(3)):
        while not ELEM_SELECT_TABLE.is_displayed:
            try:
                # print("Achou migao", )
                break
            except (ElementClickInterceptedException, NoSuchElementException):
                print("Filtrando Novamente...")
        # print("Execucao Indice",i )
        ELEM_SELECT_PAGE = Select(find_elements_load(shadow_root1, By.CSS_SELECTOR, ELEM_SELECT_PAGE_ID)[1])
        ELEM_SELECT_PAGE.select_by_index(i)
        row_gp = find_elements_load(shadow_root1, By.ID, "idGrupoBtn")
        try:
            verifica_grupo(row_gp)
        except Exception as ex:
            print("Ocorreu um erro na pagina", i + 1, "do Loop", x, "Filtrando Novamente...")
            
    #if x > 0:
        #print("Loop:", x)
    contador = 1
    while True:
        agora = datetime.now()
        formato = "%d-%m-%Y %H:%M:%S"
        data_formatada = agora.strftime(formato)
        try:
            if elem_filter_button.is_displayed:
                #driver.execute_script("arguments[0].scrollIntoView(true)", elem_filter_button)
                elem_filter_button.click()
                break
        except (ElementClickInterceptedException, NoSuchElementException):
            print("Filtrando Novamente... ", "Tentativa ", contador, " - ", data_formatada)
            contador += 1
            # for i in list(range(3)):
            #     while not ELEM_SELECT_TABLE.is_displayed:
            #         try:
            #             # print("Achou migao222", )
            #             break
            #         except (ElementClickInterceptedException, NoSuchElementException):
            #             print("Filtrando Novamente...",)
            #         # print('Deu nao migaoo4444')
            #     # print("Execucao Indice",i )
            #     ELEM_SELECT_PAGE = Select(
            #         find_elements_load(
            #             shadow_root1, By.CSS_SELECTOR, ELEM_SELECT_PAGE_ID
            #         )[1]
            #     )
            #     row_gp = find_elements_load(shadow_root1, By.ID, "idGrupoBtn")
            #     verifica_grupo(row_gp)
            #     ELEM_SELECT_PAGE.select_by_index(i)        

raise Exception("Reiniciando aplicação!")

# %%
# capt()

# %%
# driver.execute_script('arguments[0].scrollIntoView(true)',elem_filter_button)
# elem_filter_button.click()
