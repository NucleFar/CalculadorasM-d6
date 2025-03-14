from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
            body = request.json
            input_data = self.__validate_body(body)

            average = self.__calculate_average(input_data)
            format_response = self.__format_response(average)
            return format_response

    def __validate_body(self, body: Dict) -> List[float]:
            if "numbers" not in body:
                raise HttpUnprocessableEntity("Badly Formatted Body!")
        
            input_data = body["numbers"]
            return input_data

    def __calculate_average(self, numbers: List[float]) -> float:
            average = self.__driver_handler.average1(numbers)
            return average
    
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "average": round(average, 2)
            }
        }