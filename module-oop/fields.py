from abc import ABC, abstractmethod
from validators import TextValidator, IntegerValidator

class AbstractField(ABC):

    @abstractmethod
    def __init__(self, validators):
        pass
 
    @abstractmethod
    def is_valid(self, value):
        pass

class CharField(AbstractField):

    def __init__(self, validators=None):
        self.default_validator = [TextValidator(min_length=0, max_length=999)]
        self.all_validators = self.default_validator

        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(validator.is_valid(value) is True for validator in self.all_validators)        

class TextField(AbstractField):

    def __init__(self, validators=None):

        self.default_validator = [TextValidator(min_length=1001, max_length=3000)]
        self.all_validators = self.default_validator

        if isinstance(validators, list) and validators:
            self.all_validators += validators


    def is_valid(self, value):
        return all(validator.is_valid(value) is True for validator in self.all_validators)            


class IntegerField(AbstractField):
 
    def __init__(self, validators=None):
        
        self.default_validator = [IntegerValidator(min_value=128, max_value=1024)]
        self.all_validators = self.default_validator

        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(validator.is_valid(value) is True for validator in self.all_validators)       