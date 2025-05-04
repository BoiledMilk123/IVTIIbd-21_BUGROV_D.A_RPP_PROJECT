import cherrypy
from models import Client, Transaction

class BankApp:
    @cherrypy.expose
    def index(self):
        return """
        <html>
        <head>
            <title>Банковское приложение</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: navy; }
                a { color: blue; text-decoration: none; }
                a:hover { text-decoration: underline; }
                table { border-collapse: collapse; width: 50%; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
            </style>
        </head>
        <body>
            <h1>Банковское приложение</h1>
            <a href='/clients'>Список клиентов</a>
        </body>
        </html>
        """

    @cherrypy.expose
    def clients(self):
        clients = Client.select()
        html = """
        <html>
        <head>
            <title>Список клиентов</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: navy; }
                table { border-collapse: collapse; width: 50%; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
            </style>
        </head>
        <body>
            <h1>Список клиентов</h1>
            <table>
                <tr><th>ID</th><th>Имя</th></tr>
        """
        for client in clients:
            html += f"<tr><td>{client.id}</td><td><a href='/client/{client.id}'>{client.name}</a></td></tr>"
        html += """
            </table>
            <br><a href='/'>Назад</a>
            <br><a href='/transaction/add'>Добавить транзакцию</a>
        </body>
        </html>
        """
        return html

    @cherrypy.expose
    def client(self, id):
        try:
            client = Client.get(Client.id == id)
            html = f"""
            <html>
            <head>
                <title>Клиент {client.name}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: navy; }}
                    ul {{ list-style-type: none; padding: 0; }}
                    li {{ margin: 5px 0; }}
                </style>
            </head>
            <body>
                <h1>Клиент: {client.name}</h1>
                <h2>Транзакции:</h2>
                <ul>
            """
            for trans in client.transactions:
                html += f"<li>{trans.date_time_str} - {trans.transaction_type} (<a href='/transaction/edit/{trans.id}'>Редактировать</a>)</li>"
            html += """
                </ul>
                <br><a href='/clients'>Назад к списку клиентов</a>
            </body>
            </html>
            """
            return html
        except Client.DoesNotExist:
            return "Клиент не найден"
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"

    @cherrypy.expose
    def transaction_add(self, **kwargs):
        if cherrypy.request.method == "POST":
            try:
                client_id = kwargs.get('client_id')
                date_time = kwargs.get('date_time')
                transaction_type = kwargs.get('transaction_type')

                if not all([client_id, date_time, transaction_type]):
                    return "Все поля должны быть заполнены"
                if transaction_type not in ["депозит", "кредит"]:
                    return "Неверный тип транзакции"

                client = Client.get(Client.id == client_id)
                Transaction.create(
                    client=client,
                    date_time_str=date_time,
                    transaction_type=transaction_type
                )
                raise cherrypy.HTTPRedirect("/clients")
            except Client.DoesNotExist:
                return "Клиент не найден"
            except Exception as e:
                return f"Ошибка при создании транзакции: {str(e)}"

        clients = Client.select()
        html = """
        <html>
        <head>
            <title>Добавить транзакцию</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: navy; }
                form { width: 50%; }
                label { display: block; margin: 10px 0 5px; }
                input, select { width: 100%; padding: 8px; }
                input[type=submit] { width: auto; background: navy; color: white; cursor: pointer; }
            </style>
        </head>
        <body>
            <h1>Добавить транзакцию</h1>
            <form action="/transaction/add" method="POST">
                <label for="client_id">Клиент:</label>
                <select name="client_id" id="client_id">
        """
        for client in clients:
            html += f"<option value='{client.id}'>{client.name}</option>"
        html += """
                </select>
                <label for="date_time">Дата и время:</label>
                <input type="text" name="date_time" id="date_time" value="2023-10-03 12:00">
                <label for="transaction_type">Тип транзакции:</label>
                <select name="transaction_type" id="transaction_type">
                    <option value="депозит">Депозит</option>
                    <option value="кредит">Кредит</option>
                </select>
                <br><br>
                <input type="submit" value="Добавить транзакцию">
            </form>
            <br><a href='/clients'>Назад к списку клиентов</a>
        </body>
        </html>
        """
        return html

    @cherrypy.expose
    def transaction_edit(self, id, **kwargs):
        try:
            transaction = Transaction.get(Transaction.id == id)
            if cherrypy.request.method == "POST":
                try:
                    client_id = kwargs.get('client_id')
                    date_time = kwargs.get('date_time')
                    transaction_type = kwargs.get('transaction_type')

                    if not all([client_id, date_time, transaction_type]):
                        return "Все поля должны быть заполнены"
                    if transaction_type not in ["депозит", "кредит"]:
                        return "Неверный тип транзакции"

                    transaction.client = Client.get(Client.id == client_id)
                    transaction.date_time_str = date_time
                    transaction.transaction_type = transaction_type
                    transaction.save()

                    raise cherrypy.HTTPRedirect(f"/client/{transaction.client.id}")
                except Client.DoesNotExist:
                    return "Клиент не найден"
                except Exception as e:
                    return f"Ошибка при обновлении транзакции: {str(e)}"

            clients = Client.select()
            html = f"""
            <html>
            <head>
                <title>Редактировать транзакцию</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: navy; }}
                    form {{ width: 50%; }}
                    label {{ display: block; margin: 10px 0 5px; }}
                    input, select {{ width: 100%; padding: 8px; }}
                    input[type=submit] {{ width: auto; background: navy; color: white; cursor: pointer; }}
                </style>
            </head>
            <body>
                <h1>Редактировать транзакцию</h1>
                <form action="/transaction/edit/{id}" method="POST">
                    <label for="client_id">Клиент:</label>
                    <select name="client_id" id="client_id">
            """
            for client in clients:
                selected = "selected" if client.id == transaction.client.id else ""
                html += f"<option value='{client.id}' {selected}>{client.name}</option>"
            html += f"""
                    </select>
                    <label for="date_time">Дата и время:</label>
                    <input type="text" name="date_time" id="date_time" value="{transaction.date_time_str}">
                    <label for="transaction_type">Тип транзакции:</label>
                    <select name="transaction_type" id="transaction_type">
                        <option value="депозит" {"selected" if transaction.transaction_type == "депозит" else ""}>Депозит</option>
                        <option value="кредит" {"selected" if transaction.transaction_type == "кредит" else ""}>Кредит</option>
                    </select>
                    <br><br>
                    <input type="submit" value="Сохранить изменения">
                </form>
                <br><a href='/client/{transaction.client.id}'>Назад к клиенту</a>
            </body>
            </html>
            """
            return html
        except Transaction.DoesNotExist:
            return "Транзакция не найдена"
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"

    @cherrypy.expose
    def test(self):
        return "Тестовый маршрут работает!"