class GuestListExceeded(Exception):
    pass


class GuestNameAlreadyOnGuestList(Exception):
    pass


class GuestIsNotOnGuestList(Exception):
    pass


class GuestAlreadyOnGuestList(Exception):
    pass


class GuestList:
    def __init__(self, max_guest_number: int):
        self.max_guest_number = max_guest_number if max_guest_number > 0 else 0
        self.guest_dict = {}

    def add_guest(self, guest: object, guest_name: str):
        if len(self.guest_dict) >= self.max_guest_number:
            raise GuestListExceeded()

        if guest_name in self.guest_dict:
            raise GuestNameAlreadyOnGuestList()

        if guest in self.guest_dict.values():
            raise GuestAlreadyOnGuestList()

        self.guest_dict[guest_name] = guest

    def remove_guest_by_name(self, guest_name: str):
        if guest_name not in self.guest_dict:
            raise GuestIsNotOnGuestList()

        del self.guest_dict[guest_name]

    def remove_guest(self, guest: object):
        if guest not in self.guest_dict.values():
            raise GuestIsNotOnGuestList()

        for guest_name, guest_reference in self.guest_dict:
            if guest_reference is guest:
                del self.guest_dict[guest_name]
                break
