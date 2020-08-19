def snail(snail_map):
    result = []
        final_length = len(snail_map) ** 2
            first_row = 0
                first_column = 0
                    last_row = len(snail_map) - 1
                        last_column = len(snail_map[0]) - 1
                            
                                while not len(result) == final_length:
                                    
                                            for i in range(first_column, last_column + 1):
                                                        result.append(snail_map[first_row][i])
                                                                first_row += 1
                                                                        
                                                                                for i in range(first_row, last_row + 1):
                                                                                            result.append(snail_map[i][last_column])
                                                                                                    last_column -= 1
                                                                                                            
                                                                                                                    if first_row > last_row: break
                                                                                                                            
                                                                                                                                    for i in range(last_column, first_column - 1, -1):
                                                                                                                                                result.append(snail_map[last_row][i])
                                                                                                                                                        last_row -= 1
                                                                                                                                                                
                                                                                                                                                                        if first_column > last_column: break
                                                                                                                                                                                
                                                                                                                                                                                        for i in range(last_row, first_row - 1, -1):
                                                                                                                                                                                                    result.append(snail_map[i][first_column])
                                                                                                                                                                                                            first_column += 1
                                                                                                                                                                                                                    
                                                                                                                                                                                                                        return result
                                                                                                                                                                                                                        
