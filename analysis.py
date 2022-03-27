import pandas as pd


class Analysis:
    @staticmethod
    def getData(path,sheet):
        return pd.DataFrame(pd.read_excel(path,sheet))

    @staticmethod
    def getColumns(data):
        return [i for i in data.columns]
    @staticmethod
    def combineFirstLastName(data):
        full_names = []
        for i in range(0,len(data["firstname"])):
            full_names.append(data["firstname"][i]+" "+data["lastname"][i])
        return full_names

    @staticmethod
    def totalSalesByEmployees(employee_data,order_data):
        """ Iterate all employees and the orders related to them. """
        results = {
            "employees": [],
            "sales": []
        }
        for index,employee in employee_data.iterrows():
            results["employees"].append(employee["firstname"]+" "+employee["lastname"])
            sales = 0
            for index,order in order_data.iterrows():
                if order["employee_id"] == employee["employee_id"]:
                    sales += float(order["unitprice"])*float(order["quantity"])
            results["sales"].append(sales)
        return pd.DataFrame(results)

    @staticmethod
    def salesByEmployee(name,employee_data,order_data,product_data):
        id = [row["employee_id"] for index,row in employee_data.iterrows() if row["firstname"]+" "+row["lastname"]==name][0]
        results = {
            "product": [],
            "sales": []
        }
        for index,order in order_data.iterrows():
            if order["employee_id"] == id:
                for index,product in product_data.iterrows():
                    if product["product_id"] == order["product_id"]:
                        results["product"].append(product["productname"])
                        results["sales"].append(float(order["unitprice"])*float(order["quantity"]))
        return pd.DataFrame(results)

    # @staticmethod
    # def salesByProduct(product_name,order_data,product_data):
    #     id = [row["product_id"] for index,row in product_data.iterrows() if row["productname"]==product_name][0]
    #     results = {
    #         "products": [],
    #         "sales": []
    #     }
    #     return pd.DataFrame(results)

    @staticmethod
    def totalSalesByProduct(product_data,order_data):
        """ Iterate all products and the orders related to them. """
        results = {
            "products": [],
            "sales": []
        }
        for index,product in product_data.iterrows():
            results["products"].append(product["productname"])
            sales = 0
            for index,order in order_data.iterrows():
                if order["product_id"] == product["product_id"]:
                    sales += float(order["unitprice"])*float(order["quantity"])
            results["sales"].append(sales)
        return pd.DataFrame(results)


# Read data from xlsx
# order_data = Analysis.getData("my_shop_data.xlsx","order")
# employee_data = Analysis.getData("my_shop_data.xlsx","employee")
#
# # Extract column names
# order_columns = Analysis.getColumns(order_data)
# employee_columns = Analysis.getColumns(employee_data)

#print(Analysis.combineFirstLastName(employee_data))
#Analysis.salesByEmployees(employee_data,order_data)


#
