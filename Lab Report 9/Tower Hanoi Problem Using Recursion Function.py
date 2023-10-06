def tower_of_hanoi(num_disks, source_rod, destination_rod, auxiliary_rod):
    if num_disks == 0:
        return
    tower_of_hanoi(num_disks - 1, source_rod, auxiliary_rod, destination_rod)
    print(f"Move disk {num_disks} from rod {source_rod} to rod {destination_rod}")
    tower_of_hanoi(num_disks - 1, auxiliary_rod, destination_rod, source_rod)

if __name__ == "__main__":
    num_disks = 4
    tower_of_hanoi(num_disks, 'A', 'C', 'B')
