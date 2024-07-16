from behave import given, when, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Select

#assert, apenas serve para dar mensagem de erro, caso o código não encontre algo programado pra encontrar?
#o . é uma forma de por passos para o programa percorrer ?
# oque seria o context?
# porque no def when, só a ultimo context foi criado uma variavel?
# o select é apenas para selecionar a variavel?
# existe uma nomenclatura de nomes mais utilizados nos defs ?

@given(u'que estou na página do Instituto Joga Junto')
def step_on_instituto_page(context):
    context.browser = Firefox ()
    context.browser.get('www.institutojogajunto.org')
    browser_title = context.browser.title
    assert 'Instituto Joga Junto' in browser_title, "Titulo não encontrado."
    pass


@when(u'preencho o formulário de contato')
def step_fillform(context):
    context.browser.find_element_by_id(By.NAME,'email').send_keys('admin@admin.com')     
    context.browser.find_element_by_id(By.NAME,'nome').send_keys('Gabriel Ramos Ferreira')
    context.browser.find_element_by_id(By.NAME,'body').send_keys('Minha primeira automação com behave')
    selects_subjects = context.browser.find_element_by_id(By.NAME,'assunto').send_keys('Minha primeira automação com behave')
    Select = Select(selects_subjects)
    pass


@when(u'aperto o botão de enviar')
def step_impl(context):
    pass


@then(u'os dados são recebidos com sucesso!')
def step_impl(context):
    pass