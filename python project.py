import requests
import bs4
URL="https://www.jumia.com.eg/ar/televisions/?display_size=49--43#catalog-listing"
page=requests.get(URL)
#print(page.content)
soup=bs4.BeautifulSoup(page.text ,"html.parser")
products=soup.findAll("div",{"class" : "info"})
#print(products)
for index , p in enumerate(products):
 print(f"the number of product : {index+1}")
 title=p.find("h3",{"class":"name"})
 price_befor_sale=p.findNext("div", {"class": "old"})
 Sale = p.findNext("div", {"class": "bdg _dsct _sm"})
 price_after_sale=p.find("div",{"class":"prc"})
 print(f"product_name : {title.text}")
 print(f"the price of product_befor_sale :{price_befor_sale.text}")
 print(f"Sale = {Sale.text}")
 print(f"the price of product_after_sale : {price_after_sale.text}")
 print("\n")
