with open('input.txt', 'r') as file:
    content = file.readlines()

content_dict = {}
for line in content:
    content_dict[line] = 1

for index, line in enumerate(content):
    if line:
        cards = line.split('|')
        winning_cards = list(cards[0].split(':')[1].strip().split())
        my_cards = list(cards[1].strip().split())
        
        match=0
        for card in my_cards:
            if card in winning_cards :
                match += 1

        if match>0:    
            for i in range(index+1, index+ match +1):
                content_dict[list(content_dict.keys())[i]] += list(content_dict.values())[index]

print(sum(content_dict.values()))
