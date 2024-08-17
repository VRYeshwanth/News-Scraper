import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

window = tk.Tk()
window.title('News Extractor')
window.resizable(0,0)

def generate_news():
    output.delete("1.0", tk.END)
    world_news_url = "https://www.indiatoday.in/world"
    try:
        world_page = requests.get(world_news_url)
        world_soup = BeautifulSoup(world_page.text, "html.parser")
        wor_div = world_soup.find("div", class_ = "story__grid")
        w_article = wor_div.find_all("article")
        w_headlines = []
        for article in w_article:
            w_headlines.append(article.find("h2").text.strip())
        output.insert(tk.END, "International News :-\n")
        for i, headline in enumerate(w_headlines):
            output.insert(tk.END, f"{i+1}) {headline}\n")
    except Exception:
        messagebox.showerror("ERROR", f"We had a problem fetching International News")
    
    output.insert(tk.END, "\n")

    india_news_url = "https://www.indiatoday.in/india"
    try:
        india_page = requests.get(india_news_url)
        india_soup = BeautifulSoup(india_page.text, "html.parser")
        ind_div = india_soup.find("div", class_ = "story__grid")
        i_article = ind_div.find_all("article")
        i_headlines = []
        for article in i_article:
            i_headlines.append(article.find("h2").text.strip())
        output.insert(tk.END, "National News :-\n")
        for i, headline in enumerate(i_headlines):
            output.insert(tk.END, f"{i+1}) {headline}\n")
    except Exception:
        messagebox.showerror("ERROR", "We had a problem fetching India News")
    
    output.insert(tk.END, "\n")

    business_news_url = "https://www.indiatoday.in/business"
    try:
        business_page = requests.get(business_news_url)
        business_soup = BeautifulSoup(business_page.text, "html.parser")
        bus_div = business_soup.find("div", class_ = "story__grid")
        b_article = bus_div.find_all("article")
        b_headlines = []
        for article in b_article:
            b_headlines.append(article.find("h2").text.strip())
        output.insert(tk.END, "Business News :-\n")
        for i, headline in enumerate(b_headlines):
            output.insert(tk.END, f"{i+1}) {headline}\n")
    except Exception:
        messagebox.showerror("ERROR", "We had a problem fetching Business News")

inp_frame = tk.Frame(window)
inp_frame.pack()    

heading = tk.Label(inp_frame, text="News Scraper", font="Calibri 20 bold")
heading.grid(row=0, padx=20, pady=15)

output = tk.Text(inp_frame, wrap="word", width=50, height=15, font="Calibri 20")
output.grid(row=1, column=0, sticky="nsew")

scroll_bar = tk.Scrollbar(inp_frame, command=output.yview)
scroll_bar.grid(row=1, column=1, sticky="ns")

output.config(yscrollcommand=scroll_bar.set)

btn = tk.Button(window, text="Today's News", command=generate_news, font="Calibri 15")
btn.pack(padx=20, pady=15, ipadx=20, ipady=5)

window.mainloop()