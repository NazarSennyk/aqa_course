from base_repository import BaseRepo


class TableRepo(BaseRepo):
    def __init__(self):
        super().__init__()
        self.table_name = 'users'

    def create_table_orders(self):
        self._cursor.execute(f"create table orders ( id int primary key, product_id int, quantity int);")
        return self._cursor.fetchone()

    def crate_table_products(self):
        self._cursor.execute(f"create table products (id int primary key, name varchar (25), price int);")
        return self._cursor.fetchone()
