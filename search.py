from rich.console import Console
from get_center import get_center
import requests

console = Console()

def get_packages(html):
    package_list = []

    for h in html:
        package = {
            "name":    get_center(h, '<span class="package-snippet__name">', '</span>'),
            "version": get_center(h, '<span class="package-snippet__version">', '</span>'),
            "info":    get_center(h, '<p class="package-snippet__description">', '</p>')
        }
        
        package_list += [package]
    return package_list
        

def search(keyword, page = 1, enable_log = False):
    package_list = []
    req          = requests.get(f"https://pypi.org/search/?o=&q={keyword}&page={page}")
    
    if req.status_code == 200:
        html = get_center(req.text, '<ul class="unstyled" aria-label="Search results">', '</ul>')
        package_list += get_packages(html.split("<li>"))
        
        if enable_log:
            console.log(f"[I] Got {package_list.__len__()} package(s) from page {page}.")
        
        package_list += search(keyword, page + 1)

    else:
        if enable_log:
            console.log(f"[I] Done.")
    
    return package_list
