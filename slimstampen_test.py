
from slimstampen.spacingmodel import SpacingModel, Fact, Response



m = SpacingModel()

fact1 = Fact(fact_id = 1, question = "hello", answer = "bonjour")
fact2 = Fact(2, "dog", "chien")
fact3 = Fact(3, "cat", "chat")
fact4 = Fact(4, "computer", "ordinateur")

m.add_fact(fact1)
m.add_fact(fact2)
m.add_fact(fact3)
m.add_fact(fact4)

print(m.facts)

next_fact, new = m.get_next_fact(current_time = 34000)
next_fact, new




resp = Response(fact = next_fact, start_time = 34029, rt = 2207, correct = True)

m.register_response(resp)

print(m.responses)


next_fact, new = m.get_next_fact(current_time = 38000)

print(next_fact, new)

for f in m.facts:
    print(f, m.calculate_activation(38000 + m.LOOKAHEAD_TIME, f))

resp = Response(fact = next_fact, start_time = 38007, rt = 1890, correct = True)

m.register_response(resp)


for f in m.facts:
    print(f, m.calculate_activation(42000 + m.LOOKAHEAD_TIME, f))



next_fact, new = m.get_next_fact(current_time = 42000)
next_fact, new

print('At t=0: {}'.format(m.get_rate_of_forgetting(0, fact1)))



print('After 2 responses: {}'.format(m.get_rate_of_forgetting(50000, fact1)))

resp = Response(fact = fact1, start_time = 50000, rt = 1200, correct = True)
m.register_response(resp)

print('After 3 responses: {}'.format(m.get_rate_of_forgetting(60000, fact1)))

resp = Response(fact = fact1, start_time = 60000, rt = 1100, correct = True)
m.register_response(resp)

print('After 4 responses: {}'.format(m.get_rate_of_forgetting(70000, fact1)))

resp = Response(fact = fact1, start_time = 70000, rt = 1000, correct = True)
m.register_response(resp)

print('After 5 responses: {}'.format(m.get_rate_of_forgetting(80000, fact1)))


m.export_data("data.csv")

