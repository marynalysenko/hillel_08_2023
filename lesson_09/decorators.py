class Shop:
    USERS_MAX_SIZE = 300

    def register(self, username, password1, password2, email):
        pass

    def login(self, username, password):
        pass

    @classmethod
    def build_new(cls, domain: str):
        # Host the application on {domain}
        # ...
        print(f"Hosted on {domain}")
        print(cls.USERS_MAX_SIZE)
        return

    @staticmethod
    def get_current_users_amount():
        # number = select count(id) from users;
        return 12

    def buy(self, product: dict):
        pass


zara = Shop()
bershka = Shop()

Shop.build_new("bershka.com")

zara.buy({"pants L": 122})

# це тотожний вираз
# Shop.buy(zara,
#          {
#          "pants L":122
#           }
#          )
