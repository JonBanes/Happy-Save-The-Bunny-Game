
tile_list = []

for first in range(1,9):
    tile_list.append(str(first))
    if first <= 7:
        for second in range(first + 1, 9):
            tile_list.append(str(first) + str(second))
            if first <= 6:
                for third in range(second + 1, 9):
                    tile_list.append(str(first) + str(second) + str(third))
                    if first <= 5:
                        for fourth in range(third + 1, 9):
                            tile_list.append(str(first) + str(second) + str(third) + str(fourth))
                            if first <= 4:
                                for fifth in range(fourth + 1, 9):
                                    tile_list.append(str(first) + str(second) + str(third) + str(fourth) + str(fifth))
                                    if first <= 3:
                                        for sixth in range(fifth + 1, 9):
                                            tile_list.append(str(first) + str(second) + str(third) + str(fourth) + 
                                                             str(fifth) + str(sixth))
                                            if first <= 2:
                                                for seventh in range(sixth + 1, 9):
                                                    tile_list.append(str(first) + str(second) + str(third) + 
                                                                     str(fourth) + str(fifth) + str(sixth) + str(seventh))
                                                    if first <= 1:
                                                        for eighth in range(seventh + 1, 9):
                                                            tile_list.append(str(first) + str(second) + str(third) + 
                                                                             str(fourth) + str(fifth) + str(sixth) + 
                                                                             str(seventh) + str(eighth))
#hooooooo boy, here's the end
                                                            
tile_list.sort(key=int)

print(tile_list)
print(len(tile_list))