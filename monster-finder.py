
def main():
    list_of_monsters = ["Ghouls", "Ghosts", "Vampires", "Zombies", "Witches", "Trolls"]

    file = open("./data/bat-cave.txt", "r")
    bat_cave_txt = file.read()

    for line in bat_cave_txt.split("."):
        for monster in list_of_monsters:
            if line.lower().find(monster.lower()) != -1:
                print(monster + " can be found on this line")
                print(line)
                number_of_monster(line, monster)

def number_of_monster(line, monster):
    monster_position = line.lower().find(monster.lower())
    print(monster_position)

    if (monster_position - 3 < 0 or line[(monster_position - 3)] == ""):
        print(line[(monster_position - 3)])
    else:
        print(line[(monster_position - 2)])



if __name__ == "__main__":
    main()