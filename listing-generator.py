import time

def generate_listing(product_name, keywords):
    print(f'Generating highly optimized listing for: {product_name}')
    time.sleep(1)
    return f'Title: Premium {product_name} | Top Keywords: {keywords}'

if __name__ == '__main__':
    print(generate_listing('Wireless Ergonomic Mouse', 'gaming, RGB, silent'))