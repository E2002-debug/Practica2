from flask import Blueprint, render_template, request, redirect, jsonify, Flask
from controls.tda.stack.stackOperation import StackOperation
from flask_cors import CORS

router = Blueprint('router', __name__)

# Página de inicio
@router.route('/')
def home():
    return render_template("template.html")

# Mostrar lista de comandos
@router.route('/comando')
def lista_comandos():
    file_path = r"C:\Users\USUARIO_PC\Desktop\ProyectosEstructura3\Practica1\Practica1\data\stack_data.json"
    try:
        pd = StackOperation.from_json(file_path)  # Cargar los datos desde JSON
        lista_comandos = list(pd)  # Convertir la instancia de StackOperation a lista
    except Exception as e:
        lista_comandos = []
        print(f"Error cargando comandos: {e}")
    return render_template("comando/lista.html", lista=lista_comandos, encontrado=None, not_found=None)

# Ver página para guardar comando
@router.route('/comando/ver')
def ver_guardar():
    return render_template("comando/guardar.html")

# Guardar comando
@router.route('/comando/guardar', methods=["POST"])
def guardar_comando():
    file_path = r"C:\Users\USUARIO_PC\Desktop\ProyectosEstructura3\Practica1\Practica1\data\stack_data.json"
    try:
        pd = StackOperation.from_json(file_path)  # Cargar los datos desde JSON
    except Exception as e:
        pd = StackOperation()
        print(f"Error inicializando pila: {e}")

    data = request.form
    
    if "comando" not in data:
        return jsonify({"error": "El comando no fue proporcionado"}), 400
        
    comando = data["comando"]
    pd.push(comando)
    try:
        pd.to_json(file_path)  # Guardar los datos en JSON después de agregar el comando
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    print("Comando guardado correctamente:", comando)
    return redirect("/comando", code=302)

@router.route('/comando/buscar', methods=["GET", "POST"])
def buscar_comando():
    tipo_busqueda = request.form.get("tipo_busqueda") 
    criterio = request.form.get("criterio")  
    file_path = r"C:\Users\USUARIO_PC\Desktop\ProyectosEstructura3\Practica1\Practica1\data\stack_data.json"

    try:
        pd = StackOperation.from_json(file_path) 

        if criterio:
            try:
                criterio_num = int(criterio)
                if tipo_busqueda == "1":
                    encontrado = pd.binary_search_secuencial(criterio_num)
                elif tipo_busqueda == "2":
                    encontrado = pd.binary_search(criterio_num)
            except ValueError:
                if tipo_busqueda == "1":
                    encontrado = pd.binary_search_secuencial(criterio)
                elif tipo_busqueda == "2":
                    encontrado = pd.binary_search(criterio)

            if encontrado:
                return render_template("comando/buscar.html", lista=list(pd), encontrado=encontrado, not_found=None)
            else:
                return render_template("comando/buscar.html", lista=list(pd), encontrado=None, not_found=criterio)
        else:
            return render_template("buscar.html", lista=list(pd), encontrado=None, not_found=None)

    except Exception as e:
        print(f"Error buscando comandos: {e}")
        return render_template("comando/buscar.html", lista=[], encontrado=None, not_found=criterio)

    

@router.route('/comando/ordenar', methods=["GET"])
def mostrar_ordenar():
    file_path = r"C:\Users\USUARIO_PC\Desktop\ProyectosEstructura3\Practica1\Practica1\data\stack_data.json"
    try:
        pd = StackOperation.from_json(file_path)
        return render_template("comando/ordenar.html", lista=list(pd))
    except Exception as e:
        print(f"Error cargando comandos: {e}")
        return render_template("comando/ordenar.html", lista=[])
    
@router.route('/comando/ordenar', methods=["POST"])
def ordenar_comando():
    campo = request.form["campo"]
    direccion = int(request.form["direccion"])
    algoritmo = int(request.form["algoritmo"])
    file_path = r"C:\Users\USUARIO_PC\Desktop\ProyectosEstructura3\Practica1\Practica1\data\stack_data.json"
    try:
        pd = StackOperation.from_json(file_path)
        if campo == "comando":
            pd.sort(direccion, algoritmo)
        return render_template("comando/ordenar.html", lista=list(pd))
    except Exception as e:
        print(f"Error ordenando comandos: {e}")
        return render_template("comando/ordenar.html", lista=[])


# Configuración del blueprint en la aplicación principal
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(router, url_prefix='/')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
