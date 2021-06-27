def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    pairCount = len(redShirtSpeeds)
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	bluePointer = pairCount -1 if fastest else 0
	redPointer = pairCount -1 if fastest else 0
	counter = 0
	fastestSum = 0
	while counter < pairCount:
		
		if fastest:
			if(redShirtSpeeds[redPointer] > blueShirtSpeeds[bluePointer]):
				fastestSum += redShirtSpeeds[redPointer]
				redPointer -=1
			else:
				fastestSum += blueShirtSpeeds[bluePointer]
				bluePointer -=1
			
		else:
			if(redShirtSpeeds[redPointer] > blueShirtSpeeds[bluePointer]):
				fastestSum += redShirtSpeeds[redPointer]
			else:
				fastestSum += blueShirtSpeeds[bluePointer]
			redPointer +=1
			bluePointer +=1
			
	
		counter+=1
		
    return fastestSum

# want to find the N largest integers across both arrays
# sort the arrays and iterate through them with pointers
# count up to the number of pairs