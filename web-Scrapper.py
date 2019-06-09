from bs4 import BeautifulSoup
import requests

def main():
    page = requests.get("https://www.cricbuzz.com/live-cricket-scores/20242/eng-vs-pak-match-6-icc-cricket-world-cup-2019")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    for a in soup.find_all(name='div', attrs={'class': 'cb-min-bat-rw'}):
        score = a.find(name='span', attrs={'class': 'cb-font-20 text-bold'})
    
    score_tmp = str(score)
    score_tmp1 = score_tmp.split(" ")
    score_final = []

    for i in range(3, 7):
        score_final.append(score_tmp1[i])
   
    score_final_string = ""

    for x in score_final:
        score_final_string += " " + x
    
    print(score_final_string)

if __name__ == "__main__":
    main()