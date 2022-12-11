from basic_boardgame.objects.environment.player import Player
from basic_boardgame.utils.guest_list import GuestList


class Room:
    def __init__(self, room_name: str, max_guest_number: int):
        self.room_name = room_name
        self.max_guest_number = max_guest_number
        self.guests = GuestList(max_guest_number=max_guest_number)

    def get_in(self, player: Player):
        self.guests.add_guest(player, player.name)

    def get_out(self, player: Player):
        self.guests.remove_guest(player.name)
