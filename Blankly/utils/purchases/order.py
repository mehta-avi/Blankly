import abc


class Order(abc.ABC):
    def __init__(self, response, order, interface):
        """
        Limit Order:
        needed = [
            ["product_id", str],    <- similar
            ["id", str],    <- similar
            ["created_at", float],  <- similar
            ["price", float],
            ["size", float],
            ["status", str],    <- similar
            ["time_in_force", str],     <-similar
            ["type", str],  <- similar
            ["side", str]   <- similar
        ]

        Market Order:
        needed = [
            ["product_id", str],
            ["id", str],
            ["created_at", float],
            ["funds", float],
            ["status", str],
            ["type", str],
            ["side", str]
        ]
        """
        self.__response = response
        self.__order = order
        self.Interface = interface

    def get_response(self) -> dict:
        """
        Get the original but parsed response from the exchange.
        """
        return self.__response

    def get_id(self) -> str:
        """
        Get the exchange-set order ID.
        """
        return self.__response["id"]

    def get_purchase_time(self) -> float:
        """
        Get when the purchase was created at. This may be set at slightly different points within an
        exchange's matching engine.
        """
        return self.__response["created_at"]

    def get_status(self, full=False) -> dict:
        """
        Calls the exchange with the order id of this purchase and returns the homogenized output
        Args:
            full: Set this to True to receive the all the order details. Default is False, which returns just the status
            field as (example) {"status:" "NEW"}
        """
        if full:
            return self.Interface.get_order(self.__order["product_id"], self.get_id())
        else:
            return {"status": self.Interface.get_order(self.__order["product_id"], self.get_id())["status"]}

    def get_time_in_force(self) -> str:
        """
        Get the exchange's set time_in_force value.
        """
        return self.__response["time_in_force"]

    def get_type(self) -> str:
        """
        Get order type, such as market/limit/stop.
        """
        return self.__response["type"]

    def get_side(self) -> str:
        """
        Get the order side such as buy/sell as a str.
        """
        return self.__response["side"]