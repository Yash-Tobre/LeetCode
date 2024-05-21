

class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Step 1: Initialize an empty stack
        output_list = []

        # Step 2: Iterate through each asteroid in the list
        for asteroid in asteroids:
            # Step 3: Handle collisions while there are potential collisions
            while output_list and asteroid < 0 < output_list[-1]:
                # Step 4: Compare the sizes of the colliding asteroids
                if output_list[-1] < -asteroid:
                    # Pop the stack if the asteroid on the stack is smaller
                    output_list.pop()
                    continue
                elif asteroid == -output_list[-1]:
                    # Pop the stack if the asteroids are the same size (both explode)
                    output_list.pop()
                # Break if the current asteroid is destroyed
                break
            else:
                # Append the current asteroid to the stack if no collision
                output_list.append(asteroid)

        # Step 5: Return the stack which contains the remaining asteroids
        return output_list
