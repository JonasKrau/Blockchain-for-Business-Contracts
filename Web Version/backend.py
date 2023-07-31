from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Pfad zum "Contract"-Ordner
CONTRACT_FOLDER = os.path.join(os.getcwd(), 'Contract')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_and_store_contract', methods=['POST'])
def sign_and_store_contract():
    if 'contractFile' in request.files:
        contract_file = request.files['contractFile']
        if contract_file.filename != '':
            # Sicherstellen, dass der "Contract"-Ordner existiert
            if not os.path.exists(CONTRACT_FOLDER):
                os.mkdir(CONTRACT_FOLDER)
            # Datei speichern
            contract_file.save(os.path.join(CONTRACT_FOLDER, contract_file.filename))
            return "Contract file has been signed and stored successfully!"
    return "No contract file uploaded."

if __name__ == '__main__':
    app.run(debug=True)
