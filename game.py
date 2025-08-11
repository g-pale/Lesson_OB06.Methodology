"""
Битва героев — простая консольная игра с ООП.
Запуск: python game.py
"""

from dataclasses import dataclass
import random
import time


@dataclass
class Hero:
    name: str
    health: int = 100
    attack_power: int = 20

    def attack(self, other: "Hero") -> int:
        """
        Атакует другого героя и возвращает нанесённый урон.
        По требованиям урон равен силе удара.
        """
        damage = self.attack_power
        other.health = max(0, other.health - damage)
        return damage

    def is_alive(self) -> bool:
        """Жив ли герой?"""
        return self.health > 0


class Game:
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def start(self) -> None:
        """
        Запускает игру. Ходы чередуются, пока один из героев не погибнет.
        Выводит логи боя и объявляет победителя.
        """
        print("=== БИТВА ГЕРОЕВ ===")
        print(f"Игрок: {self.player.name} (HP {self.player.health}, ATK {self.player.attack_power})")
        print(f"Компьютер: {self.computer.name} (HP {self.computer.health}, ATK {self.computer.attack_power})")
        print("-" * 32)

        # Случайно выбираем, кто ходит первым
        turn_player = bool(random.getrandbits(1))
        print(("Первым ходит ИГРОК." if turn_player else "Первым ходит КОМПЬЮТЕР.") + "\n")

        round_num = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"— Раунд {round_num} —")

            if turn_player:
                input("Ваш ход! Нажмите Enter, чтобы атаковать... ")
                dmg = self.player.attack(self.computer)
                print(f"{self.player.name} наносит {dmg} урона. У {self.computer.name} осталось {self.computer.health} HP.")
                if not self.computer.is_alive():
                    break
            else:
                time.sleep(0.6)
                dmg = self.computer.attack(self.player)
                print(f"{self.computer.name} атакует и наносит {dmg} урона. У {self.player.name} осталось {self.player.health} HP.")
                if not self.player.is_alive():
                    break

            # смена хода
            turn_player = not turn_player
            round_num += 1
            print()

        print("\n=== ИТОГИ БОЯ ===")
        if self.player.is_alive() and not self.computer.is_alive():
            print(f"Победил {self.player.name}!")
        elif self.computer.is_alive() and not self.player.is_alive():
            print(f"Победил {self.computer.name}!")
        else:
            # На всякий — если случится редкая ничья (теоретически в этой версии не должна).
            print("Ничья!")

        print("\nСпасибо за игру!")

def main():
    print("Добро пожаловать в 'Битву героев'!")
    player_name = input("Введите имя вашего героя: ").strip() or "Игрок"
    player = Hero(name=player_name)  # по умолчанию 100 HP и 20 ATK
    computer = Hero(name="Компьютер")
    game = Game(player=player, computer=computer)
    print()
    game.start()


if __name__ == "__main__":
    main()
