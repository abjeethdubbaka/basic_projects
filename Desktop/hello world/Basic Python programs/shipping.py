class ShippingContainer:
    next_serial = 1337
    @classmethod
    def _generate_serial(cls):
        result =cls.next_serial
        cls.next_serial +=1
        return result




    def __init__(self,owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self._generate_serial()
