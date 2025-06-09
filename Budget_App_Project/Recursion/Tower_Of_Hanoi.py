"""
NUMBER_OF_DISKS = 4
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

#You can move only top-most disks
#You can move only one disk at a time
#You cannot place larger disks on top of smaller ones

#The first rod is the source, where all the disks are stacked on top of each other at the beginning of the game.
#The second rod is an auxiliary rod, and it helps in moving the disks to the target rod.
#The third rod is the target, where all the disks should be placed in order at the end of the game.

def make_allowed_move(rod1, rod2):    
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True
                      
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # display our progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)            

        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)
           
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')
"""

# Set the number of disks for the Tower of Hanoi puzzle
NUMBER_OF_DISKS = 5

# Initialize the three rods:
# Rod A starts with all disks (largest to smallest from bottom to top)
# Rods B and C start empty
A = list(range(NUMBER_OF_DISKS, 0, -1))  # [5, 4, 3, 2, 1]
B = []  # Empty auxiliary rod
C = []  # Empty target rod

def move(n, source, auxiliary, target):
    """
    Recursive function to solve Tower of Hanoi puzzle
    
    Args:
        n: Number of disks to move
        source: Rod to move disks from (list)
        auxiliary: Helper rod for temporary storage (list)
        target: Rod to move disks to (list)
    """
    
    # Base case: if no disks to move, return
    if n <= 0:
        return
    
    # Step 1: Recursively move the top n-1 disks from source to auxiliary
    # This clears the way for the largest disk to be moved
    move(n - 1, source, target, auxiliary)
        
    # Step 2: Move the largest disk (nth disk) from source to target
    # This is the key move - moving the bottom disk to its final position
    target.append(source.pop())
        
    # Step 3: Display the current state of all rods after each move
    print(A, B, C, '\n')
        
    # Step 4: Recursively move the n-1 disks from auxiliary to target
    # This places all the smaller disks on top of the largest disk
    move(n - 1, auxiliary, source, target)

# Start the Tower of Hanoi solution
# Move all disks from rod A (source) to rod C (target) using rod B (auxiliary)
move(NUMBER_OF_DISKS, A, B, C)