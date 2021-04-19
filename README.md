# Eluvio_Assesment

I was invited to complete an assessment for a Data Science internship with Eluvio for summer 2021.

I used this opportunity to play around with my newly acquired PANDAS skills and create a need markdown file using jupyter notebooks.

For this assessment, I decided to split the data between those classified as 18+ and those not classified as 18+. I wanted to look at the titles of these Reddit posts to see if they showed any significant indication of censorship. I ended up downloading a csv file with swear and restricted words and checked if they were contained in the titles of all the posts. I found that the proportion of titles classified as 18+ was significantly higher than those not classified as 18+ (using a 2-prop Z test). I concluded that although the proportions were significantly different, there could be further investigation to find the best variables to predict restrictability on Reddit posts. 
