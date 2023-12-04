with open('input.txt', 'r') as file:
    content = file.readlines()

total = 0
for line in content:
    if line:
        cards = line.split('|')
        winning_cards = list(cards[0].split(':')[1].strip().split())
        my_cards = list(cards[1].strip().split())
        
        match=0
        for card in my_cards:
            if card in winning_cards :
                match += 1
        if match>0:    
            total += 2**(match-1)
        
print("total: ", total)
