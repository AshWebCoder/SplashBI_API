from flask import Flask, jsonify, redirect, url_for
from flask_restx import Resource, Api
import psycopg2
import importlib
import argparse
import sys

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return redirect(url_for('execute'))


@api.route('/execute')
class ExecuteProcedure(Resource):
    def get(self):
        try:
            module_name = file_name
            print(f"Executing {method_name} from {module_name}")
            module = importlib.import_module(module_name)
            
            if hasattr(module, class_name):
                class_obj = getattr(module, class_name)
        
                if hasattr(class_obj, method_name):
                    method = getattr(class_obj, method_name)
                    
                    if callable(method):
                        conn = psycopg2.connect(
                            database="telestaff_dev_58", 
                            user="telestaff_dev_58", 
                            password="telestaff_dev_58", 
                            host="192.168.4.154", 
                            port="5432"
                        )
                        result = method(conn)
                        print("Process completed successfully.")
                        sys.exit(0) 
                        return jsonify(result)
                    else:
                        return {"status": "error", "message": f"{method_name} is not callable"}, 400
                else:
                    return {"status": "error", "message": f"Method {method_name} not found in {class_name}"}, 404
            else:
                return {"status": "error", "message": f"Class {class_name} not found in {file_name}"}, 404

        except Exception as e:
            return {"status": "error", "message": str(e)}, 500


def get_cli_args():
    """Parse the CLI arguments."""
    parser = argparse.ArgumentParser(description="Run Flask app with dynamic file, class, and method.")
    parser.add_argument('file_name', type=str, help="File Name without .py")
    parser.add_argument('class_name', type=str, help="Class name to import")
    parser.add_argument('method_name', type=str, help="Method name to invoke")
    args = parser.parse_args()

    return args.file_name, args.class_name, args.method_name

if __name__ == '__main__':
    global file_name, class_name, method_name
    file_name, class_name, method_name = get_cli_args()
    print(f"Running Flask app with file: {file_name}, class: {class_name}, method: {method_name}")

    # Hitting the /execute route automatically.
    with app.test_client() as client:
        response = client.get('/execute') 
        print(response.json)
    sys.exit(0)
