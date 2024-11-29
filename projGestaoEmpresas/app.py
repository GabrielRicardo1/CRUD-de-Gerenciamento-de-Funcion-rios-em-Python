from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

employees = []

# Página inicial com menu
@app.route("/")
def home():
    return render_template("home.html")

# Lista funcionários
@app.route("/list")
def list_employees():
    return render_template("list.html", employees=employees)

# Cria um novo funcionário
@app.route("/create", methods=["GET", "POST"])
def create_employee():
    if request.method == "POST":
        new_employee = {
            "id": len(employees) + 1,
            "name": request.form["name"],
            "position": request.form["position"],
            "salary": float(request.form["salary"]),
            "cpf": request.form["cpf"],
            "hiring_date": request.form["hiring_date"],
        }
        employees.append(new_employee)
        return redirect(url_for("list_employees"))
    return render_template("create.html")

# Edita os funcionário
@app.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)
    if not employee:
        return "Funcionário não encontrado", 404
    if request.method == "POST":
        employee["name"] = request.form["name"]
        employee["position"] = request.form["position"]
        employee["salary"] = float(request.form["salary"])
        employee["cpf"] = request.form["cpf"]
        employee["hiring_date"] = request.form["hiring_date"]
        return redirect(url_for("list_employees"))
    return render_template("edit.html", employee=employee)

# Deletar funcionário
@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    global employees
    employees = [e for e in employees if e["id"] != employee_id]
    return redirect(url_for("list_employees"))

if __name__ == "__main__":
    app.run(debug=True)
