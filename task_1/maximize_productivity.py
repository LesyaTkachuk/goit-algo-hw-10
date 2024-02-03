import pulp

def maximize_productivity():
    # model initialisation
    model = pulp.LpProblem("Maximize productivity", pulp.LpMaximize)

    # variables definition
    L = pulp.LpVariable("Lemonad", lowBound=0, cat="Integer")
    J = pulp.LpVariable("Juice", lowBound=0, cat="Integer")

    # objective function for productivity maximisation
    model += L + J, "Production"

    # add constraints
    model += 2 * L + 1 * J <= 100, "Water"
    model += 1 * L <= 50, "Sugar"
    model += 1 * L <= 30, "Lemon juice"
    model += 2 * J <= 40, "Fruit puree"

    # problem solving
    model.solve()

    # print results
    print("Status of problem: ", pulp.LpStatus[model.status])
    print("Total optimal production amount is: ", pulp.value(model.objective))
    print("Optimal products amount:")
    for var in model.variables():
        print(f"{var.name} = {var.varValue}")
