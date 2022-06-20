def parse(self, response):
    page = response.url[-1]
    file_name = f"posts-{page}.html"
    print("="*30 + file_name)
    with open(file_name, 'wb') as file:
        file.write(response.body)
