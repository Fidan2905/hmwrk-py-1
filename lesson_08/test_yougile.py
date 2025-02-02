
from Page.PageObjectAPI import Yougile

login = "fidanmahmudova2905@gmail.com"
password = "fidanmahmudova"
companyId = "415c4047-228b-4934-aad2-a405a867c567"
apikey = "ZaTRqRUoW8oCnHHY4NJm+LSzQw79ii68fS9N2pn9e0Y49Oc54WRHtQn4nIJrM0Ej"
api = Yougile("https://ru.yougile.com/api-v2")


def test_getlistcomp_positive():
    companies = api.get_list_projects(apikey)
    assert companies["content"][1]["title"] == "Проект дз", "Ошибка!"


def test_getlistcomp_negative():
    companies = api.get_list_projects(apikey)
    assert companies["content"][10]["title"] == 0, "Ошибка!"


def test_postcreate_negative():
    companies = api.create_project(apikey, "")
    assert companies["statusCode"] == 400, "Не вернулась 400"


def test_getprojectbyid_positive():
    idpr = "415c4047-228b-4934-aad2-a405a867c567"
    companies = api.get_project_by_id(apikey, idpr)
    assert companies["title"] == "Potrocol", "Неверный проект!"


def test_getprojectbyid_negative():
    companies = api.get_project_by_id(apikey, "11n1111111111111111")
    assert companies["statusCode"] == 404, "Не вернулась 400"


def test_putprojectbyid_positive():
    idpr = "415c4047-228b-4934-aad2-a405a867c567"
    companies = api.put_project_by_id_title(apikey, idpr, "Делай ноги!")
    assert companies["id"] == idpr, "Неверный проект!"


def test_putprojectbyid_negative():
    idpr = "1111111111111111111"
    companies = api.put_project_by_id_title(apikey, idpr, "Делай ноги!")
    assert companies["statusCode"] == 404, "Неверный проект!"
