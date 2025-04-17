from flask import Flask, jsonify,request
from controller import validate_input

app = Flask(__name__)

@app.route("/contact-form", methods=["POST"])
#Entry point of the API
def contact_form():
    try:
        data = request.get_json()
        #name from the request
        name=data.get("name")
        #email from the request
        email=data.get("email")
        #message from the request
        message=data.get("message")
        #Validate the input
        response = validate_input(name,email,message)
        if response:
            return jsonify(
                {
                    "message": "Form submitted successfully",
                    "response":response
                            }
                            ), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    

 


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)

