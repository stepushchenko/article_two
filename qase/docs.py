import json
import os

import config


# decorator for updating QASE steps
def step(action: str, data: str = '', expected_result: str = ''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            Docs().prepare_step_data(action, data, expected_result)  # save step data
            return func(*args, **kwargs)  # step execution
        return wrapper
    return decorator


class Docs:
    def __init__(self, database_json: str = 'docs.json'):
        self.database_path = f'qase/{database_json}'

    def _prepare_case_data(self, request) -> dict:  # noqa: no-self-use
        result = {
            'steps': [],
            'automation': 2
        }
        return result

    def create_database(self, request) -> bool:
        if os.path.exists(self.database_path):
            self.delete_database()
        with open(self.database_path, 'w') as database:
            database.write(json.dumps(self._prepare_case_data(request)))
        return os.path.exists(self.database_path)

    def prepare_step_data(self, action: str, data: str = '', expected_result: str = ''):
        step_value = {
            'action': action,
            'data': data,
            'expected_result': expected_result
        }
        if os.path.exists(self.database_path):
            database: dict = self.read()
            database['steps'].append(step_value)
            self.save(database)

    def read(self) -> dict:
        with open(self.database_path) as database:
            return json.load(database)

    def save(self, updated_database: dict) -> bool:
        with open(self.database_path, 'w') as database:
            json.dump(updated_database, database)
        return self.read() == updated_database

    def delete_database(self) -> bool:
        os.remove(self.database_path)
        return not os.path.exists(self.database_path)
