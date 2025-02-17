class Actor:
    def __init__(self, name, uses):
        self.name=name
        self.uses=uses

class UseCase:
    def __init__(self, name, description):
        self.name=name
        self.description=description

usecases = []
report = UseCase("Report", "Report pothole and damage. Also assigns work order data and creates damage file")
usecases.append(report)
update = UseCase("Update Progress", "Update the progress of the report")

actors = []
citizen = Actor("Citizen", [report])
actors.append(citizen)
pwdrs = Actor("Public Works Department Repair System", [update])
actors.append(pwdrs)

for actor in actors:
    print(f"Actor: {actor.name} with use cases: {actor.uses}")