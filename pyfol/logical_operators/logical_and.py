class LogicalAND:
    def __init__(self, _temp_pred1, _temp_pred2):
        self.temp_pred1 = _temp_pred1
        self.temp_pred2 = _temp_pred2

    def __repr__(self):
        return f"{self.temp_pred1} AND {self.temp_pred2}"