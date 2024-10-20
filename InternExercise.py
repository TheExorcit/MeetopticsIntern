import requests 
from bs4 import BeautifulSoup
import json

url= "https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/n-bk7-plano-convex-lenses-ar-400-700nm-SLB-P-M.html"

response1 = requests.get(url)

print(response1.status_code)

soup1 = BeautifulSoup(response1.content, 'html.parser')

table1 = soup1.find('table', id='super-product-table')
contador = 0
products = []
if table1:
    tbody1 = table1.find('tbody')
    rows1 = tbody1.find_all('tr')
    for row1 in rows1:
        cells1 = row1.find(class_='grouped-item-cell grouped-item-name')
        if cells1 != None:
            a_tag = cells1.find('a')
            product_code = cells1.find(class_='sku-cell').text.strip()
            specs = {}
            if a_tag and 'href' in a_tag.attrs:
                href = a_tag['href']
                #print(href)
                response2 = requests.get(href)
                soup2 = BeautifulSoup(response2.content, 'html.parser')
                table2 = soup2.find('table', id='product-attribute-specs-table')
                if table2:
                    tbody2 = table2.find('tbody')
                    rows2 = tbody2.find_all('tr')
                    for row2 in rows2:
                        th = row2.find('th')
                        td = row2.find('td')
                        if th and td:
                            key = th.text.strip()
                            value = td.text.strip()
                            specs[key] = value
                product = {}
                product[product_code] = specs
                products.append(product)            
                contador = contador + 1

with open('products.json', 'w') as f:
    json.dump(products, f, indent=4)


print(contador)
        
