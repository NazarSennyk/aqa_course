from base_repository import BaseRepo


class UserRepository(BaseRepo):
    def __init__(self):
        super().__init__()
        self.table_name = 'users'

    def get_user_by_id(self):
        self._cursor.execute(f"select from {self.table_name} where {self.table_name}.id = {user_id};")
        return self._cursor.fetchone()

    def insert_one(self):
        self._cursor.execute(f"insert into {self.table_name} (id, name, price) values ({id}, '{name}', {price});")

    def insert_into_table(self, table_name):
        self._cursor.execute(f"insert into {self.table_name} (id, product_id, quantity) values ({id}, {product_id}, {quantity});")

    def join_tables(self):
        self._cursor.execute(f"select products.name, products.price \n"
                             f"from products\n"
                             f" as prod inner join orders as ord on prod.id = ord.quantity;")
        return self._cursor.fetchone()

    def delete_by_email(self, email):
        self._cursor.execute(f"delete from users where {self.table_name}.email= '{email}';")






