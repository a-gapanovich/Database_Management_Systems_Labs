import json

# открыть файл
def open_file(path: str) -> list:
    with open(path) as file:
        data = json.loads(file.read())
        name_model = data["name"]
        data_model = data["data"]
        list_of_data = []
        for i in range(len(data_model)):
            dict_of_data = {
                "model": f"app.{name_model}",
                "pk": i + 1,
                "fields": data_model[i]
            }
            list_of_data.append(dict_of_data)
    return list_of_data


def write_into_file(path: str, list_of_data: list) -> None:
    with open(path, "w") as file:
        data = json.dumps(list_of_data)
        file.write(data)


list_of_data1 = open_file("json_files/classicmodels_table_customers.json")
write_into_file("DMS/fixtures/customers.json", list_of_data1)

list_of_data1 = open_file("json_files/classicmodels_table_employees.json")
write_into_file("DMS/fixtures/employees.json", list_of_data1)

list_of_data1 = open_file("json_files/classicmodels_table_offices.json")
write_into_file("DMS/fixtures/offices.json", list_of_data1)

list_of_data1 = open_file("json_files/classicmodels_table_orderdetails.json")
write_into_file("DMS/fixtures/orderdetails.json", list_of_data1)

list_of_data1 = open_file("json_files/classicmodels_table_orders.json")
write_into_file("DMS/fixtures/orders.json", list_of_data1)

list_of_data1 = open_file("json_files/classicmodels_table_payments.json")
write_into_file("DMS/fixtures/payments.json", list_of_data1)

list_of_data1 = open_file("json_files/classicmodels_table_productlines.json")
write_into_file("DMS/fixtures/productlines.json", list_of_data1)

list_of_data1 = open_file("json_files/classicmodels_table_products.json")
write_into_file("DMS/fixtures/products.json", list_of_data1)
