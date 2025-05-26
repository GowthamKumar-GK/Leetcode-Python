num=list(map(int, input().split()))
add=0
for i in range (len(num)):
    if i%2!=0:
        pass
    else:
        add=add+num[i]
print(add)
        
    
"""from typing import List

class HouseRobber:
    
    def max_loot(self, house_values: List[int]) -> int:
        """"
        #Calculate the maximum amount of money that can be robbed 
        #without alerting the police (no adjacent houses robbed).
        
     #   Args:
       #     house_values: List of integers representing money in each house
            
       # Returns:
         #   Maximum money that can be robbed
        """"
        
        # Handle edge cases
        if not house_values:
            return 0
        if len(house_values) == 1:
            return house_values[0]
        
        # Initialize tracking variables
        # prev_max tracks maximum loot two houses back
        # current_max tracks maximum loot up to previous house
        prev_max, current_max = 0, 0
        
        for current_house_value in house_values:
            # Temporary store current_max before we update it
            temp = current_max
            # Current max is either:
            # 1. The value from robbing this house plus prev_max (non-adjacent)
            # 2. The current_max (not robbing this house)
            current_max = max(prev_max + current_house_value, current_max)
            # Update prev_max to what was current_max before this iteration
            prev_max = temp
            
        return current_max

# Example usage
if __name__ == "__main__":
    robber = HouseRobber()
    houses = [2, 7, 9, 3, 1]
    print(f"Maximum loot for {houses}: ${robber.max_loot(houses)}")
    # Output: Maximum loot for [2, 7, 9, 3, 1]: $12"""
