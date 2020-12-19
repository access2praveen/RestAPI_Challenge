from account import Account
from book import Book
import string
import random
import testdata


class TestCreateUser:

    BASE_URL = "https://demoqa.com"


    def randomString(self, stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(stringLength))
        return name

    def test_create_user(self):

        global user_id
        global token
        username = self.randomString()
        print("username:", username)
        password = "User!2345"
        self.auth = (username, password)
        account = Account(self.BASE_URL, username, password)
        response = account.create_user()
        user_id = response.json().get("userID")
        res = account.generate_token()
        token=res.json().get("token")


    def test_get_all_books(self):
        book = Book(self.BASE_URL);
        response = book.get_books()
        print(response.json())

    def test_getbook_by_isbn(self):
        isbn = Book(self.BASE_URL)
        response = isbn.get_book_by_isbn(isbn=testdata.current_isbn)
        print(response)

    def test_create_book(self):
        print("USERID", user_id)
        print("Token", token)
        payload = {
            "userId": user_id,
            "collectionOfIsbns": [
                {
                    "isbn": testdata.current_isbn
                }
            ]
        }
        newbook = Book(self.BASE_URL)
        response = newbook.create_book(payload, token)
        print(response)

    def test_update_book_isbn(self):
        payload = {
             "userId": user_id,
             "isbn": testdata.new_isbn
        }

        updatebook = Book(self.BASE_URL)
        response = updatebook.update_book(payload, token, testdata.current_isbn)
        print(response)

    def test_delete_book_by_isbn(self):
        payload = {
             "userId": user_id,
             "isbn": testdata.new_isbn
        }
        deletebook = Book(self.BASE_URL)
        response = deletebook.delete_book_by_isbn(payload, token)
        print(response)

    def test_delete_all_books(self):

        delbook = Book(self.BASE_URL)
        response = delbook.delete_books(user_id, token)
        print(response)

    def test_delete_user(self):
        Account.delete_user(userid=user_id,token=token)

