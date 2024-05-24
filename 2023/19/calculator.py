
class Calculator():
    def __init__(self, data):
        self.data = data
        self.workflows = self.data[0]
        self.ratings = self.data[1]

    def calculate_rating_result(self, rating):
        # TODO
        return rating['x'] + rating['m'] + rating['a'] + rating['s']

    def is_condition_true(self, rating, condition):
        return ((rating[condition.left] > condition.right) and (condition.operator == '>')) \
            or ((rating[condition.left] < condition.right) and (condition.operator == '<'))

    def get_rating_is_accepted(self, rating, workflow_node):
        if workflow_node.value == 'R':
            return False
        if workflow_node.value == 'A':
            return True

        if workflow_node.value:
            return self.get_rating_is_accepted(rating, self.workflows[workflow_node.value])

        if self.is_condition_true(rating, workflow_node.condition):
            return self.get_rating_is_accepted(rating, workflow_node.if_node)
        else:
            return self.get_rating_is_accepted(rating, workflow_node.else_node)

    def calculate1(self):
        result = 0
        for rating in self.ratings:
            init_workflow = self.workflows['in']
            if self.get_rating_is_accepted(rating, init_workflow):
                result += self.calculate_rating_result(rating)
        return result

    def calculate2(self):
        pass
