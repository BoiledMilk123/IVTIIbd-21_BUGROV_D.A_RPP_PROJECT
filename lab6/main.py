from models import db, Client, Transaction
import cherrypy
from app_new import BankApp

print("BankApp imported successfully:", BankApp)

if __name__ == "__main__":
    db.connect()
    db.create_tables([Client, Transaction])

    client, _ = Client.get_or_create(name="Сидоров Сидор Сидорович")
    Transaction.get_or_create(
        client=client,
        date_time_str="2023-10-03 12:00",
        transaction_type="депозит"
    )

    cherrypy.engine.subscribe('before_request', db.connect)
    cherrypy.engine.subscribe('after_request', db.close)

    cherrypy.quickstart(BankApp(), "/")